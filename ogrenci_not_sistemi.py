import sqlite3

class Ogrenci:
    ogrenciList = []

    def __init__(self, isim, soyisim, no, puan):
        self.isim = isim
        self.soyisim = soyisim
        self.no = no
        self.puan = puan

    @classmethod
    def ogrenciEkle(cls, isim, soyisim, no, puan):
        yeniOgrenci = Ogrenci(isim, soyisim, no, puan)
        cls.ogrenciList.append(yeniOgrenci)

    @classmethod
    def listeyiYazdir(cls):
        for ogrenci in cls.ogrenciList:
            print(f"Öğrenci Adı: {ogrenci.isim}, "
                  f"Soyadı: {ogrenci.soyisim}, "
                  f"No: {ogrenci.no}, "
                  f"Puan: {ogrenci.puan}")


class VeriTabaniBaglantisi:
    def __init__(self, veritabani_isim, tablo_isim):
        self.veritabani = sqlite3.connect(veritabani_isim)
        self.imlec = self.veritabani.cursor()
        self.tablo = tablo_isim

        self.imlec.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.tablo} (
                ogrenciAdi NVARCHAR(20),
                ogrenciSoyadi NVARCHAR(20),
                no INTEGER PRIMARY KEY AUTOINCREMENT,
                puan INTEGER
            )
        """)

    def ogrenciGetir(self):
        sorgu = f"SELECT * FROM {self.tablo}"
        self.imlec.execute(sorgu)
        Ogrenci.ogrenciList.clear()

        for ogr in self.imlec.fetchall():
            Ogrenci.ogrenciEkle(ogr[0], ogr[1], ogr[2], ogr[3])

    def ogrenciEkleme(self, isim, soyisim, puan):
        sorgu = f"INSERT INTO {self.tablo} (ogrenciAdi, ogrenciSoyadi, puan) VALUES (?,?,?)"
        self.imlec.execute(sorgu, (isim, soyisim, puan))
        self.veritabani.commit()
        self.ogrenciGetir()

    def ogrenciSil(self, no):
        sorgu = f"DELETE FROM {self.tablo} WHERE no=?"
        self.imlec.execute(sorgu, (no,))
        self.veritabani.commit()
        self.ogrenciGetir()

    def notGuncelle(self, no, yeniNot):
        sorgu = f"UPDATE {self.tablo} SET puan=? WHERE no=?"
        self.imlec.execute(sorgu, (yeniNot, no))
        self.veritabani.commit()
        self.ogrenciGetir()


if __name__ == "__main__":
    veritabani = VeriTabaniBaglantisi("ogrenci_sistemi.db", "ogrenci")

    veritabani.ogrenciEkleme("Ali", "Kaya", 80)
    veritabani.ogrenciEkleme("Ayşe", "Demir", 90)
    veritabani.ogrenciEkleme("Mehmet", "Yılmaz", 70)

    Ogrenci.listeyiYazdir()

    veritabani.notGuncelle(2, 95)
    Ogrenci.listeyiYazdir()

 
    veritabani.ogrenciSil(1)
    Ogrenci.listeyiYazdir()
