import random as rd

actions =[
    "gathered to celebrate ",
    " did a random dance "
    "mocked at someone ",
    "left asasp",
    " moved to ",
    "celebrated defeat",
]
places = [
    "nimrana to",
    "then arrived at location",
    "highways of delhi",
    " at the bank og Yamuna",
    " satyed at % star hotel",
    " left the palace"
]
subject = [
    "the PM modi",
    "a cat of ",
    "The two random boys",
    "A reputed trader of ",
    "shah liked ",
    "left  to be enter "
]

# start the headline generator
while True:
   subject = rd.choice(subject)
   actions = rd.choice(actions)
   places = rd.choice(places)

   headline = f"BREAKING NEWS {subject} {actions} {places}"

   print("\n" + headline)

   user = input("\n do you want another headline (yes/no)").strip().lower()

   if(user == "no"):
      break
      
  




# print("enter these credensials")
# value = 9
# for i in range(5):
#     s = input("any action which sounds funny")
#     actions.append(s)

# for i in range(5):
#     s = input("any places which are famous")
#     places.append(s)

# for i in range(5):
#     s = input("any subject you like ")
#     subject.append(s)

# print(subject,"\n", places ,"\n",actions,"\n")
# headline =[]
# str = "priti"
# str.format

# headline.append(rd.choice(subject) +" to " + rd.choice(actions)+  "   finally the   "+ rd.choice(places))
# # headline.append(rd.choice(actions))
# # headline.append(rd.choice(places))

# print(headline)