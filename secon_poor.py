num=int(input())
lista_Cal=[]
for i in range(num):
    nombre=input()
    Calificacion=float(input())
    lista=[Calificacion,nombre]
    lista_Cal.append(lista)
lista_Cal.sort()
while(True):
     n=0
     if lista_Cal[n][0]!=lista_Cal[n+1][0]:
         if lista_Cal[n+1][0]==lista_Cal[n+2][0]:
             print("{}".format(lista_Cal[n+1][1]))
             print("{}".format(lista_Cal[n+2][1]))
             break
         else:
            print("{}".format(lista_Cal[n+1][1]))
            break
     elif lista_Cal[n][0]==lista_Cal[n+1][0]:
        n=n+1
        break
""""
//////////////
///////////////
///////////////"""

    if __name__ == '__main__':
    l=[]
lista=[]
for i in range(int(input())):
    nombre=input()
    score=float(input())
    l.append([score,nombre])
    l.sort()
h=1
if l[0][0]==l[h][0]:
    h=h+1
    if l[1][0]<l[h][0]:
            print(l[h][1])
    if l[1][0]==l[h][0]:
            print("{},{}".format(l[1][1],l[2][1]))
elif l[1][0]<l[2][0]:
    print(l[h][1])
elif l[1][0]==l[h][0]:
    print("{}\n{}".format(l[1][1],l[2][1]))
