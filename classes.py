class Cat:
   """model of a cat"""

   def __init__(self, name, age):
      self.name = name
      self.age = age

   def sit(self):
      print(f"{self.name.title()} is now sitting.")

   def hiss(self):
      print(f"{self.name.title()} just hissed.")

my_cat = Cat('cookie', 2)

print(f"my cats name is {my_cat.name.title()}.")
print(f"My cat is {my_cat.age} years old.")
my_cat.hiss()
my_cat.sit()

cute_cat = Cat('teddy', 2)

print(f"\n{cute_cat.name} Is a dude cat.")
print(f"He is {cute_cat.age}.")
cute_cat.sit()
