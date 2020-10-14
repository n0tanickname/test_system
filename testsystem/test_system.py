import linecache

print("ВАЖНО: Путь к файлу необходимо указывать включая название и расширение самого файла!!!")

path = str(input("pls input path to the test file - "))

balls = 0
ans = []

with open(path, "r") as file:
    length = file.readlines()
    for i in range(1, len(length), 3):
        print(linecache.getline(path, i))

        ans = list(linecache.getline(path, i+1))
        c = 1
        kans = []
        rans = ""
        an = ""
        for k in range(0, len(ans)):
            if ans[k].isspace():
                kans.append("{}. {}   ".format(c, an).rstrip(""))
                an = ""
                c += 1
            else:
                an += ans[k]

        for k in range(len(kans)):
            rans += kans[k].rstrip("''")
        print(rans)

        ua = str(input("answer - "))
        ra = linecache.getline(path, i+2).rstrip("\n")

        if str(ua) == str(ra):
            print("Right")
            balls += 1
        else:
            print("Wrong")

print("Scored {} out of {}".format(balls, len(length) // 3))

# C:\Users\n0tanickname\Desktop\test.txt
