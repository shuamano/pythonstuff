names = ['Bob', 'jack', 'dude', 'buffengi', 'clark', 'zebra']

names.sort()
print(names)
print("wow its in alphabetical order")
#this sorting is permanent and cant be undone.

#to sort it unpermanently:
print("original list:")
print(names)
print("\nsorted list:")
print(sorted(names))
print("\noriginal list:")
print(names)

#reverse the order
print("\nreversed:")
names.reverse()
print(names)

#find the length of a list
print(len(names))