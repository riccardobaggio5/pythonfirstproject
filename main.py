"""
 num1 = input ('enter number: ')
 # gets input as string#
 num2 = input ('enter number:)
 to convert the string into number I can use the convert function

 result = int(num1) + int(num2)
 print(result)

 # but it's not a float number so:
 num1 = input(enter number)
 gets input as string#
 num2 = input('enter number: ')
 result = float(num1) + float(num2)
 print(result)


# MAD LIBS GAME, we put strings into a story randomly

color = input("Enter color: ")
plural = input("Enter plural: ")
name = input("Enter name: ")

print("roses are " + color)
print(plural + " are blue")
print("i love " + name)

# LISTS for large amount of data
# array of strings
friends = ["kevin", "karen", "jim", "oscar", "toby"]
print(friends)
print(friends[2])
print(friends[-1])
print(friends[2:4])

print(friends[1])
friends[1] = "mike"
print(friends[1])

# LIST FUNCTIONS

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["kevin", "karen", "jim", "oscar", "toby"]
print (friends)

# EXTEND: append another list to a list

# friends.extend(lucky_numbers)
# print(friends)

# APPEND: append one item to the end of the list

friends.append("bro")
print(friends)

# INSERT: append one item in the index

friends.insert(1, "kelly")
print(friends)

# REMOVE: remove an element

friends.remove("oscar")
print(friends)

# CLEAR: reset the list

# friends.clear()
# print(friends)

# POP: pop an itme off the list, from the index if stated, if not pops the last

friends.pop()
print(friends)

# INDEX: returns the index of an element if present. Returns error if not present
print(friends.index("kevin"))


# COUNT: counts elements of that type in list
friends.insert(4, "oscar")
friends.insert(4, "oscar")
friends.insert(4, "oscar")
print(friends)
print(friends.count("oscar"))

# SORT: in ascending order
friends.insert(4, "aaron")
friends.sort()
print(friends)

# REVERSE

lucky_numbers.reverse()
print(lucky_numbers)

# COPY STRINGS

friends2 = friends.copy()
print(friends2)


# TUPLES: type of data structure, container, similar to a list

# coordinates = (4, 5)
# tuple is immutable: can't be change or modified
# print(coordinates[1])

# we can create a coordinate list
# though the values can't be modified, it's a special use case niche
coordinates = [(4, 5), (6, 7), (80, 34)]
"""


# FUNCTIONS!!!!

def say_hi():
    print("Hello!")


def say_hi_second(name):
    print("Hello " + name)


def say_hi_third(name, age):
    print("Hello " + name)
    print("You are " + str(age))


def say_hi_fourth(name, age):
    print("Hello " + name)
    print("You are " + str(age))


say_hi_fourth("Mike", 3)
say_hi_fourth("Steve", 55)
