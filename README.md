[README.md](https://github.com/user-attachments/files/21780550/README.md)


Bu proje, **Python** ve **SQLite** kullanarak öğrenci bilgilerini (ad, soyad, numara, not) yönetebileceğiniz basit bir veritabanı uygulamasıdır.

 Özellikler
- Öğrenci ekleme
- Öğrenci listesini görüntüleme
- Öğrenci silme
- Öğrencinin notunu güncelleme
- Verilerin **SQLite** veritabanında kalıcı olarak saklanması

 Kullanılan Teknolojiler
- Python 3
- SQLite3

Dosya Yapısı
```
   ogrenci-not-sistemi
 ogrenci_not_sistemi.py  
 README.md                
  .gitignore               
```

 Kullanım Örneği
```python
veritabani = VeriTabaniBaglantisi("ogrenci_sistemi.db", "ogrenci")
veritabani.ogrenciEkleme("Ali", "Kaya", 80)
veritabani.ogrenciEkleme("Ayşe", "Demir", 90)
Ogrenci.listeyiYazdir()
veritabani.notGuncelle(2, 95)
Ogrenci.listeyiYazdir()
```


