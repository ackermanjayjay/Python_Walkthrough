class calc:
    Matrix1=0
    Matrix2=0
    itasi=0
    baris=0
    hasil=[]
    hasil2=[]
    kolom=0
    def niceMeet(self):
        # Masukkan baris
        self.baris=int(input("Masukkan element baris: "))
        self.kolom=int(input("Masukkan kolom: "))

    def inptuMatrix1(self):
        # use map
        for self.itasi in range(self.baris):
            for self.itasi in range(self.kolom):
                    self.Matrix1=list(map(int,input("\nMasukkan Matrix 1: ").split()))
                    self.hasil.append(self.Matrix1)

    def inputMatrix2(self):
          for self.itasi in range(self.baris):
            for self.itasi in range(self.kolom):
                    self.Matrix2=list(map(int,input("\nMasukkan Matrix 2:").split()))
                    self.hasil2.append(self.Matrix2)

            
    def cetak(self):
        print("\nMatrix 1:",self.hasil)
        print("\nMatrix 2: ",self.hasil2)

       

hasil= calc()
hasil.niceMeet()
hasil.inptuMatrix1()
hasil.inputMatrix2()
hasil.cetak()            
