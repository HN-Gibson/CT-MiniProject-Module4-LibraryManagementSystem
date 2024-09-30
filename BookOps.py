

class Book:
    def __init__(self,title,author,genre,pub_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.pub_date = pub_date
        self.available = "Available"
 
    def borrow_book(self):
        if self.available == "Available":
            self.available = "Borrowed"
            
    def return_book(self):
        self.available = "Available"
    
    def __repr__(self):
        return f"\nTitle: '{self.title}'\nAuthor: {self.author}\nGenre: {self.genre}\nYear of Publication: {self.pub_date}\n{self.available}\n"




