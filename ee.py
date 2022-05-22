"""class kayit():
    def __init__(self,isim,kayitYas,kayitCinsiyet,kayitKilo,kayitBoy):
        self.isim = isim
        self.kayitYas = kayitYas 
        self.kayitCinsiyet = kayitCinsiyet
        self.kayitKilo = kayitKilo
        self.kayitBoy = kayitBoy
    def endeks(self):
        endeks = 0
        endeks = (self.kayitKilo)/(self.kayitBoy)^2
        return endeks

        
        
def kayit():
    kayit_ad_soyad_split = input("Ad Soyad : ")
    kayit_ad_soyad = kayit_ad_soyad_split.split(" ")
    kayit_yas = int(input("Yaş : "))
    kayit_cinsiyet = input("Cinsiyet : ")
    kayit_kilo = int(input("Kilo : "))
    kayit_boy = int(input("Boy : "))"""
    

def menu():  #fonksiyon
    func_hesap = 0 
    while (True):
        print("Bu alışverişten ödenecek tutar = {} \n".format(func_hesap))
        alisveris_secim = input("""
                                    1. Porsiyon protein---15 TL
                                    2. Küçük Su(0.5 LT)---2.5 TL
                                    3. Büyük Su(1.0 LT)---5 TL
                                    4. Bitki Çayları---15 TL
                                    5. BİTİR
                                    """)          
        try:
            alisveris_secim = int(alisveris_secim)
            if alisveris_secim > 5:
                print("Girilen değer 5'ten büyük olamaz!! \n")
            elif alisveris_secim < 1:
                print("Girilen değer 1'den küçük olamaz!! \n")
        except:
            print("Sizden istenilen değerde bir değer giriniz. \n")                                     
        if (alisveris_secim == 1):
                                                        func_hesap = func_hesap + 15
                                                        alinan = "Porsiyon protein"           
        elif (alisveris_secim == 2):
                                                        func_hesap = func_hesap + 2.5 
                                                        alinan = "Küçük Su"
        elif (alisveris_secim == 3):
                                                        func_hesap = func_hesap + 5
                                                        alinan = "Büyük Su"
        elif (alisveris_secim == 4):
                                                        func_hesap = func_hesap + 15
                                                        alinan = "Bitki Çayı"
        elif (alisveris_secim == 5):
                        return func_hesap

def cikis():
        cikis_saati = input("Çıkış yaptığınız saati giriniz : ")
        musteri.append(hesap0)
        musteri.append(cinsiyet)
        musteri.append(giris_saati)
        musteri.append(cikis_saati)
        gun_sonu_musteriler[ad_soyad] = musteri
        im.execute("""INSERT INTO islemlerr(AD_SOYAD,CİNSİYET,GİRİŞ_SAATİ,ÇIKIŞ_SAATİ,HARCAMA)VALUES (?,?,?,?,?)""", (ad_soyad,cinsiyet,giris_saati,cikis_saati,hesap0))
        vt.commit()
        
print("----------GREENN GYM TURNİKE SİSTEMİ----------")

import sqlite3
vt = sqlite3.connect('database.db')
im = vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS 'islemlerr' (AD_SOYAD CHAR,CİNSİYET CHAR,GİRİŞ_SAATİ NUMERIC,ÇIKIŞ_SAATİ NUMERIC,HARCAMA REAL)")
vt.commit()

Loop = 1
loop3 = 1
musteri = []
gun_sonu_musteriler = {}   #sözlük
cinsiyet = ""
"""while(True):
    kayitLoop = input("Kayıt varsa 'e' yoksa 'h' tuşlayınız.")
    if (kayitLoop) == 'e':
       kayit = kayit()
        
    elif (kayitLoop) == 'h':
       break"""
while(Loop == 1):
    hesap0=0
    musteri = []
    cinsiyet = ""
    alinan = ""
    while(True): 
     giris_saati = input("Giriş saatinizi yazınız (Örn. 16.00) \n")
     try:
         giris_saati = float(giris_saati)
         break
     except:
         print("Lütfen düzgün giriş yapınız. \n")
         pass
    ad_soyad = input("Adınızı ve Soyadınızı arada boşluk olacak şekilde giriniz : ")
    while(True):               
         cinsiyet_input = input("Cinsiyetiniz nedir (Erkek ise 'e' Kadın ise 'k') : ")
         try:
             if cinsiyet_input == "e":
                 break
             elif cinsiyet_input =="k":
                 break
             else:
                 print("Geçerli giriş yapınız. \n")
                 continue
         except:
                pass    
    ad_soyad_list = ad_soyad.split(" ")
    if (cinsiyet_input == 'e'):
        print("Hoşgeldiniz {} Bey \n".format(ad_soyad_list[0]))
        cinsiyet = "Erkek"
    elif (cinsiyet_input == 'k'):
        print("Hoşgeldiniz {} Hanım \n".format(ad_soyad_list[0]))
        cinsiyet = "Kadın"
    loop3 = 1
    while(loop3 == 1):    
     alisveris = 1        
     while(alisveris == 1):
                while(True):
                    secim = input("Bir şeyler satın almak isterseniz 'e' istemezseniz 'h' ile devam ediniz. \n")
                    try:
                        if secim == "e":
                            break
                        elif secim =="h":
                            break
                        else:
                            print("Geçerli giriş yapınız. \n")
                            continue
                    except:
                                print("Geçerli giriş yapınız. \n")
                                pass                        
                if (secim == 'e'):
                    hesap1 = menu()
                    hesap0 += hesap1
                    
                    break
                elif (secim == 'h'):
                             alisveris = 2
                             loop3 = 2
     while(True):               
         cikis_kontrol = input("Çıkış yapmak istiyorsanız 'e' yazınız. Yapmak istemiyorsanız 'h' yazınız. \n")
         try:
             if cikis_kontrol == "e":
                 break
             elif cikis_kontrol =="h":
                 break             
             else:
                 print("Geçerli giriş yapınız. \n")
                 continue
         except:
                print("Geçerli giriş yapınız. \n")
                pass
     if (cikis_kontrol == 'e'):
         cikis()
         loop3 = 2
     else: 
        loop3 = 1
    gunsonu = input("Gün sonu ise 'e' yazınız. Değilse herhangi bir şey tuşlayınız \n")
    if (gunsonu == 'e'):
           print(gun_sonu_musteriler)
           break    