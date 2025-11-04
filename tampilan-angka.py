soa14 = ""
for i in range(1, 7):
    soa14 += str(i) * i
print("soal nomor 4 :" + soa14)

soa15 = ""
for p in range(6, 0, -1):
    soa15 += str(p) * p
print("soal nomor 5 :" + soa15)

soa16 = ""
for a in range(1, 7):
    for b in range(1, a + 1):
        soa16 += str(b)
print("soal nomor 6 :" + soa16)

soa17 = ""
for a in range(6, 0, -1):
    for b in range(a, 0, -1):
        soa17 += str(b)
print("soal nomor 7 :" + soa17)


soa18 = ""
soa18 += "1" * 2
soa18 += "2"
soa18 += "3" * 3
for i in range(1, 5):
    soa18 += str(i)
soa18 += "5" * 5
for i in range(1, 7):
    soa18 += str(i)
print("soal nomor 8 :" + soa18)


soa19 = ""
soa19 += "1"
soa19 += "2" * 2
soa19 += "123"
soa19 += "4" * 4
for i in range(1, 6):
    soa19 += str(i)
soa19 += "6" * 6
print("soal nomor 9 :" + soa19)


soa110 = ""
for i in range(6, 0, -1):
    soa110 += str(i)
soa110 += "5" * 4
for i in range(5, 0, -1):
    soa110 += str(i)
soa110 += "3" * 2
for i in range(3, 0, -1):
    soa110 += str(i)
soa110 += "1"
print("soal nomor 10 :" + soa110)


soa111 = ""
soa111 += "6" * 6
for i in range(1, 6):
    soa111 += str(i)
soa111 += "4" * 4
for i in range(1, 4):
    soa111 += str(i)
soa111 += "221"
print("soal nomor 11 :" + soa111)


soa112 = ""
for i in range(1, 3):
    soa112 += str(i)
soa112 += "2"
for i in range(1, 4):
    soa112 += str(i)
for i in range(1, 5):
    soa112 += str(i)
for i in range(5, 7):
    soa112 += str(i) * i
for i in range(1, 8):
    soa112 += str(i)
for i in range(1, 9):
    soa112 += str(i)
soa112 += "9" * 9
print("soal nomor 12 :" + soa112)


soa113 = ""
soa113 += "1"
for b in range(1, 3):
    soa113 += str(b)
for b in range(3, 5):
    soa113 += str(b) * b
for b in range(1, 6):
    soa113 += str(b)
for b in range(1, 7):
    soa113 += str(b)
for b in range(7, 9):
    soa113 += str(b) * b
for b in range(1, 10):
    soa113 += str(b)
print("soal nomor 13 :" + soa113)


soa114 = ""
for k in range(8, 6, -1):
    soa114 += str(k) * k
for k in range(6, 0, -1):
    soa114 += str(k)
for k in range(5, 0, -1):
    soa114 += str(k)
for k in range(4, 2):
    soa114 += str(k) * k
for k in range(2, 0, -1):
    soa114 += str(k)
soa114 += "1"
print("soal nomor 14 :" + soa114)


soa115 = ""
for g in range(8, 0, -1):
    soa115 += str(g)
for g in range(7, 0, -1):
    soa115 += str(g)
for g in range(6, 4, -1):
    soa115 += str(g) * g
for g in range(4, 0, -1):
    soa115 += str(g)
for g in range(3, 0, -1):
    soa115 += str(g)
for g in range(2, 0, -1):
    soa115 += str(g) * g
print("soal nomor 15 :" + soa115)


soa116 = ""
n = 1
terms = 12
for i in range(terms):
    soa116 += str(n)
    if i < terms - 1:
        soa116 += " "
    if i % 2 == 0:
        n += 4
    else:
        n -= 2
print("soal nomor 16 :" + soa116)


soal17=""
n = 2
for i in range(10):
    soal17 += str(n) + " "
    if i % 2 ==0:
        n += 10
    else:
        n -=5    
print("soal nomer 17 :"+soal17)

soa18= ""
n = 5
for i in range(12):
    soa18 += str(n) + " "
    if i % 2 == 0:
        n -= 3
    else:
        n += 5
print("soal nomer 18 :" + soa18)


soal19 = ""
n = 3
for i in range(10):
    soal19 += str(n) + " "
    if i % 2 == 0:
        n *= 3
    else:
        n -= 5
print("soal nomer 19 :" + soal19)


soal20 = ""
n = 1
increments = [1, 2, 3]
for i in range(13):
    soal20 += str(n) + " "
    n *= 2
print("soal nomer 20 :"+soal20)


soa121 = ""
n = 1
for i in range(10):
    soa121 += str(n) + " "
    n *= 2
print("soal nomor 21 :" + soa121)


soa122 = ""
n = 3
faktorial = 1
soa122 = str(n) + "! = "
for i in range(n, 0, -1):
    soa122 += str(i) + " "
    if i > 1:
        soa122 += " x "
    faktorial *= i
soa122 += " = " + str(faktorial)
print("soal nomor 22 :" + soa122)


soal23 = ""
maks = 45
a, b = 0, 1
soal23 += str(a) + " " + str(b) + " "
while True:
    c = a + b
    if c > maks:
        break
    soal23 += str(c) + ","
    a, b = b, c
print("soal nomer 23 :"+soal23)


soal24 = ""
n_awal = 10
n_akhir = 35
for i in range(n_awal, n_akhir + 1):
    if i % 3 == 0:
        soal24 += str(i) + " "
print("soal nomer 24 :"+soal24)


soal25 = ""
n_awal = 10
n_akhir = 40
for i in range(n_awal, n_akhir + 1):
    if i % 4 == 0:
        soal25 += str(i) + " "
print("soal nomer 25 :"+soal25)


soal26 = ""
n_awal = 1
n_akhir = 10
jumlah_bulat_positif = 0
for i in range(n_awal, n_akhir + 1):
    if i > 0:
        jumlah_bulat_positif += 1
        soal26 += str(i) + " "
print("soal nomer 26 :"+soal26)
print("soal bilangan bulat positif dari",n_awal, n_akhir)


soal27 = ""
awal = 1
n_akhir = 20
total_genap = 0
for i in range(n_awal,n_akhir + 1):
    if i % 2 == 0:
        total_genap += i
        soal27 += str(i) + " "
print("soal nomer 27 :"+ soal27)


soal28 = ""
awal = 1
n_akhir = 20
total_genap = 0
for i in range(n_awal,n_akhir + 1):
    if i % 2 ==0:
        total_genap += i
        soal28 += str(i) + " "
print("soal nomer 28 :"+ soal28)
print("total bilangan ganjil dari", n_awal, "hingga", n_akhir,"adalah, jumlah_ganjil")


soal29 = ""
n_awal = 10
n_akhir = 30
prima_list = []
for n in range(n_awal, n_akhir, +1):
    if n > 1:
        for i in range( 2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            prima_list.append(n)
print("soal nomer 29 : bilangan prima adalah =", end = " ")
for p in prima_list:
    print(f"{p}", end = " ")
print()


soal30 = ""
n_awal = 10
n_akhir = 30
prima_list = []
for j in range(n_awal, n_akhir, +1):
    if j > 1:
        for i in range(2, int(j**0.5) +1):
            if j % i == 0:
                break
            else:
                prima_list.append(j)
print("soal nomer 30 :")
print("bilangan prima", ' '.join(str(p)for p in prima_list))
print("jumlah total bilagan prima :", len(prima_list))

