def _get_guardrails_messages(conversation: List[DiningChatMessage]) -> List[Dict[str, str]]:
    messages = []
    for item in conversation:
        if item.role in ("human", "bot", "ai"):
            messages.append({'role': item.role, 'content': item.message})
    logger.info(f"Guardrails messages: {messages}")
    return messages


class Checks:
    num_checks = 2  # Updated to handle multiple validations if needed
    CHECK_OUT_OF_SCOPE = "check_out_of_scope"
    MASK_DATA = "mask_data"


class CheckHumanInputAction:

    log_id = 'check_human_input_action'

    @staticmethod
    async def execute(channel: DiningChannel) -> DiningChannel:
        with tracer.start_as_current_span("CheckHumanInputAction.execute") as span:
            TracerProviderSingleton.update_span(
                span, CheckHumanInputAction.log_id,
                channel.request.conversation_id,
                channel.request.x_amex_tracking_id
            )

            # Fetch Guardrails data
            rails = await CheckHumanInputAction._get_llmrails_cache(channel=channel)
            messages = CheckHumanInputAction._get_messages(channel)
            rails_output = await CheckHumanInputAction._get_rails_output(channel=channel, rails=rails, messages=messages)

            if rails_output.get("status_code") == 500:
                logger.error(msg := "Inappropriate language is not allowed")
                channel.exception = InappropriateLanguageException(msg)
                rails_output["status_code"] = 200
                raise channel.exception

            # Validate and process output
            validated_rails_output = CheckHumanInputAction._validate_rails_output(rails_output, channel)
            rails_output_fail = validated_rails_output.get("fail", "").lower()
            rails_output_unsafe = validated_rails_output.get("unsafe", "").lower()
            logger.info(f"Rails output (fail): {rails_output_fail}")
            logger.info(f"Rails output (unsafe): {rails_output_unsafe}")

            # Logic to handle fail and unsafe
            if rails_output_fail == "fail" and rails_output_unsafe == "unsafe":
                logger.info(msg := "Human input has inappropriate words and is out of scope")
                channel.exception = InappropriateLanguageException(msg)
                channel.input_safety.check_out_of_scope = False
                raise channel.exception
            elif rails_output_fail == "fail":
                logger.warning(msg := "Human input is out of scope")
                channel.exception = OutOfScopeException(msg)
                channel.input_safety.check_out_of_scope = False
                raise channel.exception
            elif rails_output_unsafe == "unsafe":
                logger.info(msg := "Human input has inappropriate words")
                channel.exception = InappropriateLanguageException(msg)
                channel.input_safety.check_out_of_scope = True
                raise channel.exception
            elif validated_rails_output.get("greeting", "").lower() == "greeting":
                logger.info(msg := "Human input is greeting")
                channel.exception = GreetingResponseException(msg)
                channel.input_safety.check_out_of_scope = True
                TracerProviderSingleton.record_message_scope(span, channel, "Human input is greeting")
            elif validated_rails_output.get("confirmation", "").lower() == "confirmation":
                logger.info(msg := "Human input is confirmation or thank you")
                channel.exception = ConfirmationResponseException(msg)
                channel.input_safety.check_out_of_scope = True
            elif validated_rails_output.get("support", "").lower() == "support":
                logger.info(msg := "Human input is a request for support")
                channel.exception = SupportResponseException(msg)
                channel.input_safety.check_out_of_scope = True
            else:
                logger.info(msg := "Human input is other")
                channel.input_safety.check_out_of_scope = True
                TracerProviderSingleton.record_message_scope(span, channel, "Human input is in scope")

            return channel

    @staticmethod
    def _get_messages(channel: DiningChannel):
        """Prepare messages for input to Guardrails."""
        messages = _get_guardrails_messages(conversation=channel.context.dining_conversation)
        messages.append({'role': 'user', 'content': channel.request.chat_utterance})

        if len(messages) >= 3:
            messages = messages[-3:]  # Keep only the last 3 messages for context

        # Log for debugging and tracking
        logger.info(f"Input messages from user to guardrails: {channel.request.chat_utterance}")
        logger.info(f"Input messages to guardrails: {messages}")
        return messages

    @staticmethod
    async def _get_rails_output(rails, messages, channel):
        """Call Guardrails to process user input and generate an output."""
        try:
            return await rails.generate_async(messages=messages)
        except PermissionDeniedError as e:
            logger.error(msg := f"Inappropriate language is not allowed: {str(e.message)}")
            channel.exception = InappropriateLanguageException(msg)
            raise channel.exception
        except Exception as e:
            logger.error(msg := f"Failed to run guardrails: {e}")
            channel.exception = SystemException(msg)
            raise channel.exception

    @staticmethod
    def _validate_rails_output(rails_output: dict, channel) -> dict:
        """
        Validate the output of the LLMRails object after executing the generate_async method.
        The output is determined by the logic provided in the configuration folder.

        Args:
            rails_output: Output of the guardrails object
            channel: The current communication channel object

        Returns:
            validated_output: A dictionary containing the validated output of LLMRails
        """

        if isinstance(rails_output, dict):
            rails_output = rails_output.get('content')
            if rails_output is None:
                logger.error(msg := "The output of guardrails is a dictionary without the key 'content'")
                channel.exception = SystemException(msg)
                raise channel.exception

        if not isinstance(rails_output, str):
            logger.error(msg := "The output of guardrails is not a string")
            channel.exception = SystemException(msg)
            raise channel.exception

        if Checks.num_checks > 1:
            if '\n' in rails_output:
                rails_output = rails_output.split('\n')
            else:
                logger.error(msg := "Incorrect output format from guardrails for multiple tasks")
                channel.exception = SystemException(msg)
                raise channel.exception

        if Checks.num_checks == 1:
            rails_output = [rails_output]

        if len(rails_output) != Checks.num_checks:
            logger.error(msg := f"Expected {Checks.num_checks} checks from guardrails but got {len(rails_output)}")
            channel.exception = SystemException(msg)
            raise channel.exception

        validated_output = {}

        for check_output in rails_output:
            if ':' not in check_output:
                logger.error(msg := "Invalid output format from guardrails for a single task")
                channel.exception = OutOfScopeException(msg)
                raise channel.exception

            try:
                check_output = check_output.split('\n')
                channel.request.chat_utterance = check_output[0]
                validated_output[check_output[1].split(':')[0]] = check_output[1].split(':')[1]
            except IndexError as e:
                logger.error(msg := f"Index error occurred while processing validated output of LLMRails: {e}")
                channel.exception = OutOfScopeException(msg)
                raise channel.exception
            except Exception as e:
                logger.error(msg := f"Exception occurred while processing validated output of LLMRails: {e}")
                channel.exception = OutOfScopeException(str(msg))
                raise channel.exception

        logger.info(f"validated_output: {validated_output}")
        return validated_output

    @staticmethod
    def _process_rails_outputs(rails_output: dict) -> str:
        """
        Determine whether checks passed or failed, and return the boolean value.

        Args:
            rails_output: A dictionary containing the validated output of LLMRails

        Returns:
            str: Result of the validation process
        """
        if all(val.lower() == "pass" for val in rails_output.values()):
            return "pass"
        elif all(val.lower() == "greeting" for val in rails_output.values()):
            return "greeting"
        elif all(val.lower() == "confirmation" for val in rails_output.values()):
            return "confirmation"
        elif all(val.lower() == "support" for val in rails_output.values()):
            return "support"
        elif all(val.lower() == "unsafe" for val in rails_output.values()):
            return "unsafe"
        else:
         return "fail"
