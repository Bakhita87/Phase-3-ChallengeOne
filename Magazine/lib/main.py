from Article import Article
from Author import Author
from Magazine import Magazine



def main():
    author = Author("Bakhita")
    print(author.name())

    magazine = Magazine("Vogue", "Fashion")
    print(magazine.name())
    print(magazine.category())

    article = Article(author, magazine, " ")
    print(article.title())
    print(Article.all())
    print(Magazine.all())

    

    if __name__ == "__main__":
     main
