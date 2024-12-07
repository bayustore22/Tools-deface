# T-DEF - TOOLS DEFACE

## Deskripsi

**T-DEF** adalah tools berbasis Python yang dirancang untuk melakukan deface website dengan efisiensi dan kemudahan. Dikembangkan oleh **Wanz Xploit**, tools ini menawarkan dua mode operasi utama:

1. **Deface Tunggal**: Mengunggah file script ke satu target secara langsung.
2. **Deface Multi**: Mengunggah file script ke banyak target sekaligus, yang tercantum di file `target.txt`.

Tools ini dilengkapi dengan tampilan menarik, banner dinamis, efek loading, dan tabel laporan hasil deface.

---

## Fitur Utama

- **Validasi URL**: Memastikan URL target diawali dengan `http://` atau `https://`.
- **Pengecekan File Otomatis**: Memverifikasi keberadaan file HTML yang akan diunggah.
- **Hapus Duplikat**: Di mode multi, tools secara otomatis menghapus target duplikat dari daftar.
- **Animasi Loading**: Memberikan pengalaman pengguna yang lebih interaktif.
- **Tabel Hasil**: Menampilkan laporan status upload untuk setiap target (berhasil/gagal).
- **IP Address Lokal**: Ditampilkan untuk membantu identifikasi jaringan.

---

## Cara Instalasi di Termux

Ikuti langkah-langkah berikut untuk menginstal dan menggunakan tools ini di Termux:

1. **Perbarui dan Tingkatkan Paket Termux**:
   ```bash
   pkg update && pkg upgrade
   ```

2. **Pasang Git dan Python**:
   ```bash
   pkg install git python -y
   ```

3. **Clone Repository Tools Deface**:
   ```bash
   git clone https://github.com/wanzxploit/tools-deface
   ```

4. **Pindah ke Direktori Tools**:
   ```bash
   cd tools-deface
   ```

5. **Instal Dependensi Python**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Persiapkan File**:
   - **File `target.txt`**:
     Buat file `target.txt` untuk mode multi dengan format daftar URL (satu URL per baris). File ini harus berada di dalam direktori tools.
   - **File Script HTML**:
     Letakkan file script HTML yang akan diunggah (contoh: `deface.html`) di direktori yang sama dengan tools. Nama file harus sesuai dengan input yang akan dimasukkan saat menjalankan tools.

---

## Panduan Penggunaan

1. **Jalankan Tools**:
   ```bash
   python dev.py
   ```

2. **Pilih Mode Operasi**:
   - Ketik **1** untuk Deface Tunggal.
   - Ketik **2** untuk Deface Multi.

3. **Masukkan Input**:
   - Untuk mode tunggal:
     - Masukkan nama file HTML (contoh: `deface.html`).
     - Masukkan URL target.
   - Untuk mode multi:
     - Pastikan daftar URL target telah tercantum di `target.txt`.
     - Masukkan nama file HTML yang akan diunggah.

4. **Tinjau Hasil**:
   Tools akan menampilkan tabel laporan hasil deface yang mencakup status setiap target (berhasil/gagal).

---

## Penjelasan Sistem Kerja

1. **Deface Tunggal**:
   - Memvalidasi URL yang dimasukkan.
   - Mengecek keberadaan file HTML.
   - Mengunggah file ke target dan memberikan laporan status.

2. **Deface Multi**:
   - Membaca daftar URL dari file `target.txt`.
   - Menghapus URL duplikat secara otomatis.
   - Mengunggah file ke setiap target dan mencatat hasilnya.

3. **Tabel Hasil**:
   - Menampilkan laporan status upload setiap URL dengan format rapi (berhasil/gagal).

---

## Peringatan Penting

- **Penggunaan yang Bertanggung Jawab**:
  Tools ini dirancang untuk tujuan edukasi. Penyalahgunaan tools ini adalah tanggung jawab pengguna sepenuhnya.
- **Backup Data**:
  Jika Anda memiliki akses resmi ke target, lakukan backup data sebelum menggunakan tools ini.
- **Legalitas**:
  Penggunaan tools ini untuk menyerang tanpa izin adalah tindakan ilegal dan melanggar hukum.

---

## Kredit dan Kontak

Dikembangkan oleh **Wanz Xploit**.

- **Instagram**: [reyzroam](https://www.instagram.com/reyzroam/)
- **YouTube**: [Wanz Xploit](https://www.youtube.com/c/wanzxploit/)
- **GitHub**: [wanzxploit](https://github.com/wanzxploit)

---

## Lisensi

Tools ini dirilis di bawah **MIT License**. Anda bebas menggunakannya untuk kebutuhan edukasi, namun tetap patuhi aturan dan hukum yang berlaku.

