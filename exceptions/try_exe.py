L = [1,2,3,4,5]

try:
    x = int(input('Enter an index: '))
    print(L[x])
except (IndexError, ValueError) as msg:
    print(msg)
# except IndexError as msg:
#     print('invalid index:', msg)
# except ValueError:
#     print('enter only int values')
except:
    print('some error occured')

print("program terminated")