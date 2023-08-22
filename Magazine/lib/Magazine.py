class Magazine :
    def __init__(self, name, category) :
        self.name = name
        self.category = category

    def all(self) :
        return  self.name + " " + self.category
    
    @classmethod
    def find_by_name(self, name) :
        for magazine in self.all() :
            if(magazine.name == name ):
                return magazine

    @classmethod
    def all(self) :
        pass

    
    
magazine = Magazine ("Gossip Girl", "Entertainment") 
magazine.name = "Forbes"
magazine.category = "Business"
print(magazine.name) 
print(magazine.category)
print(magazine.all())

