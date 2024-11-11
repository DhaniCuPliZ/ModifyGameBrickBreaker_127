import tkinter as tk
from tkinter import messagebox

def hasil_prediksi(): #menghitung hasil prediksi
    try: #Memulai blok pengecekan untuk menangani kesalahan input.
        
        for entry in entries: #Mengulangi setiap kotak input dalam daftar entries
            nilai = int(entry.get()) #Mengambil nilai dari input dan merubahnya menjadi integer
            if not (0 <= nilai <= 100): #Memeriksa apakah nilai bukan dari 0-100.
                raise ValueError("Nilai Harus Antara 0 dan 100.") # Menampilkan ValueError jika nilai bukan dari 0-100.
       
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi", fg="#006600") #Tampilkan text jika semua input valid dengan warna hijau

    except ValueError:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.") #Menampilkan valueerror jika input tidak valid

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan") #Menetapkan judul tampilan.
root.geometry("500x600") #Mengatur ukuran tampilan menjadi 500x600 piksel.
root.configure(bg="#f0f0f0") #Memberikan warna latar belakang tampilan abu-abu muda


judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white") #Membuat label judul_label sebagai judul aplikasi dengan teks "Aplikasi Prediksi Prodi Pilihan" dengan font arial ukuran 16 dan dicetak tebal dengan warna background hijau muda dan teks berwarna putih
judul_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10) #menempatkan label di baris pertama (row=0) dan mengambil dua kolom (columnspan=2).

# Menyimpan input nilai ke dalam daftar entries
entries = []
for i in range(10): #Mengulangi 10 kali untuk membuat 10 label dan 10 kotak input.
    # Label untuk mata pelajaran
    mata_pelajaran_label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:", font=("Arial", 10), bg="#f0f0f0") #Membuat label mata_pelajaran_label untuk setiap mata pelajaran dengan teks "Nilai Mata Pelajaran X:" dengan fon arial ukuran 10 dan warna background abu abu muda
    mata_pelajaran_label.grid(row=i+1, column=0, sticky="e", padx=10, pady=5) #Menempatkan label di sebelah kiri setiap baris, dimulai dari row=i+1, di kolom 0, dan rata kanan (sticky="e").
    
    # Entry untuk input nilai
    input_value = tk.Entry(root, bg="#e0f7fa", fg="#004d40", font=("Arial", 10)) #Membuat kotak input input_value untuk setiap mata pelajaran, dengan latar belakang biru muda dan teks hijau gelap dan font arial ukuran 10.
    input_value.grid(row=i+1, column=1, padx=10, pady=5) #menempatkan kotak input input_value pada baris i+1 di kolom 1 dengan padx 10 pady 5 
    entries.append(input_value) #menambahkan input_value ke dalam daftar entries, yang menyimpan semua kotak input ini untuk diakses 

# Tombol untuk hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, bg="#2196F3", fg="white", font=("Arial", 12, "bold")) #Membuat tombol prediksi_button dengan teks "Hasil Prediksi" yang menjalankan hasil_prediksi() saat diklik. Warna latar tombol adalah biru, dengan teks putih dan ukuran font 12, tebal.
prediksi_button.grid(row=11, column=0, columnspan=2, pady=20) #Menempatkan tombol di baris 11 dan mengambil dua kolom.

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333333") #hasil_label akan muncul dengan teks kosong di awal, font Arial berukuran 12, latar belakang abu-abu muda, dan teks berwarna abu-abu gelap
hasil_label.grid(row=12, column=0, columnspan=2, pady=10) #Menempatkan label di baris 12 dan mengambil dua kolom.


root.mainloop() # Menjalankan aplikasi

