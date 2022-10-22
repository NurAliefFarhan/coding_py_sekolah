menu = {
    "Fried Chicken" : 15000, 
    "Burger Queen" : 2500, 
    "French Fries" : 10000, 
    "Jasmine Tea" : 5000, 
    "Ice Coca-Cola" : 12000
}
print("==================== Datar Menu ====================")
for i in menu: 
    print("Daftar Menu : ", i, "\t Harga : ", menu[i])
print("Pembelian diatas Rp100.000, - mendapatkan diskon 15%")
print("====================================================")
beli = input("Pilih Menu : ")
jumlah = int(input("Jumlah Pesanan : "))
bayar = jumlah * menu[beli] 

if bayar > 100000:
    diskon = bayar*15/100
    total = bayar - diskon
else: 
    total = bayar 

print("==================== Detail Menu ====================")
print("Menu yang dipesan : ", beli)
print("Jumlah yang dipesan : ", jumlah)
print("Total Biaya : ", bayar)
print("Total yang harus bibayar : ", total)


