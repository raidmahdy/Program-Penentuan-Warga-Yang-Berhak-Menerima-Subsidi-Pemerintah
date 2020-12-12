i=a=b=c=0
print('Hallo, Selamat Datang di Tembalang :D')
print('Kampung Elegan Milik Kita Bersama')
print('')
print('')
print('Program Ini Bertujuan Untuk Mengetahui Warga Yang Pantas Mendapat Bantuan Subsidi Pemerintah.')
print('')
print('')
i=0
nama=[]
nmrrmh=[]
kis=[]
kndrn=[]
klmpk=[]
jmlh=[]
while True:
    print('Masukkan data ke -',i+1)
    nama.append(input('Nama Panggilan Anda (Menggunakan Huruf Kecil Semua) : '))
    input('Apa Pekerjaan Anda : ')
    input('Apa Pekerjaan Istri Anda : ')
    input('Gaji Anda Perbulan Saat Ini : ')
    input('Gaji Istri Perbulan Saat Ini : ')
    input('Berapa Anak Anda : ')
    input('Apakah Anda Memiliki KIM : ')
    input('Berapa Biaya Tagihan Listrik Perbulan : ')
    input('Berapa Biaya Tagihan Pam Perbulan (Isi Jika Memasanng PAM) :  ')
    input('Berapa Biaya Wifi Perbulan(Isi Jika Mamasang Wifi) : ')
    nmrrmh.append(input('Masukan Nomer Rumah Anda, 3 digit. Contoh : 24D. : '))
    if len(nmrrmh[i])!=3:
        print('Nomor Rumah Tidak Valid !')
        print
        nama.pop(i)
        nmrrmh.pop(i)
        continue
    kis.append(input('Masukan 16 digit angka pada KIS Jika Memiliki Kartu Indonesia Sejahtera (KIS), jika tidak isi saja huruf t 16 kali : '))
    if len(kis[i])!=16:
        print('KIS Tidak Valid')
        print
        nama.pop(i)
        nmrrmh.pop(i)
        kis.pop(i)
        continue
    kndrn.append(input('Berapa Jumlah Kendaraan Bermotor Anda CARA PENGISIAN (Jika tidak punya : tidak, jika punya 1 : punya, jika lebih dari 1 : lebih) : '))
    if len(kndrn[i])!=5:
        print('Input Tidak Valid')
        print
        nama.pop(i)
        nmrrmh.pop(i)
        kis.pop(i)
        kndrn.pop(i)
        continue
    klmpk.append(kndrn[i])
    if klmpk[i]=='tidak':
        klmpk[i]='Ekonomi Kebawah'
        a+=1
    elif klmpk[i]=='punya':
        klmpk[i]='Ekonomi Menengah'
        b+=1
    elif klmpk[i]=='lebih':
        klmpk[i]='Ekonomi Ke atas'
        c+=1
    else:
        print('Input Salah')
        print
        continue
    lagi=''
    while lagi!='y' and lagi!='t':
        lagi=input('INPUT LAGI [y/t] : ')
        i+=1
    if lagi!='y':
        break
