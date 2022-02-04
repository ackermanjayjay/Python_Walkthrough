# Menggunakan Map

class Listku:
    elemet=0
    masukkanList=0

    def input(self):
      
       self.elemet=int(input("Masukkan element List nada anda: "))

    def iterasi(self):
        # Use Spaces
            self.masukkanList=list(map(int,input("\nMasukkan List anda: ").strip().split(' ')))[:self.elemet]

        # With Comma
        #  self.masukkanList=list(map(int,input("\nMasukkan List anda: ").strip().split(',')))[:self.elemet]
 

    def output(self):
            print("\n List anda: ",self.masukkanList)

Cetak=Listku()
Cetak.input()
Cetak.iterasi()
Cetak.output()
