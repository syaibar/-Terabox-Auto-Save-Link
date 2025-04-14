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
└── links.txt                           # daftar link publik Terabox
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

## 🧠 Isi `TeraboxAutoSaveLink.py`

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# File dengan daftar link Terabox
LINK_FILE = "links.txt"

# XPath tombol 'Simpan ke Terabox'
SIMPAN_XPATH = '/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]'

# Setup Chrome
options = Options()
options.add_experimental_option("detach", True)  # biar tidak langsung tutup
driver = webdriver.Chrome(options=options)

# Buka link login Terabox dulu (biar kamu login manual)
print("🔐 Silakan login dulu ke akun Terabox...")
driver.get("https://www.terabox.com")
input("✅ Setelah login dan masuk ke dashboard, tekan Enter untuk melanjutkan...")

# Baca semua link dari file
with open(LINK_FILE, "r") as f:
    links = [line.strip() for line in f if line.strip()]

# Proses setiap link
for i, url in enumerate(links, 1):
    print(f"\n🔗 Membuka link ke-{i}: {url}")
    try:
        driver.get(url)
        time.sleep(5)  # Tunggu elemen muncul

        # Klik tombol 'Simpan ke Terabox'
        simpan_btn = driver.find_element(By.XPATH, SIMPAN_XPATH)
        simpan_btn.click()
        print("✅ Disimpan ke Terabox")
        time.sleep(3)  # Tunggu proses simpan selesai
    except Exception as e:
        print(f"❌ Gagal memproses {url}: {e}")

print("\n🎉 Selesai semua!")
```

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
