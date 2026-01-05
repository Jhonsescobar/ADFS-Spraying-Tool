Case Study: University of Edinburgh ADFS Exposure

Date: October 2023Target: edadfed.ed.ac.ukVulnerability Type: Lack of Rate Limiting / Brute Force Vector

Executive Summary

During a routine security assessment using the ADFS-Spraying-Tool, I discovered that the Active Directory Federation Services (ADFS) login endpoint of the University of Edinburgh was susceptible to automated credential attacks.

The system processed multiple consecutive login attempts without triggering IP blocking, CAPTCHA, or Smart Lockout mechanisms.
Technical Analysis

    Observation: The endpoint at https://edadfed.ed.ac.uk/adfs/ls/ returns HTTP 200 OK for both valid and invalid login attempts without displaying explicit error messages.
    Impact: An attacker could perform a "Password Spraying" attack (testing one common password against many accounts) to compromise weak user credentials.
    Proof: The simulation script successfully processed 4 sequential login attempts without any throttling.
Recommendation

    Implement Azure AD Smart Lockout policies.
    Enforce CAPTCHA after 3 failed attempts.
    Restrict ADFS access to trusted IP ranges via VPN.

