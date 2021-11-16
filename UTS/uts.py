# lulus =input("Apakah Kamu lulus")
# if lulus == "Tidak":
#     print("kamu tidak lulus")

# elif lulus == "Iya":
#     print("Kamu Lulus")

print("\n======  Rental Mobil  =======")
print("Menyediakan Sewa Mobil Pribadi")

mobil = input("Silahkan Masukkan nama anda : ")
print("Nama Penyewa = ", mobil)



saja = "lanjut"
while(True) :
    nama = [" Toyota Alphard 1 ", " Avanza 2"  , "Pajero Sport 3", "Fortuner 4" , "Honda Civic 5" ]

    for list in nama:
        print("\n==== 1. ", nama[0],"====")
        print("\n==== 2. ", nama[1],"====")
        print("\n==== 3. ", nama[2],"====") 
        print("\n==== 4. ", nama[3],"====") 
        print("\n==== 5. ", nama[4],"====")   
        break

    sewa = int(input("Silahkan Pilih Mobil yang akan di sewa : "))
    lama = int(input("Berapa Hari : " ))

    
    if sewa == 1:
        biaya1= lama*80000000
        print("Biaya sewa Mobil 1 Rp : ",biaya1 )

    elif sewa == 2:
        biaya2 = lama*15000000
        print("Biaya Sewa Mobil 2 Rp : ", biaya2)

    elif sewa == 3:
        biaya3 = lama*23000000
        print("Biaya Sewa Mobil 3 Rp : ", biaya3)

    elif sewa == 4:
        biaya4 = lama*30000000
        print("Biaya Sewa Mobil 4 Rp : ", biaya4)

    elif sewa == 5:
        biaya5 = lama*45000000
        print("Biaya Sewa Mobil 5 Rp : ", biaya5)
    else:
        print('masukan pilihan yang benar')
        continue

    lagi = (input("Apakah anda ingin menyewa mobil type lainnya  ? "))
    if lagi == "y":
           continue
    else:
        print("\n=====Terima Kasih Telah Berkunjung=====")
        break

    