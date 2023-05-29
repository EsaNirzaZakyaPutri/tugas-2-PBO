class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)


class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("Nama:", mahasiswa.nama)
            print("NIM:", mahasiswa.nim)
            print()


class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)
        print()


# 1. Implementasi kelas Mahasiswa, Jurusan, dan Universitas
# Sudah diimplementasikan di atas.

# 2. Membuat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# 3. Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)

# 4. Membuat objek Mahasiswa dan menambahkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa_1 = Mahasiswa("Esa Nirza Zakya Putri", "G1A022036", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa_1)

# 5. Menampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# 6. Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_ti.tampilkan_daftar_mahasiswa()

