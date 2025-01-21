#  program promosi penjualan dengan memberikan bonus Bracket TV setiap pembelian di atas Rp 1.500.000 

belanja = int(input("masukan nominal belanja :"))

if belanja > 1500000 and belanja < 5000000 :
    print("anda mendapatkan TV BRACKET!")
elif belanja > 5000000 :
    print("anda mendapatkan SOUND BAR!")
else :
    print("tidak mendapatkan bonus!")