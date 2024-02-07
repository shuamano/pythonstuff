bikes = ['trek', 'schwinn', 'specialized', 'polygon']
print(bikes)
print(bikes[2])
#important to note: the list starts counting from zero. As in, the first item is zero, the second is one and so on
print(bikes[3].title())
#to get the last item in a list, just put -1 in the brackets: 
print(bikes[-1])
message = f"my First bike was a {bikes[1].title()}."
print(message)
#updating a value in the list like this
bikes[0] = 'oogabooga'
print(bikes[0].title())
print(bikes)

#add a new element to the list like this:
bikes.append("marin")
print(bikes)

#insert a value like this:
bikes.insert(0, 'ducati?')
print(bikes)

#delete a value like this: 
del bikes[0]
print(bikes)

print( f" \n {bikes}\n")
#you can "pop" a value from the top of the list like this
pop_bike = bikes.pop()

print(bikes)
print(pop_bike)