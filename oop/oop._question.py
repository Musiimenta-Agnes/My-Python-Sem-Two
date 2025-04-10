# Define a python  class named Book. ad attributes: title, author,and pages.
#  Provide a method in the class to display the information about the book.
#  Create an instance of the class and display the information


#Creating a class
class Book():
    def __init__(self, title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

       # creating a method
    def display_method(self):
        print(f"The book title is  {self.title} and the book author is {self.author} and the pages are {self.pages}" )

# Adding a method
information = Book('FOOD HUB', "Mr. Nkudi", '14 Pages')
        
# Displaying the information

information.display_method()

