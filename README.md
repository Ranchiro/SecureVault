# 🔐 SecureVault

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Security](https://img.shields.io/badge/Security-AES--256-red.svg)]()

A secure, encrypted password manager built with Python. Features military-grade AES-256 encryption, master password protection, and a secure password generator.

## ✨ Features

- 🔒 **AES-256 Encryption** - Industry-standard encryption for your passwords
- 🔑 **Master Password Protection** - Single password to unlock your vault
- 🎲 **Password Generator** - Create strong, random passwords
- 📊 **Password Strength Checker** - Analyze password security
- 💾 **Local Storage** - Your data never leaves your machine
- 🐍 **Pure Python** - No external dependencies except cryptography

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/Ranchiro/SecureVault.git
cd SecureVault

# Install dependencies
pip install -r requirements.txt
```

## 📖 Usage

### Basic Usage

```python
from vault import SecureVault

# Create and unlock vault
vault = SecureVault()
vault.unlock("your_master_password")

# Add a password
vault.add_password("github", "username", "secure_password")

# Retrieve a password
creds = vault.get_password("github")
print(creds["username"], creds["password"])

# List all services
print(vault.list_services())
```

### Password Generator

```python
from password_generator import PasswordGenerator

gen = PasswordGenerator()

# Generate a secure password
password = gen.generate(length=20)
print(password)  # e.g., "K#9mP@xL2$vNq8Yw!Z"

# Generate a passphrase
phrase = gen.generate_passphrase(word_count=4)
print(phrase)  # e.g., "apple-delta-sierra-echo"

# Check password strength
result = gen.check_strength("MyP@ssw0rd!")
print(result["strength"])  # "strong"
```

## 🔒 Security

- Uses **PBKDF2** with 480,000 iterations for key derivation
- **AES-256** encryption via the Fernet implementation
- Passwords are **never stored in plain text**
- Master password is **never saved** to disk

## 📁 Project Structure

```
SecureVault/
├── vault.py              # Core encryption module
├── password_generator.py # Password generation utility
├── requirements.txt      # Project dependencies
├── LICENSE               # MIT License
└── README.md             # Documentation
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Ruchir Ganatra** - [@Ranchiro](https://github.com/Ranchiro)

---

⭐ Star this repo if you find it useful!
