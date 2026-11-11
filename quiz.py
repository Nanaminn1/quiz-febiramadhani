print("----------------------------------")
print(" PROGRAM REMEDIAL NILAI MAHASISWA")
print("----------------------------------")

# input nama mahasiswa
nama = input("Masukkan nama mahasiswa: ")

# menentukan target nilai
if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Nama mahasiswa tidak terdaftar!")
    exit()

print("Nama Mahasiswa :", nama)
print("Target Nilai   :", target)

# proses ujian
percobaan = 1
lulus = False

while percobaan <= 3:
    nilai = int(input(f"Masukkan nilai ujian ke-{percobaan}: "))

    if nilai >= target:
        lulus = True
        print("Selamat!", nama, "berhasil lulus!")
        print("Nilai:", nilai)
        break
    else:
        print("Nilai belum mencapai target.")

        if percobaan < 3:
            print("Silakan mengikuti remedial.")
        else:
            print("Kesempatan ujian telah habis.")

    percobaan += 1

# menampilkan hasil akhir
print("---------- HASIL AKHIR ----------")

if lulus:
    print(nama, "DINYATAKAN LULUS!")
else:
    print(nama, "DINYATAKAN TIDAK LULUS!")

print("---------------------------------")
