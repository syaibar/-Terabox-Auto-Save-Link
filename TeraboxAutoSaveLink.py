from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# File dengan daftar link Terabox
LINK_FILE = "links.txt"

# XPath tombol 'Simpan ke Terabox'
SIMPAN_XPATH = '/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]'

# XPath tombol 'Konfirmasi' di pop-up lokasi penyimpanan
KONFIRMASI_XPATH = '/html/body/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div[3]/div/div[3]'

# XPath tombol 'X' / Close di jendela notifikasi berhasil
CLOSE_XPATH = '/html/body/div[1]/div/div/div/div[2]/div/div[5]/div/div[2]/div[1]/img'

# Setup Chrome
options = Options()
options.add_experimental_option("detach", True)  # Agar browser tidak langsung tertutup
driver = webdriver.Chrome(options=options)

# Baca daftar link
try:
    with open(LINK_FILE, "r") as f:
        links = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print(f"❌ File '{LINK_FILE}' tidak ditemukan.")
    driver.quit()
    exit()

# Arahkan ke link pertama untuk login langsung di halaman yang relevan
if links:
    print("🔐 Silakan login terlebih dahulu di halaman pertama link Terabox...")
    driver.get(links[0])
    input("✅ Setelah login dan masuk dashboard, tekan Enter untuk mulai proses...")
else:
    print("❌ Daftar link kosong!")
    driver.quit()
    exit()

# Proses setiap link
for i, url in enumerate(links, 1):
    print(f"\n🔗 Membuka link ke-{i}: {url}")
    try:
        driver.get(url)
        time.sleep(5)  # Tunggu halaman termuat

        # Klik tombol Simpan
        simpan_btn = driver.find_element(By.XPATH, SIMPAN_XPATH)
        simpan_btn.click()
        print("✅ Klik tombol 'Simpan ke Terabox'")
        time.sleep(2)

        # Klik tombol Konfirmasi di jendela penyimpanan
        konfirmasi_btn = driver.find_element(By.XPATH, KONFIRMASI_XPATH)
        konfirmasi_btn.click()
        print("✅ Klik tombol 'Konfirmasi'")
        time.sleep(2)

        # Klik tombol Close (X) di notifikasi 'berhasil disimpan'
        close_btn = driver.find_element(By.XPATH, CLOSE_XPATH)
        close_btn.click()
        print("✅ Klik tombol 'Close'")
        time.sleep(3)

    except Exception as e:
        print(f"❌ Gagal memproses {url}: {e}")

print("\n🎉 Semua link selesai diproses!")
