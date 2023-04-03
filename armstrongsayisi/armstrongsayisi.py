while True:
    try:
        sayi = int(input("Lütfen pozitif bir tam sayı giriniz: "))
        break
    except ValueError:
        print("Lütfen geçerli bir değer giriniz.")
n = len(str(sayi))
ilksayi = 0
ilksayi = sayi
toplam = 0
if sayi > 0:
    while sayi !=0:
        toplam += (sayi % 10)**n
        sayi //= 10
    if ilksayi == toplam:
        print(ilksayi,"bir Armstrong sayısıdır.")
    else:
        print(ilksayi,"bir Armstrong sayısı değildir.")
else:
    print("Lütfen geçerli bir değer giriniz.")
        
        
        
        
        
        
