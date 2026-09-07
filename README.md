# 🔐 Advanced Password Security Analyzer

A cybersecurity project designed to analyze password security through
password strength evaluation, entropy estimation, cryptographic hashing,
secure salting, Argon2id password hashing, and controlled dictionary
attack analysis.

> ⚠️ This project is intended for educational purposes and authorized
> cybersecurity testing only.

---

## 📌 Project Overview

The **Advanced Password Security Analyzer** is a command-line
cybersecurity application developed in Python.

The project demonstrates how passwords can be analyzed, hashed,
salted, and evaluated against common password-cracking techniques.

It combines defensive password-security techniques with a controlled
laboratory demonstration of dictionary-based password recovery.

---

## 🚀 Key Features

- 🔎 Password strength analysis
- 🚨 Common password detection
- 📊 Password security scoring
- 🧮 Password entropy estimation
- 🛡️ Crack-resistance classification
- 🔐 SHA-256 hashing demonstration
- 🧂 Cryptographically secure random salting
- 🔒 Argon2id secure password hashing
- ✅ Password hash verification
- ❌ Wrong-password rejection testing
- 🧪 Automated security testing with Pytest
- 📄 JSON security report generation
- 🧰 Controlled dictionary attack demonstration
- ⚔️ John the Ripper integration
- 💻 Professional command-line interface

---

# 🏗️ Project Architecture

```text
Password-Security-Analyzer/
│
├── src/
│   ├── main.py
│   ├── hash_engine.py
│   ├── salt_engine.py
│   ├── password_analyzer.py
│   ├── entropy_analyzer.py
│   ├── argon2_engine.py
│   └── report_generator.py
│
├── tests/
│   └── test_password_analyzer.py
│
├── results/
│   ├── test_hash.txt
│   ├── test_wordlist.txt
│   ├── john_hash.txt
│   └── security_report.json
│
├── screenshots/
│
├── documentation/
│
├── README.md
├── requirements.txt
└── .gitignore# Advanced Password Security Analyzer

A cybersecurity project for analyzing password strength, entropy,
hashing, salting, and controlled password-cracking resistance.

## Features

- Password strength analysis
- Common password detection
- Security scoring
- Password entropy calculation
- Crack-resistance classification
- SHA-256 hashing
- Cryptographically secure random salting
- Salted SHA-256 generation
- Automated security tests
- JSON security report generation
- Controlled dictionary-attack demonstration
- Professional CLI interface

## Project Architecture

```text
Password-Security-Analyzer/
├── src/
│   ├── main.py
│   ├── hash_engine.py
│   ├── salt_engine.py
│   ├── password_analyzer.py
│   ├── entropy_analyzer.py
│   └── report_generator.py
├── tests/
├── results/
├── screenshots/
├── documentation/
├── README.md
└── requirements.txt
