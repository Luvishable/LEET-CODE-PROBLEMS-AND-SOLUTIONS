def operation(liste):

    x = 0
    n = len(liste)
    for i in range(n):
        if liste[i][1] == "+":
            x += 1
        else:
            x -= 1
    return x

#print(operation(["X++","++X","--X","X--","--X"]))

def operation2(liste):
    return liste.count("++X") + liste.count("X++") - liste.count("--X") - liste.count("X--")
#print(operation(["X++","++X","--X","X--","--X"]))