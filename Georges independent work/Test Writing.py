f = open("Test.txt", "a")
i = 0
while i <=20:
    i = i +1
    the = str(i) + "\n"
    f.write(the)
f.close()
f = open("Test.txt", "r")
for line in f:
    print(line)
f.close
