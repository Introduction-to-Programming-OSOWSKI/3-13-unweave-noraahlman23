def unweave(w):
    newword1 = " "
    newword2 = " "
    for i in range (0, len(w), 2):
        newword1 = newword1 + w[i]

    for i in range (1, len(w), 2):
        newword2 = newword2 + w[i]
    return newword1 + " " + newword2
print (unweave("potato"))