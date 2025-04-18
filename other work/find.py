
greeting = "hello World"
position1 = greeting.find("o")
position2 = greeting.find("orl")
position3 = greeting.find("d")
position4 = greeting.find("m")

print(position1,position2,position3,position4)
print(position4)

greeting = "hello World"
position1 = greeting.find("o")
position2 = greeting.rfind("o")
position3 = greeting.rfind("orl")
position4 = greeting.rfind("lro")

print(position1,position2,position3,position4)
