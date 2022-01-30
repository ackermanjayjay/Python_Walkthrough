class Perpustakaan:
    manga_pinjam=5500
    manga_harga=60000
    cerita_pinjam=5000
    cerita_harga=50000

    durasi=0
    pinjam=0
    totalPinjam=0
    nama=""
    bayar=0

    def Keterangan(self):
        print("Selamat Datang di perpustakaan Ackerman")
        print("Buku Cerita Harga Rp 50.000")
        print("Manga Rp 60.000")
        print("Minjam Buku cerita Rp 5.000/hari")
        print("Minjam Manga Rp 5.500/hari")
        print("Jika kehilangan buku maka = hari lama pinjam * harga buku")
        print("\n")

    def inputNama(self):
        self.nama=input("Masukkan nama Anda: ")
        pilihan=input("Anda ingin pinjam Buku ? Y or N: ")
        if pilihan=="Y"or pilihan=="y":
         print("Anda Memilih pinjam buku")
         self.pinjam=int(input("Anda Ingin pinjam berapa :"))

    def bayar(self):
        self.totalPinjam=self.pinjam*self.cerita_pinjam
        print("\n")
        self.bayar=int(input("Bayar: "))
        if self.bayar==self.totalPinjam:
            print("Anda membayar sebesar Rp",self.bayar)
            print(" Pembayaran anda lunas")
        elif self.bayar<self.totalPinjam:
            print("Anda kurang bayar sebesar: Rp",self.totalPinjam-self.bayar)
        elif self.bayar>self.totalPinjam:
            print("Anda mendapat Kembali",self.bayar-self.totalPinjam)        

    def output(self):
        print("Nama anda: ",self.nama)
        print("Anda meminjam Buku Cerita selama: ",self.pinjam," Hari")
        print("Total anda Membayar sebesar: Rp",self.totalPinjam)
        


Cetak=Perpustakaan()
Cetak.Keterangan()
Cetak.inputNama()
Cetak.bayar()
Cetak.output()