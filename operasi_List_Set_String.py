# # len()

# contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

# print(contoh_list)
# print(len(contoh_list))


# string = "Belajar Dicoding"

# print(string)
# print(len(string))

# # min() max()

# angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]

# print(f'angka terkecil adalah {min(angka)}')
# print(f'angka terbesar adalah {max(angka)}')


# # .count()

# genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]

# print(genap.count(6))
# print(genap.count(4))

# string = "Belajar Python di Dicoding sangat menyenangkan"

# substring = "a"

# print(f'Jumlah huruf a dalam kalimat tersebut ada {string.count(substring)}')

# # in and not in (output true or false) dapat digunakan untuk condition statement

# kalimat = "Belajar Python di Dicoding sangat menyenangkan"

# print('Dicoding' in kalimat)
# print('Tidak' in kalimat)
# print('Dicoding' not in kalimat)
# print('Tidak' not in kalimat)

# # initialize multiple variable with list

# data = ['shirt', 'white', 'L']

# aparel,color,size = data

# print(data)
# print(aparel)
# print(color)
# print(size)

# # sort (pengurutan data)
# # sort menggunakan ASCII untuk sorting string atau char

# kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
# kendaraan.sort()

# print(f'print ascending {kendaraan}')

# # sort dapat menggunakan reverse = true untuk sort secara descending
# kendaraan.sort(reverse=True)

# print(f'print descending {kendaraan}')

# # error
# # sort tidak dapat mengurutkan data integer dan string sekaligus sehingga satu array variable harus satu tipe data
# # urutan = ['Dicoding', 1, 2, 'Indonesia', 3]

# # urutan.sort()

# # print(urutan)



# """
# TODO:
# Diberikan sebuah variabel berisi nilai list dengan nama "var_list". 
# Berdasarkan list tersebut, cari hal-hal berikut ini:
# - Panjang list tersebut dan simpan dengan nama variabel "panjang".
# - Nilai maksimal list tersebut dan simpan dengan nama variabel "maksimal".
# - Nilai minimal list tersebut dan simpan dengan nama variabel "minimal".
# - Berapa banyak angka 605132 dalam list tersebut dan simpan dalam variabel bernama "banyak"

# Tips:
# - Anda bisa menggunakan berbagai kode yang ada di materi operasi, 
#   tidak diperbolehkan memasukan nilai secara langsung.
# """

# # Jangan ubah kode ini
# var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
# 179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
# 592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
# 950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
# 351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
# 175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
# 407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
# 605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
# 673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
# 235780, 857943, 605132, 125094, 620493, 913250
# ]

# # TODO: Buat kode Anda di bawah ini

# panjang = len(var_list)
# maksimal = max(var_list)
# minimal = min(var_list)
# banyak = var_list.count(605132)

# print(panjang)
# print(maksimal)
# print(minimal)
# print(banyak)
