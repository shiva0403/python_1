
class Customer:
    def __init__(self, id, name, bstreet, bcity, bstate, bzip, sstreet, scity, sstate, szip):
        self.id = id
        self.name = name
        self.baddr = self.Address(bstreet, bcity, bstate, bzip)
        self.saddr = self.Address(sstreet, scity, sstate, szip)

    class Address:
        def __init__(self, street='', city='', state='', zip=''):
            self.street = street
            self.city = city
            self.state = state
            self.zip = zip

        def __str__(self):
            return f"{self.street}, {self.city}, {self.state}, {self.zip}"

        def print_address(self):
            print(f"Street: {self.street}")
            print(f"City: {self.city}")
            print(f"State: {self.state}")
            print(f"Zip: {self.zip}")

c = Customer(1, "Krishna", "123 Main St", "Springfield", "IL", "62701", "456 Elm St", "Springfield", "IL", "62702")
print(c.id)
print(c.baddr)
print(c.baddr.print_address())
print(c.saddr.print_address())