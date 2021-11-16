print("\n    ====Caffe GoodDay====")

pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

total1=0
jenis1=""
porsi=0
gelas=0

def Daftar_barang():
   global total1
   global porsi
   global jenis1
   print ("\n========Menu Makanan=============")       
   print("1. Burger King         : Rp25000")  
   print("2. Spaghetti deluxe    : Rp20000")
   print("3. Steak               : Rp50000")
   print("4. Seblak              : Rp12000")
   print("5. Ayam pedas          : Rp15000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       total1=porsi*25000
       print (porsi," Burger King = Rp", total1)
       jenis1=("Burger King")
   elif nomor==2:
       total1=porsi*20000
       print (porsi," Spaghetti deluxe = Rp", total1)
       jenis1=("Spaghetti deluxe")
   elif nomor==3:
       total1=porsi*50000
       print (porsi, " Steak = Rp", total1)
       jenis1=("Steak")
   elif nomor==4:
       total1=porsi*12000
       print (porsi, " Seblak = Rp", total1)
       jenis1=("Seblak")
   elif nomor==5:
       total1=porsi*15000
       print (porsi, " Ayam pedas = Rp", total1)
       jenis1=("Ayam pedas")
   else:
      print("Pilihan tidak tersedia, silahkan coba lagi!!")
      Daftar_barang()


Daftar_barang()

total2=0
jenis2=""

def fungsiminuman():
   global total2
   global jenis2
   global gelas
   print("\n========Menu Minuman========")
   print("1. HOT/ICE Ameericano   : Rp20000")
   print("2. HOT/ICE Latte        : Rp15000")
   print("3. HOT/ICE Matcha       : Rp15000")
   print("4. HOT/ICE Tea          : Rp8000")
   print("5. HOT/ICE Milk         : Rp10000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       total2=gelas*20000
       print (gelas," HOT/ICE Ameericano  = Rp", total2)
       jenis2=(" HOT/ICE Ameericano ")
   elif nomor==2:
       total2=gelas*15000
       print (gelas, " HOT/ICE Latte = Rp", total2)
       jenis2=(" HOT/ICE Latte")
   elif nomor==3:
       total2=gelas*15000
       print (gelas, " HOT/ICE Matcha  = Rp", total2)
       jenis2=(" HOT/ICE Matcha ")
   elif nomor==4:
       total2=gelas*8000
       print (gelas, " HOT/ICE Tea = Rp", total2)
       jenis2=(" HOT/ICE Tea")
   elif nomor==5:
       total2=gelas*10000
       print (gelas, " HOT/ICE Milk = Rp", total2)
       jenis2=(" HOT/ICE Milk")
   else:
      print("Pilihan tidak tersedia, silahkan coba lagi!!")
      fungsiminuman()


fungsiminuman()
totalsemua=0
totalsemua=total1+total2
print("\nTotal yang harus dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("=========== T O T A L ============")
print("==================================")
print (" Nama          :",pembeli)
print (" Barang        :",porsi,jenis1,"Rp.", total1)
print ("                ",gelas,jenis2,"Rp.", total2)
print (" Total         : Rp.",totalsemua)
print (" Tunai         : Rp.",uang)
print (" Kembalian     : Rp.",kembalian)
print("=================================")
print("==Terima Kasih Telah Berkunjung==")
print("=================================")
