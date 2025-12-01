class game:

    # class members 
      # body-----

    #methods of the class / behaviours
    def game_details(self,name,players):
        self.name = name
        self.players = players
        print(self.name,self.players)
    
    def game_rules(self):
        print(f"one  team starts the game  and the all rules are monitored by a coach ")

game1 = game()
game2 = game()
game1.game_details("kho-kho","7")
game1.game_rules()
game2.game_details("chess","4")

# use of self ------
#  self is used as an object everytime an object is created
# it is one of the in-build proprties of python
# always pass self even with no parameters in the methods...
# an empty class must have pass to avoid errors

class Nothing:
    pass #without pass this will  throw an error 

#----------------------without   _init_()     ---------------------------------------------------
class Persons:
  def person_Details(self, name, age=18):
    self.name = name
    self.age = age

p1 = Persons()
p1.person_Details("Emil", 30)

print(p1)  # gives memory location
print(p1.name)
print(p1.age)

#_init_() -> this is the fun. which is always called to initiate the class everytime an obj. is created
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)