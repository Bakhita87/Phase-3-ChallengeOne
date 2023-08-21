# from Article import Article

class Author:
    def __init__(self, name = "Bakhita"):
        self.name = name 
       
   
    def get_name(self):
        return self.name
    def add_article(self, magazine ,title):
        self.article = Article(self.name, magazine, title)

author = Author()

print(author.name)

