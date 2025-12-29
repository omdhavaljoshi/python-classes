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
    def __init__(self,title,author):
        super.__init__(title,author)

    def download(self):
        print(f"""
        {self.title} = 100MB
        """)

class Audio_book(Book):
    def __init__(self,title,author):
        super.__init__(title,author)
    def samples(self):
        print(f"""
        Sample 1 = {self.title}.WAV
        Sample 2 = {self.title}.WAV
        Sample 3 = {self.title}.WAV
        """)