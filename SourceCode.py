# Mengimport Modul dan Submodul
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Mengatur tampilan window
window = tk.Tk()

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.geometry("1024x768")

# Membuat halaman 
page1 = tk.Frame(window)
page2 = tk.Frame(window)
page3 = tk.Frame(window)
page4 = tk.Frame(window)
page5 = tk.Frame(window)
page6 = tk.Frame(window)
page7 = tk.Frame(window)
page8 = tk.Frame(window)
page9 = tk.Frame(window)

# Perulangan yang mengatur posisi halaman
for frame in (page1, page2, page3, page4, page5, page6, page7, page8, page9):
    frame.grid(row=0, column=0, sticky='nsew')

# Fungsi untuk menampilkan halaman
def show_frame(frame):
    frame.tkraise()

show_frame(page1)

# ==================================================== Page 1 ====================================================

# Mengatur Latar Belakang
page1.config(background="#FFC948")
bg1= tk.PhotoImage(file="1.png")
page1_bg =tk.Label(page1, image=bg1)
page1_bg.place(x=0, y=0)

# Mengatur tampilan tulisan
page1_teks =tk.Label(page1, text='SISTEM INFORMASI\nRUMAH SAKIT', font=('Durian Days', 30, 'bold'), fg='black', compound="bottom")
page1_teks.place(x=450, y=50)

# Membuat dan Mengatur tombol button
tombol_admin =tk.Button(page1, text = ' Admin ', font=('Consolas',15), activebackground='blue', command=lambda: show_frame(page2))
tombol_admin.place(x=600, y=350)
tombol_user =tk.Button(page1, text = ' User ', font=('Consolas',15), activebackground='blue', command=lambda: show_frame(page6))
tombol_user.place(x=605, y=450)

# Mengatur tampilan tulisan
page1_subteks1 = tk.Label(page1, text = ' MASUK SEBAGAI: ', font = ('Consolas', 15, 'bold'),fg= 'black', bg= 'white')
page1_subteks1.place(x=560, y=260)
page1_subteks2 = tk.Label(page1, text = ' atau ', font = ('Anton', 12),fg= 'black', bg= 'white')
page1_subteks2.place(x=625, y=408)

# ==================================================== Page 2 ====================================================

# Mengatur Latar Belakang
page2.config(background="white")
bg2= tk.PhotoImage(file="3.png")
page2_bg =tk.Label(page2, image=bg2)
page2_bg.place(x=0, y=0)

# Mengatur tampilan tulisan
page2_teks =tk.Label(page2, text='SIGN IN', font=('calibri', 30, 'bold'), bg = "white" , fg='black')
page2_teks.place(x=580, y=100)

# Fungsi untuk cek login
def cek_login():
    username_admin = entry_username.get()
    password_admin = entry_password.get()
    if username_admin == "admin" and password_admin == "12345":
        page2.pack_forget()
        show_frame(page3)
                  
    else:
        messagebox.showinfo("WARNING", "Username atau password anda salah!")

# Membuat label dan entry untuk username
label_username = tk.Label(master=page2, text="Username:", font=("Calibri",15), fg='white', bg= "black")
label_username.place(x=480, y=250)
entry_username = tk.Entry(master=page2, font=('Calibri', 15), bg="white")
entry_username.place(x=600, y=250)

# Membuat label dan entry untuk password
label_password = tk.Label(master=page2, text="Password:", font=("Calibri", 15), fg='white', bg= "black")
label_password.place(x=480, y=300)
entry_password = tk.Entry(master=page2, font=('Calibri', 15), bg="white", show="*")
entry_password.place(x=600, y=300)

# Membuat button untuk login dan back
button_login1 = tk.Button(master=page2, text=" Login ", font=("Consolas",15), activebackground='blue', command=cek_login) 
button_login1.place(x=600, y=400)
tombol_back =tk.Button(page2, text = " Back ", font=("calibri",15), activebackground="blue", command=lambda: show_frame(page1))
tombol_back.place(x=615, y=450)

# ==================================================== Page 3 ====================================================

# Mengatur Latar Belakang
page3.config(background="#FFC948")
bg3= tk.PhotoImage(file="1.png")
page3_bg =tk.Label(page3, image=bg3)
page3_bg.place(x=0, y=0)

# Mengatur tampilan tulisan
page3_teks =tk.Label(page3, text='SELAMAT DATANG DI HALAMAN ADMIN', font=('Durian Days', 30, 'bold'), fg='black', compound="bottom")
page3_teks.place(x=250, y=50)

# Membuat dan mengatur tombol button
tombol_tambahpasien =tk.Button(page3, text = ' Input Data Pasien ', font=('Consolas',15), activebackground='blue', command=lambda: show_frame(page4))
tombol_tambahpasien.place(x=525, y=350)
tombol_tambahobat =tk.Button(page3, text = ' Input Data Obat ', font=('Consolas',15), activebackground='blue', command=lambda: show_frame(page5))
tombol_tambahobat.place(x=535, y=450)

# Mengatur tampilan tulisan
page3_subteks1 = tk.Label(page3, text = ' SILAHKAN PILIH DATA YANG AKAN DI INPUT: ', font = ('Consolas', 15, 'bold'),fg= 'black', bg= 'white')
page3_subteks1.place(x=400, y=260)
page3_subteks2 = tk.Label(page3, text = ' atau ', font = ('Calibri', 12),fg= 'black', bg= 'white')
page3_subteks2.place(x=610, y=408)

# Membuat dan mengatur tombol button
tombol_logout =tk.Button(page3, text = " Logout ", font=("calibri",15), activebackground="white", bg='white', command=lambda: show_frame(page2))
tombol_logout.place(x=1200, y= 600)

# ==================================================== Page 4 ====================================================

# Mengatur Latar Belakang
page4.config(background='#ADD8E6')
bg4= tk.PhotoImage(file="2.png")
page4_bg =tk.Label(page4, image=bg4)
page4_bg.place(x=0, y=0)

# Data pasien disimpan dalan array
data_pasien =  [
    {"nama": "Akram Analis", "umur": 25, "jenis_kelamin": "Laki-laki", "alamat": "Kandang Limun", "ruangan": "UGD", "jenis_penyakit": "Maag"},
    {"nama": "Merly Yuni Purnama", "umur": 23, "jenis_kelamin": "Perempuan", "alamat": "Lingkar Barat", "ruangan": "Kamar Operasi", "jenis_penyakit": "Pendarahan"},
    {"nama": "Atika Oktavianti", "umur": 22, "jenis_kelamin": "Perempuan", "alamat": "Sawah Lebar", "ruangan": "Kamar Perawat", "jenis_penyakit": "Sesak Napas"}
]

# Fungsi tambah data pasien
def tambah_pasien():
    nama = entry_nama.get()
    umur = int(entry_umur.get())
    jenis_kelamin = entry_jenis_kelamin.get()
    alamat = entry_alamat.get()
    ruangan = entry_ruangan.get()
    jenis_penyakit = entry_jenis_penyakit.get()

    pasien = {"nama": nama, "umur": umur, "jenis_kelamin": jenis_kelamin, "alamat": alamat, "ruangan": ruangan, "jenis_penyakit": jenis_penyakit}
    data_pasien.append(pasien)

    entry_nama.delete(0, tk.END)
    entry_umur.delete(0, tk.END)
    entry_jenis_kelamin.delete(0, tk.END)
    entry_alamat.delete(0, tk.END)
    entry_ruangan.delete(0, tk.END)
    entry_jenis_penyakit.delete(0, tk.END)

# Fungsi tampilkan data pasien
def tampilkan_data():
    # Menghapus data pada Treeview sebelum menampilkan data terbaru
    tree_admin.delete(*tree_admin.get_children())

    if data_pasien:
        # Mengisi data pasien ke dalam Treeview
        for i, pasien in enumerate(data_pasien, start=1):
            tree_admin.insert("","end", text=str(i), values=(pasien["nama"], pasien["umur"], pasien["jenis_kelamin"], pasien["alamat"], pasien["ruangan"], pasien["jenis_penyakit"]))

# Fungsi hapus data pasien
def hapus_pasien():
    selected_item = tree_admin.selection()
    if selected_item:
        index = int(tree_admin.item(selected_item)["text"]) - 1
        data_pasien.pop(index)
        tampilkan_data()
        messagebox.showinfo("Pemberitahuan", "Data Pasien Telah Dihapus! ")

# Fungsi update data pasien
def update_pasien():
    selected_item = tree_admin.selection()
    if selected_item:
        index = int(tree_admin.item(selected_item)["text"]) - 1
        pasien = data_pasien[index]

        window_update = tk.Toplevel(window)
        window_update.title("Update Pasien")

        label_nama_update = tk.Label(window_update, text="Nama:")
        label_nama_update.pack()
        entry_nama_update = tk.Entry(window_update)
        entry_nama_update.pack()
        entry_nama_update.insert(tk.END, pasien["nama"])

        label_umur_update = tk.Label(window_update, text="Umur:")
        label_umur_update.pack()
        entry_umur_update = tk.Entry(window_update)
        entry_umur_update.pack()
        entry_umur_update.insert(tk.END, str(pasien["umur"]))

        label_jenis_kelamin_update = tk.Label(window_update, text="Jenis Kelamin:")
        label_jenis_kelamin_update.pack()
        entry_jenis_kelamin_update = tk.Entry(window_update)
        entry_jenis_kelamin_update.pack()
        entry_jenis_kelamin_update.insert(tk.END, pasien["jenis_kelamin"])

        label_alamat_update = tk.Label(window_update, text="Alamat:")
        label_alamat_update.pack()
        entry_alamat_update = tk.Entry(window_update)
        entry_alamat_update.pack()
        entry_alamat_update.insert(tk.END, pasien["alamat"])

        label_ruangan_update = tk.Label(window_update, text="Ruangan:")
        label_ruangan_update.pack()
        entry_ruangan_update = tk.Entry(window_update)
        entry_ruangan_update.pack()
        entry_ruangan_update.insert(tk.END, pasien["ruangan"])

        label_jenis_penyakit_update = tk.Label(window_update, text="Jenis Penyakit:")
        label_jenis_penyakit_update.pack()
        entry_jenis_penyakit_update = tk.Entry(window_update)
        entry_jenis_penyakit_update.pack()
        entry_jenis_penyakit_update.insert(tk.END, pasien["jenis_penyakit"])

        def simpan_update():
            pasien["nama"] = entry_nama_update.get()
            pasien["umur"] = int(entry_umur_update.get())
            pasien["jenis_kelamin"] = entry_jenis_kelamin_update.get()
            pasien["alamat"] = entry_alamat_update.get()
            pasien["ruangan"] = entry_ruangan_update.get()
            pasien["jenis_penyakit"] = entry_jenis_penyakit_update.get()

            window_update.destroy()
            tampilkan_data()
            messagebox.showinfo("Pemberitahuan", "Data Pasien Telah Diperbarui! ")

        button_simpan_update = tk.Button(window_update, text="Simpan", command=simpan_update)
        button_simpan_update.pack()

# Label dan entry tambah pasien
label_tambah_pasien = tk.Label(page4, text="TAMBAH PASIEN", font=("calibri",20, 'bold'))
label_tambah_pasien.place(x=570,y=50)

label_nama = tk.Label(page4, text="Nama:")
label_nama.place(x=545, y=100)
entry_nama = tk.Entry(page4)
entry_nama.place(x=655, y=100)

label_umur = tk.Label(page4, text="Umur:")
label_umur.place(x=545, y=125)
entry_umur = tk.Entry(page4)
entry_umur.place(x=655, y=125)

label_jenis_kelamin = tk.Label(page4, text="Jenis Kelamin:")
label_jenis_kelamin.place(x=545, y=150)
entry_jenis_kelamin = tk.Entry(page4)
entry_jenis_kelamin.place(x=655, y=150)

label_alamat = tk.Label(page4, text="Alamat:")
label_alamat.place(x=545, y=175)
entry_alamat = tk.Entry(page4)
entry_alamat.place(x=655, y=175)

label_ruangan = tk.Label(page4, text="Ruangan:")
label_ruangan.place(x=545, y=200)
entry_ruangan = tk.Entry(page4)
entry_ruangan.place(x=655, y=200)

label_jenis_penyakit = tk.Label(page4, text="Penyakit:")
label_jenis_penyakit.place(x=545, y=225)
entry_jenis_penyakit = tk.Entry(page4)
entry_jenis_penyakit.place(x=655, y=225)

# Membuat gaya khusus untuk tabel
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background="#1D267D", foreground="white", fieldbackground="#1D267D")

# Membuat Treeview untuk menampilkan data pasien
tree_admin = ttk.Treeview(page4)
tree_admin["columns"] = ("Nama", "Umur", "Jenis Kelamin", "Alamat", "Ruangan", "Jenis Penyakit")
tree_admin.place(x=250, y=320)

# Mengatur lebar kolom pada Treeview
tree_admin.column("#0", width=50)
tree_admin.column("Nama", width=150)
tree_admin.column("Umur", width=50)
tree_admin.column("Jenis Kelamin", width=100)
tree_admin.column("Alamat", width=200)
tree_admin.column("Ruangan", width=100)
tree_admin.column("Jenis Penyakit", width=150)

# Menampilkan heading kolom
tree_admin.heading("#0", text="No.")
tree_admin.heading("Nama", text="Nama")
tree_admin.heading("Umur", text="Umur")
tree_admin.heading("Jenis Kelamin", text="Jenis Kelamin")
tree_admin.heading("Alamat", text="Alamat")
tree_admin.heading("Ruangan", text="Ruangan")
tree_admin.heading("Jenis Penyakit", text="Jenis Penyakit")

# Mengatur tinggi tabel
tree_admin["height"] = 10

# Tombol Tambah Pasien
button_tambah = tk.Button(page4, text="Tambah", command=tambah_pasien)
button_tambah.place(x=620, y=250)

# Tombol Tampilkan Data
button_tampilkan_data = tk.Button(page4, text="Tampilkan Data", bg='green', command=tampilkan_data)
button_tampilkan_data.place(x=600,y=550)

# Tombol Hapus Pasien
button_hapus = tk.Button(page4, text="Hapus", bg='red', command=hapus_pasien)
button_hapus.place(x=625,y=585)

# Tombol Update Pasien
button_update = tk.Button(page4, text="Update", bg='yellow', command=update_pasien)
button_update.place(x=622, y=285)

tombol_logout =tk.Button(page4, text = " Back ", font=("calibri",15), activebackground="white", bg='blue', command=lambda: show_frame(page3))
tombol_logout.place(x=1200, y= 600)

# ==================================================== Page 5 ====================================================

# Mengatur Latar Belakang
page5.config(background='#ADD8E6')
bg5= tk.PhotoImage(file="2.png")
page5_bg =tk.Label(page5, image=bg4)
page5_bg.place(x=0, y=0)

# Data pasien disimpan dalan array
data_obat = []

# Fungsi tambah data obat
def tambah_obat():
    nama_penyakit = entry_penyakit.get()
    nama_obat = str(entry_obat.get())

    obat = {"nama penyakit": nama_penyakit, "nama obat": nama_obat}
    data_obat.append(obat)

    entry_penyakit.delete(0, tk.END)
    entry_obat.delete(0, tk.END)

# Fungsi tampilkan data obat
def tampilkan_data_obat():

# Menghapus data pada Treeview sebelum menampilkan data terbaru
    tree_obat.delete(*tree_obat.get_children())

    if data_obat:
        # Mengisi data obat ke dalam Treeview
        for i, obat in enumerate(data_obat, start=1):
            tree_obat.insert("", "end", text=str(i), values=(obat["nama penyakit"], obat["nama obat"]))
            
# Fungsi hapus data obat
def hapus_obat():
    selected_item = tree_obat.selection()
    if selected_item:
        index = int(tree_obat.item(selected_item)["text"]) - 1
        data_obat.pop(index)
        tampilkan_data_obat()
        messagebox.showinfo("Pemberitahuan", "Data Obat Telah Dihapus!")

# Fungsi update data obat
def update_obat():
    selected_item = tree_obat.selection()
    if selected_item:
        index = int(tree_obat.item(selected_item)["text"]) - 1
        obat = data_obat[index]

        window_update = tk.Toplevel(window)
        window_update.title("Update Jenis Obat")

        label_obat_update = tk.Label(window_update, text="Jenis Obat:")
        label_obat_update.pack()
        entry_obat_update = tk.Entry(window_update)
        entry_obat_update.pack()
        entry_obat_update.insert(tk.END, str(obat["nama obat"]))

        def simpan_update():
            obat["nama obat"] = entry_obat_update.get()

            window_update.destroy()
            tampilkan_data_obat()
            messagebox.showinfo("Pemberitahuan", "Data Obat Telah Diperbarui!")

        button_simpan_update = tk.Button(window_update, text="Simpan", command=simpan_update)
        button_simpan_update.pack()

# Label dan entry tambah jenis obat
label_tambah_obat = tk.Label(page5, text="TAMBAH OBAT", font=("Calibri",20, 'bold'))
label_tambah_obat.place(x=570,y=50)

label_nama_penyakit = tk.Label(page5, text="Nama penyakit:")
label_nama_penyakit.place(x=540, y=150)
entry_penyakit = tk.Entry(page5)
entry_penyakit.place(x=650, y=150)

label_nama_obat = tk.Label(page5, text="Nama obat:")
label_nama_obat.place(x=540, y=175)
entry_obat = tk.Entry(page5)
entry_obat.place(x=650, y=175)

# Membuat gaya khusus untuk tabel
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background="#1D267D", foreground="white", fieldbackground="#1D267D")

# Membuat Treeview untuk menampilkan data obat
tree_obat= ttk.Treeview(page5, style="Treeview")
tree_obat["columns"] = ("Nama penyakit", "Nama obat")
tree_obat.place(x=380, y=295)

# Mengatur lebar kolom pada Treeview
tree_obat.column("#0", width=50)
tree_obat.column("Nama penyakit", width=250)
tree_obat.column("Nama obat", width=250)

# Menampilkan heading kolom
tree_obat.heading("#0", text="No.")
tree_obat.heading("Nama penyakit", text="Nama penyakit")
tree_obat.heading("Nama obat", text="Nama obat")

# Tombol Tambah Obat
button_tambah = tk.Button(page5, text="Tambah", command=tambah_obat)
button_tambah.place(x=625, y=225)

# Tombol Tampilkan Data
button_tampilkan_data = tk.Button(page5, text="Tampilkan Data", bg='green', command=tampilkan_data_obat)
button_tampilkan_data.place(x=613, y=530)

# Menggunakan fungsi tampilkan_data_obat() saat pertama kali menjalankan program
tampilkan_data_obat()

# Tombol Hapus Obat
button_hapus = tk.Button(page5, text="Hapus", bg='red', command=hapus_obat)
button_hapus.place(x=634,y=558)

# Tombol Update Obat
button_update = tk.Button(page5, text="Update", bg='yellow', command=update_obat)
button_update.place(x=627, y=255)

tombol_logout =tk.Button(page5, text = " Back ", font=("calibri",15), activebackground="white", bg='blue', command=lambda: show_frame(page3))
tombol_logout.place(x=1200, y= 600)

# ==================================================== Page 6 ====================================================

# Mengatur Latar Belakang
page6.config(background="white")
bg6=tk.PhotoImage(file="3.png")
page6_bg =tk.Label(page6, image=bg6)
page6_bg.place(x=0, y=0)

# Mengatur tampilan tulisan
page6_teks =tk.Label(page6, text='SIGN IN', font=('calibri', 30, 'bold'), bg = "white" , fg='black')
page6_teks.place(x=615, y=100)

# Fungsi untuk cek login
def cek_login():
    username_user = entry_username1.get()
    password_user = entry_password1.get()
    if username_user == "user" and password_user == "qwert":
        page6.pack_forget()
        show_frame(page7)
             
    else:
        messagebox.showinfo("WARNING"," Username atau password anda salah! ")

# Membuat label dan entry untuk username
label_username1 = tk.Label(master=page6, text="Username:", font=("Argent",15), fg='white', bg= "black")
label_username1.place(x=500, y=250)

entry_username1 = tk.Entry(master=page6, font=('calibri', 15), bg="white")
entry_username1.place(x=620, y=250)

# Membuat label dan entry untuk password
label_password1 = tk.Label(master=page6, text="Password:", font=("Argent", 15), fg='white', bg= "black")
label_password1.place(x=500, y=300)

entry_password1 = tk.Entry(master=page6, font=('calibri', 15), bg="white", show="*")
entry_password1.place(x=620, y=300)

# Membuat button untuk login
button_login2 = tk.Button(master=page6, text=" Login ", font=("Consolas",15), activebackground='blue', command=cek_login) 
button_login2.place(x=630, y=400)

tombol2 =tk.Button(page6, text = " Back ", font=("calibri",15), activebackground="blue", command=lambda: show_frame(page1))
tombol2.place(x=645, y=450)

# ==================================================== Page 7 ====================================================

# Mengatur Latar Belakang
page7.config(background="#FFC948")
bg7= tk.PhotoImage(file="1.png")
page7_bg =tk.Label(page7, image=bg7)
page7_bg.place(x=0, y=0)

# Mengatur tampilan tulisan
page7_teks =tk.Label(page7, text='SELAMAT DATANG DI HALAMAN USER', font=('Durian Days', 30, 'bold'), fg='black', compound="bottom")
page7_teks.place(x=250, y=50)

# Membuat dan Mengatur tombol button
tombol_caripasien =tk.Button(page7, text = ' Cari Data Pasien ', font=('Consolas',15), activebackground='blue', command=lambda: show_frame(page8))
tombol_caripasien.place(x=525, y=350)
tombol_cariobat =tk.Button(page7, text = ' Cari Data Obat ', font=('Consolas',15), activebackground='blue', command=lambda: show_frame(page9))
tombol_cariobat.place(x=535, y=450)

# Mengatur tampilan tulisan
page7_subteks1 = tk.Label(page7, text = ' SILAHKAN PILIH DATA YANG AKAN DI CARI: ', font = ('Consolas', 15, 'bold'),fg= 'black', bg= 'white')
page7_subteks1.place(x=400, y=260)
page7_subteks2 = tk.Label(page7, text = ' atau ', font = ('Calibri', 12),fg= 'black', bg= 'white')
page7_subteks2.place(x=610, y=408)

tombol_logout =tk.Button(page7, text = " Logout ", font=("calibri",15), activebackground="white", bg='white', command=lambda: show_frame(page6))
tombol_logout.place(x=1200, y= 600)

# ==================================================== Page 8 ====================================================

# Mengatur Latar Belakang
page8.config(background='#ADD8E6')
bg8= tk.PhotoImage(file="4.png")
page8_label =tk.Label(page8, image=bg8)
page8_label.place(x=0, y=0)

# Data Pasien
Data_Pasien = [
    {"nama": "Akram Analis", "umur": 25, "jenis_kelamin": "Laki-laki", "alamat": "Kandang Limun", "ruangan": "UGD", "jenis_penyakit": "Maag"},
    {"nama": "Merly Yuni Purnama", "umur": 23, "jenis_kelamin": "Perempuan", "alamat": "Lingkar Barat", "ruangan": "Kamar Operasi", "jenis_penyakit": "Pendarahan"},
    {"nama": "Atika Oktavianti", "umur": 22, "jenis_kelamin": "Perempuan", "alamat": "Sawah Lebar", "ruangan": "Kamar Perawat", "jenis_penyakit": "Sesak Napas"},
    {"nama": "Sinta Ezra Wati Gulo", "umur": 23, "jenis_kelamin": "Perempuan", "alamat": "Merpati", "ruangan": "Klinik Rawat Jalan", "jenis_penyakit": "Cedera Tulang Belakang"},
]

def cari_pasien():
    # Menghapus data pada Treeview sebelum mencari data
    tree1.delete(*tree1.get_children())

    # Mengambil input pencarian dari pengguna
    pencarian = entry_pencarian.get().lower()

    # Melakukan pencarian berdasarkan nama pasien
    hasil_pencarian = []
    for pasien in Data_Pasien:
        if pencarian in pasien["nama"].lower():
            hasil_pencarian.append(pasien)

    # Menampilkan hasil pencarian
    if hasil_pencarian:
        pasien = hasil_pencarian[0]
        tree1.insert("", "end", values=(pasien["nama"], pasien["umur"], pasien["jenis_kelamin"], pasien["alamat"], pasien["ruangan"], pasien["jenis_penyakit"]))
    else:
        messagebox.showinfo("WARNING", "Nama Pasien Tidak Ditemukan!")

def hapus_pasien():
    # Mendapatkan item yang dipilih dari Treeview
    item = tree1.focus()

    if item:
        # Mendapatkan data pasien yang akan dihapus
        pasien = tree1.item(item)
        data_pasien = pasien['values'][0]

        # Mencari indeks data pasien yang akan dihapus
        indeks = None
        for i, data in enumerate(Data_Pasien):
            if data['nama'] == data_pasien:
                indeks = i
                break

        if indeks is not None:
            # Menghapus data pasien dari list
            Data_Pasien.pop(indeks)

            # Menghapus item dari Treeview
            tree1.delete(item)

            messagebox.showinfo("Pemberitahuan", "Data pasien telah dihapus")

            # Mengaktifkan tombol cari setelah data berhasil dihapus
            button_cari.config(state=tk.NORMAL)
    else:
        messagebox.showinfo("WARNING", "Silakan pilih pasien yang akan dihapus")

        # Menonaktifkan tombol cari jika belum ada data yang dihapus
        button_cari.config(state=tk.DISABLED)

# Membuat Treeview untuk menampilkan data pasien
tree1 = ttk.Treeview(page8)
tree1["columns"] = ("Nama", "Umur", "Jenis Kelamin", "Alamat", "Ruangan", "Jenis Penyakit")

# Mengatur lebar kolom pada Treeview
tree1.column("#0", width=50)
tree1.column("Nama", width=150)
tree1.column("Umur", width=50)
tree1.column("Jenis Kelamin", width=100)
tree1.column("Alamat", width=200)
tree1.column("Ruangan", width=100)
tree1.column("Jenis Penyakit", width=150)

# Menampilkan heading kolom
tree1.heading("#0", text="No.")
tree1.heading("Nama", text="Nama")
tree1.heading("Umur", text="Umur")
tree1.heading("Jenis Kelamin", text="Jenis Kelamin")
tree1.heading("Alamat", text="Alamat")
tree1.heading("Ruangan", text="Ruangan")
tree1.heading("Jenis Penyakit", text="Jenis Penyakit")

# Label dan entry pencarian
label_pencarian = tk.Label(page8, text="Nama Pasien", font=("Calibri", 20, 'bold'))
label_pencarian.place(x=570, y=40)

# Entry pencarian
entry_pencarian = tk.Entry(page8)
entry_pencarian.place(x=583, y=120)

# Tombol cari
button_cari = tk.Button(page8, text="Cari", bg='white', command=cari_pasien)
button_cari.place(x=630, y=150)

# Tombol hapus
button_hapus = tk.Button(page8, text="Hapus", bg='red', command=hapus_pasien)
button_hapus.place(x=630, y=450)

# Mengatur tinggi tabel
tree1["height"] = 10

# Membuat scrollbar vertikal
scrollbar = ttk.Scrollbar(page8, orient="vertical", command=tree1.yview)
tree1.configure(yscrollcommand=scrollbar.set)

# Menempatkan Treeview dan scrollbar
tree1.place(x=230, y=200)

tombol3 = tk.Button(page8, text="Back", font=("calibri", 15), activebackground="white", bg='blue', command=lambda: show_frame(page7))
tombol3.place(x=1228, y=603)

# ==================================================== Page 9 ====================================================

# Mengatur Latar Belakang
page9.config(background='#ADD8E6')
bg9= tk.PhotoImage(file="4.png")
page9_label =tk.Label(page9, image=bg9)
page9_label.place(x=0, y=0)

# Data penyakit
Jenis_Penyakit = [
    {"jenis_penyakit": "Maag", "jenis_obat": "Promaag"},
    {"jenis_penyakit": "Pendarahan", "jenis_obat": "Transamin"},
    {"jenis_penyakit": "Sesak Napas", "jenis_obat": "Grafasma"},
    {"jenis_penyakit": "Cedera Tulang Belakang", "jenis_obat": "Nsaid"},
]

def cari_jenis_penyakit():
    # Menghapus data pada Treeview sebelum mencari data
    tree2.delete(*tree2.get_children())

    # Mengambil input pencarian dari pengguna
    pencarian = entry_pencarian.get().lower()

    # Melakukan pencarian berdasarkan jenis penyakit
    hasil_pencarian = []
    for penyakit in Jenis_Penyakit:
        if pencarian in penyakit["jenis_penyakit"].lower():
            hasil_pencarian.append(penyakit)

    # Menampilkan hasil pencarian
    if hasil_pencarian:
        for i, penyakit in enumerate(hasil_pencarian, start=1):
            tree2.insert("", "end", text=str(i), values=(penyakit["jenis_obat"], penyakit["jenis_penyakit"]))
    else:
        messagebox.showinfo("WARNING","Jenis penyakit tidak ditemukan.")

def hapus_obat():
    # Mendapatkan item yang dipilih dari Treeview
    item = tree2.focus()

    if item:
        # Mendapatkan data penyakit yang akan dihapus
        penyakit = tree2.item(item)
        jenis_penyakit = penyakit['values'][1]

        # Mencari indeks data penyakit yang akan dihapus
        indeks = None
        for i, data in enumerate(Jenis_Penyakit):
            if data['jenis_penyakit'] == jenis_penyakit:
                indeks = i
                break

        if indeks is not None:
            # Menghapus data penyakit dari list
            Jenis_Penyakit.pop(indeks)

            # Menghapus item dari Treeview
            tree2.delete(item)
            messagebox.showinfo("Pemberitahuan!","Data telah berhasil dihapus")


            # Mengaktifkan tombol cari setelah data berhasil dihapus
            button_cari.config(state=tk.NORMAL)
    else:
        messagebox.showinfo("WARNING"," Silakan pilih jenis penyakit yang akan dihapus ")

        # Menonaktifkan tombol cari jika belum ada data yang dihapus
        button_cari.config(state=tk.DISABLED)

# Label dan entry Jenis Penyakit
label_pencarian = tk.Label(page9, text="Jenis Obat", font=("Calibri", 20, 'bold'))
label_pencarian.place(x=583, y=40)

# Entry pencarian
entry_pencarian = tk.Entry(page9)
entry_pencarian.place(x=583, y=120)

# Tombol cari
button_cari = tk.Button(page9, text="Cari", command=cari_jenis_penyakit)
button_cari.place(x=630, y=150)

# Tombol hapus
button_hapus = tk.Button(page9, text="Hapus", bg="red", command=hapus_obat)
button_hapus.place(x=630, y=450)

# Membuat Treeview untuk menampilkan data penyakit
tree2 = ttk.Treeview(page9)
tree2["columns"] = ("Jenis Obat", "Jenis Penyakit")
tree2.heading("#0", text="No.")
tree2.heading("Jenis Obat", text="Jenis Obat")
tree2.heading("Jenis Penyakit", text="Jenis Penyakit")
tree2.pack(pady=10)

# Menempatkan Treeview
tree2.place(x=343, y=200, width=610, height=220)

tombol3 = tk.Button(page9, text="Back", font=("calibri", 15), activebackground="white", bg='blue', command=lambda: show_frame(page7))
tombol3.place(x=1230, y=603)

window.mainloop()
