For this assignment, you will be working with a Magazine domain.
You are required to create three models: `Author`, `Article`, and `Magazine`.
For our purposes, an `Author` has many `Article`s, a `Magazine` has many `Article`s, and `Article`s belong to both `Author` and `Magazine`.
`Author` - `Magazine` is a many-to-many relationship.
Note: You should draw your domain on paper or on a whiteboard before you start coding. Remember to identify a single source of truth for your data.
Topics
- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods
Instructions
To get started, install all dependencies required for this project.
Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are easiest. Be careful: some of the later methods rely on earlier ones.
Note!  - You'll need to create your own test sample instances so that you can try/test out your code. Make sure your relationships and methods work in the console before submitting.
Writing error-free code is more important than completing all of the deliverables listed - prioritize writing methods that work over writing more methods that don't work. You should test your code in the console as you write.
Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.
Before you submit! - Save and run your code to verify that it works as you expect. If you have any methods that are not working yet, feel free to leave comments describing your progress.
Deliverables
Create a folder with the name of your project. Inside it, create 3 files named:
- Articles.py
- Author.py
- Magazine.py
Add any other necessary files required for this project inside this folder.
Write the following methods in the classes in the files created. Feel free to build out any helper methods if needed.
Sample of what your folder structure should look like:
Screenshot (154)-code challenga 1.png
NB: Pipfile sample for reference
[[source]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
ipdb = "*"

[dev-packages]

[requires]
python_version = "3.10"
Initializers, Readers, and Writers
Author
- `Author __init__(name)`
  - An author is initialized with a name, as a string.
  - A name **cannot** be changed after it is initialized.
- `Author name()`
  - Returns the name of the author
Magazine
- `Magazine __init__(name, category)`
  - A magazine is initialized with a name as a string and a category as a string
  - The name and category of the magazine **can be** changed after being initialized.
- `Magazine name()`
  - Returns the name of this magazine
- `Magazine category()`
  - Returns the category of this magazine
- `Magazine all()`
  - Returns a list of all Magazine instances
Article
- `Article __init__(author, magazine, title)`
  - An article is initialized with an author as an Author object, a magazine as a Magazine object, and title as a string.
  - An article **cannot** change its author, magazine, or title after it is has been initialized.
- `Article title()`
  - Returns the title for that given article
- `Article all()`
  - Returns a list of all Article instances
Object Relationship Methods
Article
- `Article author()`
  - Returns the author for that given article
- `Article magazine()`
  - Returns the magazine for that given article
Author
- `Author articles()`
  - Returns a list of Article instances the author has written
- `Author magazines()`
  - Returns a **unique** list of Magazine instances for which the author has contributed to
Magazine
- `Magazine contributors()`
  - Returns a list of Author instances who have written for this magazine
Associations and Aggregate Methods
Author
- `Author add_article(magazine, title)`
  - Given a magazine (as Magazine instance) and a title (as a string), creates a new Article instance and associates it with that author and that magazine.
- `Author topic_areas()`
  - Returns a **unique** list of strings with the categories of the magazines the author has contributed to
Magazine
- `Magazine find_by_name(name) class method`
  - Given a string of magazine's name, this method returns the first magazine object that matches
- `Magazine article_titles() class method`
  - Returns an list strings of the titles of all articles written for that magazine
- `Magazine contributing_authors()`
  - Returns a list of authors who have written more than 2 articles for the magazine