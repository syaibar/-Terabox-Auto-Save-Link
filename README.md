# 📦 Terabox Auto Save Link

**Terabox Auto Save Link** adalah program Python otomatis berbasis Selenium untuk:

- Membuka link publik Terabox
- Login ke akun Terabox kamu
- Menyimpan file ke akun kamu secara otomatis dengan klik tombol **"Simpan ke Terabox"**

---

## 📁 Fitur

✅ Baca banyak link dari file `links.txt`  
✅ Otomatis buka dan simpan ke akun Terabox  
✅ Bisa digunakan untuk koleksi besar file publik  
✅ Anti ribet! Login manual 1x, lanjut auto!

---

## 🧰 Syarat & Instalasi

1. **Python 3.x**  
2. **Google Chrome**  
3. **ChromeDriver** (harus cocok dengan versi Chrome kamu):  
   🔗 [Download ChromeDriver](https://chromedriver.chromium.org/downloads)

4. **Install dependency dengan pip:**

```bash
pip install selenium
```

---

## 📦 Struktur Folder

```
terabox-auto-save/
│
├── TeraboxAutoSaveLink.py             # file utama program
├── chromedriver.exe                   # taruh di sini (khusus Windows)
└── links.txt                          # daftar link publik Terabox
```

---

## 📝 Isi `links.txt`

Buat file `links.txt` dan masukkan semua link Terabox (satu per baris):

```
https://1024terabox.com/s/12hh8rIDoB8khXWW7vfD4AQ
https://1024terabox.com/s/1pOGfWg7r_Xd3Af-lI1-v6g
https://1024terabox.com/s/13DK5tXsSfJxo_-8S4S7XHA
```

---

## 🚀 Cara Menjalankan

```bash
python TeraboxAutoSaveLink.py
```

1. Program akan membuka browser dan minta kamu **login ke akun Terabox**
2. Setelah berhasil login, tekan **Enter** di terminal
3. Program akan memproses semua link dan menyimpannya otomatis ke akun kamu

---

## 💡 Tips

- Jangan tutup browser saat proses berjalan
- Pastikan link publik masih aktif
- Cek ulang kalau ada yang gagal (mungkin tombol tidak muncul)

---

## 🤝 Kontribusi

Pull request sangat dipersilakan!  
Jika kamu menemukan bug atau ide perbaikan, silakan buat issue atau PR ya 😄

---

## 📜 Lisensi

MIT License – bebas dipakai, diedit, dikembangkan.
