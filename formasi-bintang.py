print("soal nomer 1 ")
rows = 5
for i in range(rows * 2):
    print("*", end= " ")
print()
for i in range(rows):
    for j in range(rows - i):
        print("*", end= " ")
    for j in range(i * 2):
        print(" ", end= " ")
    for j in range(rows - i):
        print("*", end= " ")
    print()


print("soal nomer 2 :")
rows = 6
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()


print("soal nmr 3 ")
rows = 3
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end= " ")
    print()
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end= " ")
    print()



print("soal nomer 4 ")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    for j in range((rows - i) * 2):
        print(" ", end=" ")
    for i in range(i):
        print("*", end=" ")
    print()



print("soal nomer 5 :")
rows = 5
for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()


print("soal nomer 6 :")
rows = 3
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    print()
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()



print("soal nomer 7 :")
for i in range(rows, 0, -1):
    for j in range(rows, - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
for i in range(2, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()


print("soal nomer 8 :")
rows = 9
for i in range(rows):
    print("0", end=" ")
    for j in range(rows):
        print("*", end=" ")
    print()
for i in range(rows + 1):
    print("0", end=" ")
print()



print("soal nomer 9 :")
blocks = 5
for i in range(blocks):
    print("*" * 10)
    print("0")
print("0" * 10)
print("0")



print("soal nomer 10 :")
rows = 5
for i in range(rows, 1, -1):
    for k in range(i):
        print("*", end=" ")
    print()
for i in range(1, rows + 1):
    for k in range(i):
        print("*", end=" ")
    print()



print("soal nomer 11 :")
rows = 5
cols = 10
print("0" * (cols + 1))
for i in range(rows):
    print("0" + "*" * cols)


print("soal nomer 12 :")
rows = 5
cols = 10
print("0" * 10)
print("0")
for i in range(rows):
    print("*" * cols)
    print("0")


print("soal nomer 13 :")
rows = 6
cols = 7
for i in range(rows):
    zeros = i + 1
    stars = cols - zeros 
    print("0" * zeros + "*" * stars)


print("soal nomer 14 :")
rows = 5
cols = 7
for i in range(1, rows + 1):
    stars = i + 1
    zeros = cols - stars
    print("*" * stars + "0" * zeros)


print("soal nomer 15 :")
rows = 6
cols = 7
for i in range(1, rows + 1):
    stars = i
    zeros = cols - stars
    print("0" * zeros + "*" * stars)


print("soal nomer 16 :")
rows = 6
cols = 7
for i in range(1, rows + 1):
    stars = i
    zeros = cols - stars
    print("0" * zeros + "*" * stars)


print("soal nomer 17 :")
rows = 6
cols = 7
for i in range(rows):
    line = ""
    for j in range(cols):
        if j == cols - 1 - i:
            line += "*"
        else:
            line += "0"
    print(line)


print("soal nomer 18 :")
rows = 6
cols = 7
for i in range(rows):
    line = ""
    for j in range(cols):
        if j == i:
            line += "*"
        else:
            line += "0"
    print(line)



print("soal nomer 19 :")
rows = 6
cols = 7
for i in range(rows):
    if i == 0 or i == rows -1:
        print("0" * cols)
    else:
        print("0" + "*" * (cols - 2) + "0")



print("soal nomer 20 :")
cols = 6
blocks = 2
for i in range(blocks):
    print("0" * cols)
    print("*" * cols)
    print("*" * cols)
    

