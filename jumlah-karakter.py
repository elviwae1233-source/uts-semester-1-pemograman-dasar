print("soal nomor 3 :")
raws = 3
for i in range(1, raws + 1):
    for j in range(i):
        print("*", end= " ")
    print()
for i in range(1, raws + 1):
    for j in range(raws - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end= " ")
    print() 
