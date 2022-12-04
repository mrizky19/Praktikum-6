from tabulate import tabulate

dataMahasiswa = {}


print("PROGRAM INPUT NILAI")
print("===================")

def tambah(loop):
    print ("\n════════════Masukan Data Mahasiswa════════════")
    no = 0
    while(loop == "y"):
        while (True):
            nama = input("NAMA : ")
            if nama == '':
                print ('Nama tidak boleh kosong')
            else:
                break
        while (True):
            try:
                nim  = int(input("NIM  : "))
                if nim == '':
                    print ('Masukan Nim dengan Angka')
            except ValueError:
                print ('Masukan Nim dengan Angka')
            else:
                break
        while (True):
            try:
                tugas  = int(input("TUGAS  : "))
                if tugas == '':
                    print ('Masukan TUGAS dengan Angka')
            except ValueError:
                print ('Masukan TUGAS dengan Angka')
            else:
                break
        while (True):
            try:
                uts  = int(input("UTS  : "))
                if uts == '':
                    print ('Masukan UTS dengan Angka')
            except ValueError:
                print ('Masukan UTS dengan Angka')
            else:
                break
        while (True):
            try:
                uas  = int(input("UAS  : "))
                if uas == '':
                    print('Masukan UAS dengan Angka')
            except ValueError:
                print ('Masukan UAS dengan Angka')
            else:
                break
        akhir = round(tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
        no += 1
        dataMahasiswa[nim] = [no,nim,nama,tugas,uts,uas,akhir]
        loop = input("Lanjut input data? (y/t) = ")
    while(loop == "t"):
        break


def tampilkan():
    no = 0
    no += 1
    list = (dataMahasiswa.values())
    print(tabulate(list, headers=["No", "Nim", "Nama", "Tugas", "UTS", "UAS", "Nilai Akhir"], tablefmt="fancy_grid"))
    print("")

def hapus(nama):
    while True:
        try:    
            nims = int(input('Masukkan NIM data yang ingin di hapus : '))
        except ValueError:
                print ('Masukan NIM dengan angka')
        else:
            break    

    if nims in (dataMahasiswa.keys()):
        exekusi = input('Yakin Mau di hapus lur? (y/t) : ')
        if exekusi == 'y':
            del dataMahasiswa[nims]
        else :
            print("Data enggak jadi di hapus lur")
    else :
        print("NIM yang lu input enggak ada lur")  


def ubah(nama):
    no = 0
    list = (dataMahasiswa.values())
    while True:
        try:    
            nims = int(input('Masukkan NIM : '))
        except ValueError:
                print ('Masukan NIM dengan angka')
        else:
            break
            
    if nims in (dataMahasiswa.keys()):

        print('Pilih data yang mau di edit')
        edit = input('[(1)nama, (2)tugas, (3)uts, (4)uas, (x)Enggak Jadi/udah ? ] = ')
        if edit == '1':
            # Belum jadi yg nim
            newNama = (input("Masukan Nama : "))
            dataMahasiswa[nims][2] = newNama
        elif edit == '2' :
            newTugas = float(input("Masukan Nilai Tugas : "))
            dataMahasiswa[nims][3] = newTugas
            akhir = round(dataMahasiswa[nims][3] * 30 / 100) + (dataMahasiswa[nims][4] * 35 / 100) + (dataMahasiswa[nims][5] * 35 / 100)
            dataMahasiswa[nims][6] = akhir
        elif edit == '3' :
            newUts = float(input("Masukan Nilai UTS : "))
            dataMahasiswa[nims][4] = newUts
            akhir = round(dataMahasiswa[nims][3] * 30 / 100) + (dataMahasiswa[nims][4] * 35 / 100) + (dataMahasiswa[nims][5] * 35 / 100)
            dataMahasiswa[nims][6] = akhir
        elif edit == '4' :
            newUas = float(input("Masukan Nilai Uas : "))
            dataMahasiswa[nims][5] = newUas
            akhir = round(dataMahasiswa[nims][3] * 30 / 100) + (dataMahasiswa[nims][4] * 35 / 100) + (dataMahasiswa[nims][5] * 35 / 100)
            dataMahasiswa[nims][6] = akhir
    else:
        print("Nik lu belum ada lur")

    

while True:

    print("[(T)ambah, (U)bah, (H)apus, (L)ihat, (K)eluar]")
    pilihan = input("\nPilih Opsi= ")

    if pilihan.lower() == "t":
        tambah("y")
    elif pilihan.lower() == "u":
        ubah("ok")
    elif pilihan.lower() == "h":
        hapus('ok')
    elif pilihan.lower() == "l":
        tampilkan()
    elif pilihan.lower() == "k":
        break
    else:
        print("Opsi yang anda pilih tidak ada di menu")
        print("")

