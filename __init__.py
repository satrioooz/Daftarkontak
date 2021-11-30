from prettytable import PrettyTable

tabel =PrettyTable()

tabel.field_names = ['URUTAN','NAMA', 'NOMOR TELEPON']

fitur = {'1': 'TAMBAH DATA',
         '2': 'UBAH DATA',
         '3': 'HAPUS DATA',
         '4': 'TAMPILKAN DATA',
         '0': 'KELUAR'
         }

Data = {}
urutan = 0

def TambahData():
    global urutan
    
    urutan +=1
    nama = input('MASUKAN NAMA ANDA :')
    no = str(input('MASUKAN NO TELPON ANDA :'))
    
    Data.update({'URUTAN':urutan,
                'NAMA': nama,
                'NOMOR TELEPON': no
                })
    
    tabel.add_row([urutan, nama, no])
    
def LihatData():
    print(tabel)
    
def Hapus():
    print(tabel)
    urutan = input('URUTAN YANG INGIN DIHAPUS ? :')
    tanya = input('YAKIN INGIN MENGHAPUS DATA ? (Y / T ) :')
    if tanya == 'Y' or tanya =='y':
        tabel.del_row(int(urutan))
        print('\t[*] HAPUS DATA BERHASIL')
    elif tanya == 't' or tanya =='T':
        main()

def Ubah():
    print(tabel)
    urutan = input('URUTAN YANG INGIN DIUBAH ?:')
    tanya = input('YAKIN INGIN MENGUBAH DATA ? ( Y / t )')
    if tanya == 'Y' or tanya == 'y':
        tabel.del_row(int(urutan))
        print('\t[*] MENGUBAH DATA BERHASIL! ')
    elif tanya == 't' or tanya =='T':
        main()


def main():
    print('\t[*] FITUR YANG TERSEDIA')
    for key, value in fitur.items():
        print(f'{key}. {value}')
    print()
    pilih = str(input('\t[*] FITUR YANG INGIN DIPILIH :'))
    while pilih != '0':
        if pilih == '0':
            break
        elif pilih == '1':
            TambahData()
        elif pilih == '2':
            Ubah*()
        elif pilih == '3':
            Hapus()
        elif pilih == '4':
            LihatData()
        
        else:
            print('KEYWOARD ERROR!')
        pilih = str(input('\t[*] FITUR YANG INGIN DIPILIH :'))
    else:
        print('\t[*] PROGRAM SELESAI !')

main()
    
    