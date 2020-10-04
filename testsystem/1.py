path = str(input("pls input path to the test file - "))

balls  = 0

with open(path, "r") as file:
    ##lng = int(file.readline(1))
    qna = file.readlines()

    for i in range(0, len(qna), 2):

        print(qna[i])
        ra = str(qna[i+1])
        print(ra)
        print(ra)
        ua = str(input("answer - "))

        if ra == ua:
            print("Right")
            balls += 1
        else:
            print("Wrong")

print("Scored", balls, "out of ", int(len(qna) / 2))