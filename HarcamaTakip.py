import datetime
tum_harcamalar = []
""" Datetime modülünün import edilmesi ve harcamaların saklanacağı liste """
class Harcama:
        """ Bir harcamanin gerekliliklerini bulunduran sınıf """
        def __init__(self,aciklama,tutar, tarih):
              self.aciklama = aciklama
              self.tutar = tutar
              self.tarih = tarih

def harcama_ekle():
      """ Kullanıcıdan veri alarak listeye yeni harcama ekler. """
      yeni_harcama = Harcama(aciklama , float(tutar) , tarih)
      tum_harcamalar.append(yeni_harcama)
def tutartoplami():
        """ Harcamaların toplam tutarını hesaplar. """
        toplamtutar= sum(h.tutar for h in tum_harcamalar)
        print(f'Toplam Harcama: {toplamtutar} TL')      
while True:
    print('''Aşağıdaki seçeneklerden birini seçiniz
1-Harcama Ekle
2-Harcamaları Listele
3-Harcamalar Toplamı
4-Programdan çık ''')
    giris = input("seçiminiz : ")
    if giris == "1":
        try:
            """ Hatalı girişleri yakalamak için try-except bloğu """
            aciklama = input('ne harcaması yaptınız? Gİriniz : ')
            if not aciklama: raise ValueError("Açıklama boş bırakılamaz!")
            tutar = float(input('ne kadar harcama yaptınız? Gİriniz : '))
            if tutar <= 0: raise ValueError("Tutar pozitif olmalı!")
            tarih = input('Ne zaman Harcama yaptınız? Boş: Bugün (GG-AA-YYYY):')
            if not tarih: tarih = datetime.date.today()
            else:tarih = datetime.datetime.strptime(tarih, "%d-%m-%Y").date()
            harcama_ekle()
            print("Harcama eklendi")
        except ValueError as e:
              print(f'Hatalı Giriş: {e}')    
    elif giris=="2":
         """ Harcamaları tutara göre büyükten küçüğe sıralayıp listeleme """
         i=1
         sirali_liste = sorted(tum_harcamalar, key=lambda x: x.tutar, reverse=True)
         for h in sirali_liste:
           mesaj = f'{i}. harcamanızın açıklaması: {h.aciklama} , tutarı: {h.tutar} TL , tarihi: {h.tarih.strftime("%d.%m.%Y")} günüdür'
           print(mesaj)
           i+=1
    elif giris=="3":
        """ Harcamaların toplam tutarını gösterme """
        tutartoplami()
    
    elif giris == "4":
         """ Çıkış işlemi """
         print("çıkış yapılıyor")
         break    
    
                    
    
