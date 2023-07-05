# Tugas Besar Proyek Struktur Data dan Algoritma

Membuat SI Rumah Sakit dengan materi Linear Search berdasarkan pandangan User
dan Admin.

Anggota Kelompok 2: 

- G1A022006 - Merly Yuni Purnama 
- G1A022004 - Akram Analis 
- G1A022020 - Atika Oktavianti 
- G1A022040 - Sinta Ezra Wati Gulo 

## Sistem Informasi Rumah Sakit

Merupakan sebuah aplikasi GUI yang dirancang menggunakan modul tkinter di Python untuk mengimplementasikan Sistem Informasi Rumah Sakit. Aplikasi ini memiliki beberapa halaman yang memungkinkan pengguna untuk memilih peran sebagai Admin atau Pengguna (User).

## Deskripsi Kode

1. Mengimport modul dan submodul yang dibutuhkan, yaitu ```tkinter, messagebox, dan ttk```
2. Mengatur tampilan utama window menggunakan ```tkinter.Tk()```
3. Membuat beberapa halaman dalam bentuk ```tkinter.Frame()``` yang akan digunakan untuk menampilkan konten.
4. Mengatur posisi halaman menggunakan perulangan ```for```
5. Membuat fungsi ```show_frame()``` untuk menampilkan halaman yang dipilih.
6. Mengatur tampilan dan konten pada setiap halaman dengan menggunakan objek ```tkinter.Label, tkinter.Button, dan tkinter.Entry```
7. Mengatur latar belakang halaman dengan menggunakan gambar dalam ```format .png```
8. Mengimplementasikan fungsi-fungsi seperti ```cek_login(), tambah_pasien(), tampilkan_data(), hapus_pasien(), dan update_pasien()``` untuk menjalankan fungsionalitas aplikasi.
9. Menggunakan ```ttk.Treeview``` untuk menampilkan data pasien dalam bentuk tabel.
10. Mengatur gaya khusus untuk tabel menggunakan ```ttk.Style()```

## Penjelasan Kode dan Fungsi Setiap Page: 

### Page 1
Page 1 merupakan halaman utama dari aplikasi Sistem Informasi Rumah Sakit. Pada halaman ini terdapat dua pilihan yang dapat dipilih, yaitu "Admin" dan "User".

Tombol "Admin" akan memindahkan pengguna ke halaman Page 2, yang merupakan halaman login bagi administrator.
Tombol "User" akan memindahkan pengguna ke halaman Page 6, yang merupakan halaman login bagi pengguna.

### Page 2
Page 2 adalah halaman login untuk administrator. Pada halaman ini, administrator diminta untuk memasukkan username dan password. Jika input username dan password sesuai (admin dan 12345), pengguna akan diarahkan ke halaman Page 3.

Tombol "Login" akan memanggil fungsi cek_login() untuk memeriksa kecocokan username dan password yang dimasukkan.
Tombol "Back" akan kembali ke halaman Page 1.

### Page 3
Page 3 merupakan halaman selamat datang bagi administrator setelah berhasil login. Pada halaman ini, administrator dapat memilih opsi untuk memasukkan data pasien atau data obat.

Tombol "Input Data Pasien" akan memindahkan pengguna ke halaman Page 4, yang merupakan halaman untuk memasukkan data pasien.
Tombol "Input Data Obat" akan memindahkan pengguna ke halaman Page 5, yang merupakan halaman untuk memasukkan data obat.
Tombol "Logout" akan memindahkan pengguna ke halaman Page 2 untuk keluar dari akun administrator.

### Page 4
Page 4 adalah halaman untuk memasukkan data pasien. Pada halaman ini, administrator dapat memasukkan informasi pasien seperti nama, umur, jenis kelamin, alamat, ruangan, dan jenis penyakit. Data pasien yang dimasukkan akan disimpan dalam array ```data_pasien``` dan ditampilkan dalam bentuk tabel menggunakan komponen Treeview.

Setelah memasukkan data pasien, pengguna dapat menekan tombol "Tambah Pasien" untuk memasukkan data tersebut ke dalam array ```data_pasien```.
Tombol "Hapus Pasien" digunakan untuk menghapus data pasien yang dipilih dari array ```data_pasien``` dan mengupdate tampilan tabel.
Tombol "Update Pasien" akan memunculkan jendela pop-up yang memungkinkan administrator untuk mengubah data pasien yang telah dimasukkan sebelumnya.

### Page 5
Page 5 adalah halaman untuk memasukkan data obat. Pada halaman ini, administrator dapat memasukkan informasi obat seperti nama obat, kategori, jumlah stok, dan harga. Data obat yang dimasukkan akan disimpan dalam array data_obat dan ditampilkan dalam bentuk tabel menggunakan komponen Treeview.

Setelah memasukkan data obat, pengguna dapat menekan tombol "Tambah Obat" untuk memasukkan data tersebut ke dalam array ```data_obat```.
Tombol "Hapus Obat" digunakan untuk menghapus data obat yang dipilih dari array ```data_obat``` dan mengupdate tampilan tabel.
Tombol "Update Obat" akan memunculkan jendela pop-up yang memungkinkan administrator untuk mengubah data obat yang telah dimasukkan sebelumnya.

### Page 6
Page 6 adalah halaman login untuk pengguna. Pada halaman ini, pengguna diminta untuk memasukkan username dan password. Jika input username dan password sesuai (user dan 12345), pengguna akan diarahkan ke halaman Page 7.

Tombol "Login" akan memanggil fungsi ```cek_login()``` untuk memeriksa kecocokan username dan password yang dimasukkan.
Tombol "Back" akan kembali ke halaman Page 1.

### Page 7
Page 7 merupakan halaman selamat datang bagi pengguna setelah berhasil login. Pada halaman ini, pengguna dapat melihat data pasien yang telah dimasukkan oleh administrator.

Tombol "Tampilkan Data" akan memanggil fungsi ```tampilkan_data()``` untuk menampilkan data pasien dalam bentuk tabel.
Tombol "Logout" akan memindahkan pengguna ke halaman Page 6 untuk keluar dari akun pengguna.
Kode ini merupakan aplikasi sederhana untuk memahami dasar-dasar penggunaan modul tkinter dan membangun antarmuka pengguna. Anda dapat menyesuaikan dan memperluas fungsionalitas aplikasi sesuai dengan kebutuhan Anda.

### Page 8
Page 8 adalah halaman untuk menampilkan data pasien berdasarkan kriteria tertentu. Pada halaman ini, pengguna dapat memilih kriteria pencarian seperti jenis kelamin, ruangan, atau jenis penyakit. Setelah memilih kriteria, pengguna dapat menekan tombol "Cari" untuk mencari data pasien yang sesuai dan menampilkannya dalam bentuk tabel.

Setelah memilih kriteria pencarian, pengguna dapat menekan tombol "Cari" untuk memanggil fungsi ```cari_data()``` dan mencari data pasien yang sesuai dengan kriteria yang dipilih.
Tombol "Back" akan kembali ke halaman Page 7.

### Page 9
Page 9 adalah halaman untuk menampilkan data obat. Pada halaman ini, pengguna dapat melihat data obat yang telah dimasukkan oleh administrator.

Tombol "Tampilkan Data" akan memanggil fungsi ```tampilkan_data_obat()``` untuk menampilkan data obat dalam bentuk tabel.
Tombol "Logout" akan memindahkan pengguna ke halaman Page 6 untuk keluar dari akun pengguna.

Program untuk membuat SI Rumah Sakit dengan Linear Search: 

https://github.com/merlyyunipurnama/TuBes-SDA/blob/main/SourceCode.py

## Authors

- [@merlyyunipurnama](https://www.github.com/octokatherine)
