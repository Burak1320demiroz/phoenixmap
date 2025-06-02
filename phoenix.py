#!/usr/bin/env python3
import os
import subprocess

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'

class HTTPAnalyzer:
    def __init__(self):
        self.webdriver_choice = "chrome"  # Varsayılan Chrome
    def print_banner(self):
        """Araç banner'ını yazdır"""
        banner = f"""
{Colors.CYAN}
██████╗ ██╗  ██╗ ██████╗ ███████╗███╗   ██╗██╗██╗  ██╗
██╔══██╗██║  ██║██╔═══██╗██╔════╝████╗  ██║██║╚██╗██╔╝
██████╔╝███████║██║   ██║█████╗  ██╔██╗ ██║██║ ╚███╔╝ 
██╔═══╝ ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║██║ ██╔██╗ 
██║     ██║  ██║╚██████╔╝███████╗██║ ╚████║██║██╔╝ ██╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
                                                        
{Colors.BOLD}Phoenix Security Tool v0.1{Colors.END}
{Colors.YELLOW}Web Güvenlik Analiz ve Test Aracı{Colors.END}
{Colors.GREEN}...{Colors.END}
{Colors.CYAN}{'='*50}{Colors.END}
        """
        print(banner)
    
    def show_menu(self):
        menu = f"""
{Colors.BOLD}ANA MENÜ{Colors.END}
{Colors.GREEN}1.{Colors.END} XSS
{Colors.GREEN}2.{Colors.END} Çıkış
{Colors.GREEN}3.{Colors.END} Ayarlar

{Colors.CYAN}Seçiminizi yapın:{Colors.END} """
        return input(menu)
    
    def xss_panel(self):
        print(f"\n{Colors.BOLD}XSS PANELİ{Colors.END}")
        print(f"{Colors.CYAN}{'='*20}{Colors.END}")
        
        xss_menu = f"""
{Colors.GREEN}1.{Colors.END} Reflected XSS into HTML context with nothing encoded

{Colors.CYAN}Seçiminizi yapın:{Colors.END} """
        
        xss_choice = input(xss_menu)
        
        if xss_choice == '1':
            self.reflected_XSS_into_HTML_context_with_nothing_encoded()
        else:
            print(f"{Colors.YELLOW}Geçersiz seçim.{Colors.END}")
    
    def reflected_XSS_into_HTML_context_with_nothing_encoded(self):
        try:
            script_path = os.path.join("XSS", "reflected_XSS_into_HTML_context_with_nothing_encoded.py")
            subprocess.run(["python3", script_path])
        except FileNotFoundError:
            print(f"{Colors.YELLOW}Dosya bulunamadı: {script_path}{Colors.END}")
        except Exception as e:
            print(f"{Colors.YELLOW}Hata: {e}{Colors.END}")
    
    def webdriver_secimi(self):
        print(f"\n{Colors.BOLD}WEBDRIVER SEÇİMİ{Colors.END}")
        print(f"{Colors.CYAN}{'='*20}{Colors.END}")
        print(f"{Colors.YELLOW}Şu anda seçili: {self.webdriver_choice.title()}{Colors.END}\n")
        
        webdriver_menu = f"""
{Colors.GREEN}1.{Colors.END} Opera
{Colors.GREEN}2.{Colors.END} Chrome

{Colors.CYAN}Seçiminizi yapın:{Colors.END} """
        
        webdriver_choice = input(webdriver_menu)
        
        if webdriver_choice == '1':
            self.webdriver_choice = "opera"
            print(f"{Colors.GREEN}Opera WebDriver seçildi.{Colors.END}")
            self.update_webdriver_config()
        elif webdriver_choice == '2':
            self.webdriver_choice = "chrome"
            print(f"{Colors.GREEN}Chrome WebDriver seçildi.{Colors.END}")
            self.update_webdriver_config()
        else:
            print(f"{Colors.YELLOW}Geçersiz seçim.{Colors.END}")
    
    def update_webdriver_config(self):
        """WebDriver ayarını reflected_XSS dosyasında güncelle"""
        
        xss_file_path = os.path.join("XSS", "reflected_XSS_into_HTML_context_with_nothing_encoded.py")
        
        if os.path.exists(xss_file_path):
            try:
                # Dosyayı oku
                with open(xss_file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # WebDriver satırını güncelle
                if self.webdriver_choice == "opera":
                    new_line = "driver = webdriver.Opera()"
                else:  # chrome
                    new_line = "driver = webdriver.Chrome()"
                
                # Eski satırı yeni satırla değiştir
                import re
                pattern = r'driver = webdriver\.(Chrome|Opera)\(\)'
                updated_content = re.sub(pattern, new_line, content)
                
                # Dosyayı güncelle
                with open(xss_file_path, 'w', encoding='utf-8') as file:
                    file.write(updated_content)
                
                print(f"{Colors.GREEN}WebDriver ayarı güncellendi: {xss_file_path}{Colors.END}")
                
            except Exception as e:
                print(f"{Colors.YELLOW}Ayar güncellenirken hata: {e}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}XSS dosyası bulunamadı, ayar sadece bellekte saklandı.{Colors.END}")
    
    def run(self):
        self.print_banner()
        while True:
            try:
                choice = self.show_menu()
                if choice == '1':
                    self.xss_panel()
                elif choice == '2':
                    print(f"{Colors.CYAN}Çıkış yapılıyor...{Colors.END}")
                    break
                else:
                    print(f"{Colors.YELLOW}Geçersiz seçim.{Colors.END}")
            except KeyboardInterrupt:
                print(f"\n{Colors.CYAN}Çıkış yapılıyor...{Colors.END}")
                break

if __name__ == "__main__":
    analyzer = HTTPAnalyzer()
    analyzer.run()