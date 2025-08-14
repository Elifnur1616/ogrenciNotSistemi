[README.md](https://github.com/user-attachments/files/21780550/README.md)
# Öğrenci Not Sistemi

Bu proje, **Python** ve **SQLite** kullanarak öğrenci bilgilerini (ad, soyad, numara, not) yönetebileceğiniz basit bir veritabanı uygulamasıdır.

## 📌 Özellikler
- Öğrenci ekleme
- Öğrenci listesini görüntüleme
- Öğrenci silme
- Öğrencinin notunu güncelleme
- Verilerin **SQLite** veritabanında kalıcı olarak saklanması

## 🛠 Kullanılan Teknolojiler
- **Python 3**
- **SQLite3**

## 🚀 Kurulum ve Çalıştırma
1. Bu projeyi bilgisayarına klonla:
   ```bash
   git clone https://github.com/KULLANICI_ADIN/ogrenci-not-sistemi.git
   cd ogrenci-not-sistemi
   ```
2. Python dosyasını çalıştır:
   ```bash
   python ogrenci_not_sistemi.py
   ```

## 📂 Dosya Yapısı
```
📁 ogrenci-not-sistemi
 ├── ogrenci_not_sistemi.py   # Ana uygulama kodu
 ├── README.md                # Proje açıklaması
 └── .gitignore               # Gereksiz dosyaları hariç tutma
```

## 💡 Kullanım Örneği
```python
veritabani = VeriTabaniBaglantisi("ogrenci_sistemi.db", "ogrenci")
veritabani.ogrenciEkleme("Ali", "Kaya", 80)
veritabani.ogrenciEkleme("Ayşe", "Demir", 90)
Ogrenci.listeyiYazdir()
veritabani.notGuncelle(2, 95)
Ogrenci.listeyiYazdir()
```

## 📜 Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakabilirsiniz.
