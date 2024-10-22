# upper lower

# kata = 'dicoding'
# kata = kata.upper() # upper untuk mengubah string menjadi huruf besar

# word = 'DICODING'
# word = word.lower() # lower untuk mengubah string menjadi huruf kecil

# string = 'Dicoding'
# # string = string.upper()
# string = string.lower()

# string1 = '1234'
# string1 = string1.lower()


# print(kata)
# print(word)
# print(string)
# print(string1)

# rstrip() untuk menghapus spasi samping kanan
# kata = 'dicoding            '

# kata = kata.rstrip()

# print(f'{kata}aja')

#lstrip
# kata = '           dicoding'

# kata = kata.lstrip()

# print(f'ayo{kata}')


#strip() untuk menhapus spasi secara default. bisa menghapus suatu kata atau string yang disesuaikan

# kata = 'PalaPalabotakPalaPala'


# print(kata.strip("Pala"))

# .starswith menemukan suatu string diawal string dan mengebalikan nilai boolean 
# (TRUE jika ditemukan string yang dicari dan sebaliknya) (case sensitive)

# print('Dicoding Indonesia' .startswith("Dicoding"))

# kalimat = "Bambang Kotak"

# riyalorpake1 = kalimat.startswith("Bambang")
# riyalorpake2 = kalimat.startswith("Kotak")

# print(riyalorpake1)
# print(riyalorpake2)

# .endswith, seperti starswitch yang menemukan string namun diakhir string
# (case sensitive)

# print('Dicoding Indonesia' .endswith("Indonesia"))

# kalimat = "Bambang Kotak"

# riyalorpake1 = kalimat.endswith("Bambang")
# riyalorpake2 = kalimat.endswith("Kotak")

# print(riyalorpake1)
# print(riyalorpake2)

# .join() untuk menggabungkan 2 string dengan delimiter yang ditentukan

# print(' '.join(['Dicoding', 'Indonesia', '!']))

# kata1 = "rotasi"
# kata2 = "elu"
# kata3 = "kayak"
# kata4 = "bengkoank"

# delimiter = ' '

# kalimat = delimiter.join([kata1, kata2, kata3, kata4])

# print(kalimat)

# .split(), untuk memisahkan string dan output menjadi list

# print('Dicoding Indonesia !'.split())

# print('''halo,
#       saya bambang,
#       saya bumbung,
#       saya bimbing,
#       saya bembeng,
#       saya bombong
#       '''. split("\n"))


# .replace(), untuk mengganti string dengan spesifik

# string = "ayo pecekin idung ayaangg"

# print(string.replace("pecekin", "ratain"))

# .isupper() untuk mengecek apakah string menggunakan huruf besar semua
# kata = "DICODING"
# print(kata.isupper())

# .islower() untuk mengecek apakah string menggunakan huruf besar semua
# kata = "dicoding"
# print(kata.islower())

# .isalpha() untuk mengecek apakah string menggunakan alphabetic 
# kata = "dicoding"

# print(kata.isalpha())

# .isalnum() untuk mengecek apakah string menggunakan salah satu antara alphabetic atau numerik atau dua duanya
# kata = "123dicoding"

# print(kata.isalnum())

# .isdecimal() untuk mengecej apakah string menggunakan numerik semua

# kata = "123"

# print(kata.isdecimal())

# .isspace() untuk mengecej apakah string menggunakan whitespace saja

# print('     ' .isspace())


# .istitle() untuk mengecej apakah string menggunakan menggunakan huruf kapital

# kalimat1 = "Dicoding Indonesia"
# kalimat2 = "dicoding indonesia"

# print(kalimat1.istitle())
# print(kalimat2.istitle())

# .zfill() untuk mengisi nilai 0 pada string untuk menyesuaikan dengan panjang string
# dalam hal ini kata botak adalah 5 huruf atau karakter, sementara yang diminta atau dimasukan ke dalam teks fill
# harus 6 katakter, sehingga haus ditambahkan 1 "0" untuk sesuai

# teks = 'botak'

# addstr = teks.zfill(6)
# print(addstr)

# rjust untuk melakukan rata kanan, ljust untuk melakukan rata kiri, 
# center untuk memindahkan string menjadi di tengah

# print("Dicoding Botak".rjust(20," "))

# print("Dicoding Botak".ljust(20,"?"))

# print("Dicoding Botak".center(20,"-"))

#Python mengetahui bahwa pada Jum\'at, sebelum petik terdapat backslash (\) yang menandakan petik tunggal sebagai bagian dari string dan bukan akhir dari string. Escape character \' dan \" memungkinkan Anda untuk memasukkan karakter ' dan '' dalam bagian string. Beberapa contoh escape character lainnya sebagai berikut. 

# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash