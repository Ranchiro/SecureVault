#!/usr/bin/env python3
"""
SecureVault - A Secure Password Manager
Author: Ruchir Ganatra (github.com/Ranchiro)
Description: AES-256 encrypted password manager with master password protection
"""

import os
import json
import base64
import hashlib
import getpass
from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class SecureVault:
    """A secure password vault using AES-256 encryption."""
    
    def __init__(self, vault_file="vault.enc"):
        self.vault_file = vault_file
        self.salt_file = "vault.salt"
        self.fernet = None
        self.data = {}
    
    def _derive_key(self, password: str, salt: bytes) -> bytes:
        """Derive encryption key from password using PBKDF2."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
    
    def _get_salt(self) -> bytes:
        """Get or create salt for key derivation."""
        if os.path.exists(self.salt_file):
            with open(self.salt_file, "rb") as f:
                return f.read()
        salt = os.urandom(16)
        with open(self.salt_file, "wb") as f:
            f.write(salt)
        return salt
    
    def unlock(self, master_password: str) -> bool:
        """Unlock the vault with master password."""
        try:
            salt = self._get_salt()
            key = self._derive_key(master_password, salt)
            self.fernet = Fernet(key)
            
            if os.path.exists(self.vault_file):
                with open(self.vault_file, "rb") as f:
                    encrypted = f.read()
                decrypted = self.fernet.decrypt(encrypted)
                self.data = json.loads(decrypted.decode())
            else:
                self.data = {"passwords": {}, "created": str(datetime.now())}
            return True
        except Exception:
            return False
    
    def save(self):
        """Save encrypted vault to file."""
        if self.fernet:
            encrypted = self.fernet.encrypt(json.dumps(self.data).encode())
            with open(self.vault_file, "wb") as f:
                f.write(encrypted)
    
    def add_password(self, service: str, username: str, password: str):
        """Add a new password entry."""
        self.data["passwords"][service] = {
            "username": username,
            "password": password,
            "added": str(datetime.now())
        }
        self.save()
    
    def get_password(self, service: str) -> dict:
        """Retrieve password for a service."""
        return self.data["passwords"].get(service)
    
    def list_services(self) -> list:
        """List all stored services."""
        return list(self.data["passwords"].keys())
    
    def delete_password(self, service: str) -> bool:
        """Delete a password entry."""
        if service in self.data["passwords"]:
            del self.data["passwords"][service]
            self.save()
            return True
        return False


if __name__ == "__main__":
    print("SecureVault - Encrypted Password Manager")
    print("Use 'from vault import SecureVault' to import")
