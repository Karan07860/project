class book():
    def __init__(self, title, author, isbn, availability):
        self.title = title
        self.author = author
        self.isbn = isbn
        self. availability = availability
        
    def borrow(self):
        print(f"\nUser has not borrowed {self.title} by {self.author}")
        
    def returnbook(self):
        print("book has been returned.")
        
    def chechAvailability(self):
        #check if its available
        if self.availability == False:
            print(f"")