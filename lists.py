friends = ["Kevin", "Karen", "Jim"]
print(friends)
print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[-2])
print(friends[1:])

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends[1:3])

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"
print(friends[1])

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed")
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Jim")
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends.index("Kevin"))

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends.index("Oscar"))

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends)

lucky_numbers = [42, 8, 15, 16, 23, 23]
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers = [42, 8, 15, 16, 23, 23]
lucky_numbers.reverse()
print(lucky_numbers)

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()
print(friends2)

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends4 = friends.copy()
print(friends4)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends.index("Mike"))


