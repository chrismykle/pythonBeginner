
lucky_numbers = [8, 16, 23, 4, 15, 42]
friends = ["Kevin", "Jim", "Helene", "Lars", "Ola", "Chris"]

print(friends[2])   # Index 2, position 3
print(friends[-1])  # With - you start from the back of the list
print(friends[2:])  # From index 2 and up
print(friends[1:3])  # From index 1 to 3

friends.append("Chris")         # Inserts the value at the end of the list
print(friends)
friends.sort()                  # Alphabetic order
print(lucky_numbers)
lucky_numbers.sort()
print(lucky_numbers)
print(friends)


friends.extend(lucky_numbers)   # Inserts the list lucky_numbers
friends.insert(2, "Julie")      # Insert with index, value
friends.remove("Jim")           # Removes the value given
friends.pop()                   # Removes last value in list
print("Search for Chris: INDEX " + str(friends.index("Chris")))   # Use to search a list for a value
print(friends.count("Chris"))   # Counts the number of indexes with this value
print(friends)
friends.clear()                 # Removes all values in the list
print(friends)
