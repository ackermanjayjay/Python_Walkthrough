class Listku:
# Declarasi Input user List
    listku=[]
    elemet=0
    iterasiku=0
    ele=0
    def input(self):
      
        self.elemet=int(input("Masukkan element List nada anda: "))

    def iterasi(self):
    # Iterasi 
        for self.iterasiku in range (self.iterasiku,self.elemet):
            print("\nMasukkan list anda: ",self.iterasiku)
            self.ele=int(input())

# Perhatikan inteentikasi
            self.listku.append(self.ele)

    def output(self):
        print("\nList anda: ",self.listku)    

Cetak=Listku()
Cetak.input()
Cetak.iterasi()
Cetak.output()
