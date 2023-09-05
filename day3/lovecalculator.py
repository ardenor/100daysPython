name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

combined = name1 + name2

lowered = combined.lower()

t = lowered.count("t")
r = lowered.count("r")
u = lowered.count("u")
e = lowered.count("e")

true = t + r + u + e

l = lowered.count("l")
o = lowered.count("o")
v = lowered.count("v")
e = lowered.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))



if love_score < 10 or love_score > 90:
    print(f"{love_score}, coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"{love_score}, alright")
else:
    print(f"{love_score}")