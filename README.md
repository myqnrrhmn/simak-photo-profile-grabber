# Students Photo Grabber

Skrip Python ini digunakan untuk mengunduh foto profil mahasiswa berdasarkan program studi dan angkatan mereka. Foto-foto ini diambil dari situs `simak.wastu.digital` dan disimpan secara lokal dalam format `.jpg`.

## Fitur

- Mengunduh foto mahasiswa berdasarkan input **Program Studi** dan **Angkatan**.
- Mengonversi gambar yang memiliki format selain `.jpg` ke format `.jpg`.
- Menyimpan foto dengan nama file yang unik, menggunakan kombinasi angkatan, program studi, dan string acak.
- Proses otomatisasi untuk mengunduh foto dalam jumlah besar.

## Persyaratan

Untuk menjalankan skrip ini, pastikan Anda memiliki:

- Python 3.x atau lebih baru.
- Modul Python yang dibutuhkan:
  - `requests` - untuk melakukan HTTP request dan mengunduh gambar.
  - `Pillow` - untuk memanipulasi dan mengonversi gambar.