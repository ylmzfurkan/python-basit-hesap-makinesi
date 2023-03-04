# İşlem türlerini gösteren bir menü oluşturalım
print("Lütfen yapmak istediğiniz işlem türünü seçin:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

# Kullanıcıdan işlem türü, sayı1 ve sayı2'yi alalım
secim = input("Seçiminiz (1/2/3/4): ")
sayi1 = int(input("İlk sayı: "))
sayi2 = int(input("İkinci sayı: "))

# İşlem türüne göre sonucu hesaplayalım ve ekrana yazdıralım
if secim == '1':
    print(sayi1, "+", sayi2, "=", sayi1 + sayi2)
elif secim == '2':
    print(sayi1, "-", sayi2, "=", sayi1 - sayi2)
elif secim == '3':
    print(sayi1, "*", sayi2, "=", sayi1 * sayi2)
elif secim == '4':
    print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
else:
    print("Geçersiz seçim")
