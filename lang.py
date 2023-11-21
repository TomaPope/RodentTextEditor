import random
text = "#####"
Uni = 1
textlist = [*text]
num = 0
newline = ""



while True:
    random.seed(Uni)
    while num < len(textlist):
        if textlist[num] == "#":
            newline += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        elif textlist[num] == "$":
            newline += random.choice('1234567890')
        else:
            newline += " "
        num += 1
        # if newline[0] != "H":
            # break
    Uni += 1
    num = 0
    if newline == "WORLD":
        print("Universe: ", Uni)
        print(newline)
        break
    newline = ""