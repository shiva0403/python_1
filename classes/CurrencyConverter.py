class CurrencyConverter:

    def __init__(self, currency, rate):
        self.currency = currency
        self.rate = rate

    def set_currency(self, currency):
        self.currency = currency

    def get_currency(self):
        return self.currency

    def set_rate(self, rate):
        self.rate = rate

    def get_rate(self):
        return self.rate

    def convert(self, amount):
        return self.currency + ' converted amount '+ str(amount * self.rate)

usd = CurrencyConverter("USD", 74.5)
print(usd.convert(100))