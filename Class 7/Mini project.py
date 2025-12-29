class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f"""
        Title = {self.title}
        Author = {self.author}
        """)

class Ebook(Book):
    def __init__(self,title,author,downloadable):
        super.__init__(title,author)
        self.downloadable = downloadable
    def download(self):
        if self.downloadable == "yes":
            print(f"{self.title} is downloadable.")

        else:
            print(f"{self.title} is not downloadable.")

class Audio_book(Book):
    def __init__(self,title,author,samples):
        super.__init__(title,author)
        self.samples = samples

    def sample(self):
        if self.samples == "yes":
            print(f"{self.title} has audio samples.")

        else:
            print(f"{self.title} doesn't have audio samples.")

class Library:
    def __init__(self,name):
        self.name = name
        self.bookList = []
        print(f"""
           A library object is created with an empty Book List
        """)
    def add_book(self,book):
        self.bookList.append(book)
        print(f"""
          {book.title} written by {book.author} is added in the {self.name}
        """)
    def removeBook(self,title):
        index = self.bookList.index(title)
        self.bookList.pop(index)
    def showAllBook(self):
        pass
sunlight = Library("Sunrise Digital Library")
myExpWithTruth = Book("My Experiment With Truth","Mahatma Gandhi")
sunlight.add_book(myExpWithTruth)
sunlight.removeBook("My Experiment With Truth")