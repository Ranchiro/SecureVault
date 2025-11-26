#!/usr/bin/env python3
"""
Secure Password Generator
Author: Ruchir Ganatra (github.com/Ranchiro)
Description: Cryptographically secure password generator with customizable options
"""

import secrets
import string
from typing import Optional


class PasswordGenerator:
    """Generate cryptographically secure passwords."""
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate(
        self,
        length: int = 16,
        use_lowercase: bool = True,
        use_uppercase: bool = True,
        use_digits: bool = True,
        use_symbols: bool = True,
        exclude_chars: str = ""
    ) -> str:
        """Generate a secure random password."""
        
        charset = ""
        if use_lowercase:
            charset += self.lowercase
        if use_uppercase:
            charset += self.uppercase
        if use_digits:
            charset += self.digits
        if use_symbols:
            charset += self.symbols
        
        # Remove excluded characters
        for char in exclude_chars:
            charset = charset.replace(char, "")
        
        if not charset:
            raise ValueError("No characters available for password generation")
        
        # Use secrets module for cryptographic security
        password = ''.join(secrets.choice(charset) for _ in range(length))
        return password
    
    def generate_passphrase(self, word_count: int = 4, separator: str = "-") -> str:
        """Generate a memorable passphrase."""
        words = [
            "apple", "banana", "cherry", "delta", "eagle", "falcon",
            "gamma", "hotel", "india", "juliet", "kilo", "lima",
            "mango", "november", "oscar", "papa", "quebec", "romeo",
            "sierra", "tango", "ultra", "victor", "whiskey", "xray",
            "yankee", "zulu", "alpha", "bravo", "charlie", "echo"
        ]
        selected = [secrets.choice(words) for _ in range(word_count)]
        return separator.join(selected)
    
    def check_strength(self, password: str) -> dict:
        """Analyze password strength."""
        score = 0
        feedback = []
        
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Password should be at least 8 characters")
        
        if len(password) >= 12:
            score += 1
        if len(password) >= 16:
            score += 1
        
        if any(c in self.lowercase for c in password):
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if any(c in self.uppercase for c in password):
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if any(c in self.digits for c in password):
            score += 1
        else:
            feedback.append("Add numbers")
        
        if any(c in self.symbols for c in password):
            score += 1
        else:
            feedback.append("Add special characters")
        
        strength = "weak"
        if score >= 5:
            strength = "medium"
        if score >= 7:
            strength = "strong"
        
        return {
            "score": score,
            "max_score": 7,
            "strength": strength,
            "feedback": feedback
        }


if __name__ == "__main__":
    gen = PasswordGenerator()
    print("Generated Password:", gen.generate(16))
    print("Generated Passphrase:", gen.generate_passphrase())
