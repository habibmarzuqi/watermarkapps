# File .env

## Apa Itu File .env?

File `.env` adalah sebuah file konfigurasi yang digunakan untuk menyimpan variabel lingkungan (environment variables) yang digunakan oleh aplikasi. File ini biasanya berada di direktori root dari sebuah proyek dan berisi pasangan `KEY=VALUE` untuk setiap variabel lingkungan.

## Fungsi

- **Isolasi Konfigurasi**: Memisahkan konfigurasi dari kode, sehingga kode lebih mudah untuk di-maintain dan di-deploy.
- **Keamanan**: Menyimpan data sensitif seperti kredensial database, API keys, dan lain-lain, sehingga tidak ter-expose di kode sumber.
- **Portabilitas**: Mempermudah proses deploy aplikasi di berbagai lingkungan dengan konfigurasi yang berbeda-beda.

## Maksud dan Tujuan

- **Sederhana**: Formatnya yang sederhana mempermudah pembacaan dan penulisan.
- **Lokal**: Hanya berlaku untuk aplikasi atau proyek di mana file tersebut berada, tidak mempengaruhi sistem secara keseluruhan.
- **Dinamis**: Variabel-variabel dapat diubah tanpa perlu merestart aplikasi.

## Hal-Hal yang Perlu Diketahui

1. **Tidak untuk Komit**: File ini sebaiknya tidak di-commit ke repositori kode sumber, untuk mencegah kebocoran informasi sensitif.
2. **Format**: Setiap baris berisi pasangan `KEY=VALUE`.
3. **Tanpa Spasi**: Tidak boleh ada spasi di sekitar tanda `=`.
4. **Komentar**: Baris yang diawali dengan `#` akan dianggap sebagai komentar.

## Contoh
DB_HOST=localhost   
DB_USER=root   
DB_PASS=secret  
API_KEY=1234567890  


Dengan adanya file `.env`, variabel-variabel tersebut dapat diakses dalam kode melalui fungsi khusus yang disediakan oleh library atau framework yang digunakan.

## Konfigurasi .env
1. Copy template file .env 
`cp .env.example .env`
2. Isi semua variable yang dibutuhkan seperti nama database, password dan lainnya



