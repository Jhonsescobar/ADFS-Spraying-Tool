# ADFS-Spraying-Tool
Advanced Python script to simulate Password Spraying attacks on exposed ADFS endpoints. Includes PoC for University of Edinburgh Case Study.
Python 3.8+License: MITStatus: Active

A proof-of-concept Python script designed to audit Microsoft ADFS endpoints for Brute Force and Password Spraying vulnerabilities.
Overview
This tool simulates a Password Spraying attack against Active Directory Federation Services (ADFS) login pages. It helps security professionals identify if their authentication endpoints are protected against automated credential stuffing attacks.
Key Features:

    ⚡ Fast Execution: Optimized to detect lack of rate limiting quickly.
    🕵️ Silent Mode: Includes random delays and User-Agent rotation to evade basic bot detection.
    🔍 Response Analysis: Uses pattern matching to distinguish between Login Pages and Error Pages.
    📝 Reporting: Generates clear console output for security audits.

Installation

Clone the repository and install the required dependencies:
git clone https://github.com/USERNAME-KAMU/ADFS-Spraying-Tool.gitcd ADFS-Spraying-Toolpip install -r requirements.txt

Usage 
Run the script and provide the target ADFS URL (edit inside the script or modify the code to accept CLI arguments): 
python3 proof_adfs_v2.py

Example Output:
╔══════════════════════════════════════════════════╗
║     ADFS PASSWORD SPRAYING SIMULATION v2.0       ║
╚══════════════════════════════════════════════════╝
[*] Initiating Attack Vector: Password Spraying
[+] admin@ed.ac.uk -> Login PROCESSED (No Explicit Error Msg) - RISKY

Real World Case Study 

This tool has been successfully used to identify a security misconfiguration in a major UK University's infrastructure (edadfed.ed.ac.uk). 

Finding: The ADFS endpoint accepted multiple login attempts without IP blocking.
Evidence: See case_study_ed.md for the full technical report and proof logs. 

⚠️ Disclaimer: This tool is intended for educational purposes and authorized security testing only. Using this tool against targets without permission is illegal. I am not responsible for any misuse of this software. 
🤝 Contributing 

Feel free to submit issues or fork the repository for improvements. 
