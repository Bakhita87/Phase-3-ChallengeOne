from Author import Author
from Magazine import Magazine
class Article :
    def __init__(self, author, magazine, title) :
        self.author = author
        self.magazine = magazine
        self.title = title
    
    def all(self) :
        # return self.author + " " + self.magazine + " " + self.title
        pass
    
author = Author("Bakhita")
magazine = Magazine("Gossip Girl", "Entertainment")

article = Article(author, magazine, "A love triangle")
print(article.all())
print(article.author.name)


