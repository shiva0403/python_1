class Course:
    def __init__(self, name, duration, *books):
        self.name = name
        self.duration = duration
        self.books = [self.Book(b) for b in books]

    def show_details(self):
        print(f"Course Name: {self.name}")
        print(f"Duration: {self.duration} months")
        print("Books:")
        for book in self.books:
            print(book)


    class Book:
        def __init__(self, title):
            self.title = title

        def __str__(self):
            return self.title

c1 = Course("Python", 6, "Python Basics", "Advanced Python", "Data Science with Python")

c1.show_details()