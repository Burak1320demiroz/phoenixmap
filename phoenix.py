#!/usr/bin/env python3

"""
phoenixmap
Copyright (c) 2025 Burak Demiröz

This source code is licensed under the MIT License.
See the LICENSE file for details.
"""

import os
import subprocess

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'

class HTTPAnalyzer:
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

{Colors.CYAN}Seçiminizi yapın:{Colors.END} """
        return input(menu)
    
    def xss_panel(self):
        print(f"\n{Colors.BOLD}XSS PANELİ{Colors.END}")
        print(f"{Colors.CYAN}{'='*20}{Colors.END}")
        
        xss_menu = f"""
{Colors.GREEN}1.{Colors.END} Reflected XSS into HTML context with nothing encoded
{Colors.GREEN}2.{Colors.END} Stored XSS into HTML context with nothing encoded

{Colors.CYAN}Seçiminizi yapın:{Colors.END} """
        
        xss_choice = input(xss_menu)
        
        if xss_choice == '1':
            self.reflected_XSS_into_HTML_context_with_nothing_encoded()
        elif xss_choice == '2':
            self.stored_XSS_into_HTML_context_with_nothing_encoded()
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
    
    def stored_XSS_into_HTML_context_with_nothing_encoded(self):
        try:
            script_path = os.path.join("XSS", "stored_XSS_into_HTML_context_with_nothing_encoded.py")
            subprocess.run(["python3", script_path])
        except FileNotFoundError:
            print(f"{Colors.YELLOW}Dosya bulunamadı: {script_path}{Colors.END}")
        except Exception as e:
            print(f"{Colors.YELLOW}Hata: {e}{Colors.END}")
    
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