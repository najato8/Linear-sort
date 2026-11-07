def sort(T):
    
    #trouver le max du tableau
    max = T[0]
    for i in range(1,len(T)):
        if T[i] > max:
            max = T[i]

    #tableau d'apparitions vide
    apparitions = [0]*(max + 1)

    #construction du tableau d'apparition
    for k in range(len(apparitions)):
        c = 0
        for j in range(len(T)):
            if k == T[j]:
                c = c + 1

        apparitions[k] = c

    return apparitions

   

T = [7,1,3,1,2,4,1,5,2,4,3]

print(sort(T))