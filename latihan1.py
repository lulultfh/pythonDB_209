import tkinter as tk  #impor library tkinter dengan alias tk untuk membuat GUI
from tkinter import * #impor semua modul dari tkinter
import sqlite3 as sql #impor library sqlite3 dengan alias sql untuk mengelola database SQLite

tampilan = tk.Tk() #membuat jendela utama aplikasi, Tk = vactory
tampilan.configure(bg="#FFEEAD") #untuk mengatur background jendela utama 
tampilan.geometry("400x300") #untuk mengatur ukuran jendela utama (ttpi masih bisa dirubah ukurannya)
tampilan.title("Aplikasi Prediksi Prodi Pilihan") #untuk mengatur judul jendela

MTK = tk.DoubleVar() #variable untuk nilai matematika, DoubleVar  untuk tipe data float
BING = tk.DoubleVar() #variable untuk nilai bahasa inggris, DoubleVar  untuk tipe data float
GEO = tk.DoubleVar() #variable untuk nilai geografi, DoubleVar  untuk tipe data float
NAMA = tk.StringVar() #variable untuk menyimpan nama siswa, StringVar untuk tipe data string

#Function untuk memprediksi prodi dari perbandingan nilai
def prodiapanich():
    hasil = "" #variable untuk menyimpan hasil prediksi prodi
    
    #Logika operator untuk menentukan prodi berdasarkan perbandingan dari nilai tertinggi
    if float(MTK.get()) > float(GEO.get()) and float(MTK.get()) > float(BING.get()):
        hasil = "Kedokteran"
    elif float(BING.get()) > float(GEO.get()) and float(BING.get()) > float(MTK.get()):
        hasil = "Bahasa"
    elif float(GEO.get()) > float(MTK.get()) and float(GEO.get()) > float(BING.get()):
        hasil = "Teknik"
    else :
        #Logika operator tambahan berdasarkan perbandingan dari nilai yang sama
        if float(GEO.get()) == float(MTK.get()) and float(GEO.get()) > float(BING.get()):
            hasil = "Teknik atau Kedokteran"
        elif float(GEO.get()) == float(BING.get()) and float(GEO.get()) > float(MTK.get()):
            hasil = "Teknik atau Bahasa"
        elif float(MTK.get()) == float(BING.get()) and float(MTK.get()) > float(GEO.get()):
            hasil = "Kedokteran atau Bahasa"
        elif float(GEO.get()) == float(BING.get()) == float(MTK.get()):
            hasil = "Waw, Keren u bebas masuk apapun"
    
    #Menampilkan hasil prediksi pada saat klik tombol_hasil
    tombol_hasil.config(text=f"Hasil: {hasil}")
    
    #membuat database SQLite
    sql_con = sql.connect('db_prodi/prodi.sqlite')
    
    #membuat table 
    sql_con.execute('''CREATE TABLE IF NOT EXISTS prodi(
                        id INTEGER PRIMARY KEY AUTOINCREMENT, #Kolom id as primary key dan akan terisi otomatis
                        nama TEXT NOT NULL, #kolom untuk menyimpan nama siswa dan tidak boleh kosong
                        matematika REAL NOT NULL, #kolom untuk menyimpan nilai matematika dan tidak boleh kosong
                        geografi REAL NOT NULL, #kolom untuk menyimpan nilai geografi dan tidak boleh kosong
                        inggris REAL NOT NULL, #kolom untuk menyimpan nilai bahasa inggris dan tidak boleh kosong
                        hasil TEXT NOT NULL)''') #kolom untuk menyimpan hasil prediksi prodi dan tidak boleh kosong
    
    #menyimpan data entry ke dalam tabel prodi
    sql_con.execute(f'INSERT INTO prodi(nama, matematika, geografi, inggris, hasil) VALUES ("{NAMA.get().upper().strip()}", {MTK.get()}, {GEO.get()}, {BING.get()}, "{hasil}")')
    
    #menyimpan perubahan atau data baru ke database
    sql_con.commit()
    
    #menutup atau menghentikan koneksi ke database
    sql_con.close()
        
#membuat frame pertama sebagai frame bagi label dan entry
frame1 = Frame(tampilan, bg="#E2E2B6",padx=10, pady=10)
frame1.pack(fill="both", expand=True)

#membuat frame kedua sebagai frame bagi tombol_hasil 
frame2 = Frame(tampilan, bg="#E2E2B6", padx=10, pady=10)
frame2.pack(fill="both", expand=True)

#membuat label dan entry untuk nama siswa
nama_label = Label(frame1, text="Nama Siswa", font=("Inter", 11), fg="#E68369")
nama_label.pack(padx=5,expand=True)
nama_entry = Entry(frame1, textvariable=NAMA)
nama_entry.pack(padx=5, expand=True)

#membuat label dan entry untuk nilai geografi
geo_label = Label(frame1, text="Nilai Geografi", font=("Inter", 11), fg="#E68369")
geo_label.pack(padx=5,expand=True)
geo_entry = Entry(frame1, textvariable=GEO)
geo_entry.pack(padx=5, expand=True)

#membuat label dan entry untuk nilai matematika
mtk_label = Label(frame1, text="Nilai Matematika", font=("Inter", 11), fg="#E68369")
mtk_label.pack(padx=5, expand=True)
mtk_entry = Entry(frame1, textvariable=MTK)
mtk_entry.pack(padx=5, expand=True)

#membuat label dan entry untuk nilai bahasa inggris
bing_label = Label(frame1, text="Nilai Bahasa Inggris", font=("Inter", 11), fg="#E68369")
bing_label.pack(padx=5,  expand=True)
bing_entry = Entry(frame1, textvariable=BING)
bing_entry.pack(padx=5, expand=True)

#membuat tombol_hasil untuk menampilkan hasil prediksi
tombol_hasil = Button(frame2, text="Hasil Prediksi Prodi", font=("Poppins", 12), fg="#E68369", command=prodiapanich)
tombol_hasil.pack( expand = True, pady = 10)

#menjalankan loop utama untuk menampilkan jendela
tampilan.mainloop()