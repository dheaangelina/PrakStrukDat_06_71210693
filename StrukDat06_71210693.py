class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__ (self):
        return self.size
    
    def isEmpty (self):
        return self.size == 0

    def insert_head (self, no_rekening, nama, saldo):
        baru = NodeTabungan(no_rekening, nama, saldo)
        if self.isEmpty() == True:
            self.head = baru 
            self.tail = baru
        else:
            baru.next = self.head
            self.head = baru
        self.size += 1

    def delete(self, indeks):
        posisi = self.head
        if indeks == self.size-1:
            while posisi.next != self.tail:
                posisi = posisi.next
            del self.tail
            self.tail = posisi
            self.tail.next = None
            self.size -= 1
        elif indeks == 0:
            self.head = posisi.next
            del posisi
            self.size -= 1
        else:
            for i in range(indeks-1):
                posisi = posisi.next
            posisi.next = posisi.next.next
            del posisi.next
        self.size -= 1

    def print(self):
        posisi = self.head
        while posisi:
            print(f"Norek: {posisi.no_rekening}")
            print(f"Nama: {posisi.nama}")
            print(f"Saldo: {posisi.saldo}")
            print()
            posisi = posisi.next

    def filter(self, saldo):
        if self.isEmpty() == False:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                bantu = self.head
                while bantu.next != self.tail:
                    bantu = bantu.next
                hapus = self.tail
                self.tail = bantu
                self.tail.next = None
                del hapus
            self.size -= 1

    def update(self,bunga):
        if bunga >= 0 and bunga <= 100 :
            persen = bunga * 0.01
            self.saldo = bunga + persen
            print(f"Norek: {self.no_rekening}")
            print(f"Nama: {self.nama}")
            print(f"Saldo: {self.saldo}")
        else:
            print("Maaf besaran persen harus diantara 0-100")
            print()
    
slnc = SLNC()
slnc.insert_head(201,"Hanif", 250000)
slnc.insert_head(110,"Yudha", 150000)
slnc.print()
slnc.filter(100)
slnc.print()
slnc.update(200)
slnc.update(50)
slnc.print()