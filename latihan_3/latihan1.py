# program menghitung nilai akhir

print("PROGRAM MENGHITUNG NILAI AKHIR")

UTS = float(input("masukan nilai UTS :"))
UAS = float(input("masukan niali UAS :"))
TUGAS = float(input("masukan nilai tugas :"))

nilai_akhir = (0.3 + UTS) + (0.5 * UAS) + (0.2 * TUGAS)

print("nilai akhir",nilai_akhir)