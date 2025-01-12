class Dept:
    def __init__(self):
        self.depts = {
            'HR': 'Human Resources',
            'IT': 'Information Technology',
            'FIN': 'Finance'
        }

    def __call__(self, dept):
        return self.depts[dept]

dept = Dept()
s = dept('HR')
print(s)

# converting this to a closure

def Dept():
    depts = {
        'HR': 'Human Resources',
        'IT': 'Information Technology',
        'FIN': 'Finance'
    }

    def caller(dept):
        return depts[dept]

    return caller

dept = Dept()
s = dept('IT')
print(s)
