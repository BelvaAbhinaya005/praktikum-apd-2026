barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000

barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]
total_belanjaan = (barang[0] + barang[1] + barang[2] + barang[3] + barang[4] + barang[5])
pajak = total_belanjaan * 0.15
total_bayar = total_belanjaan + pajak
total_usd = total_bayar / 17726
total_yen = total_bayar / 113
rata_rata = total_bayar / len(barang)
nim = 27
bolean = nim < rata_rata

print(barang_1)
print(barang_2)
print(barang_3)
print(barang_4)
print(barang_5)
print(barang_6)
print(barang)
print(total_belanjaan) 
print(pajak)
print(total_bayar)
print(total_usd)
print(total_yen)
print(rata_rata)
print(nim)
print(bolean)
print(barang[0], barang[2], barang[4])