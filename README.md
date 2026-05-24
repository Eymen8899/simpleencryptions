# `simpleencryptions`

#### Basic encryption for your mini projects!

## Installation
```bash
pip install simpleencryptions
```
## Usage

```python
import simpleencryptions as sc

# Example: AES-256 Encryption
encrypted = sc.aes256("Hello World")
print(encrypted)
```
## Available Features

`simpleencryptions` offers a wide variety of tools to handle your security and utility needs:

### **Encryption & Decryption**
* **AES (128, 192, 256):** Standard symmetric encryption.
* **XOR:** Lightweight, bit-level encryption.
* **Caesar Cipher:** Static and Dynamic (shifting) variations.


* **Hashing:**
* **Standard:** MD5, SHA1, SHA256, SHA512.
* **Custom:** `custom_hash_by_me` (Eymen's special hashing algorithm) and `basichash`.


* **Utilities:**
* **Base64:** Quick encoding and decoding.
* **Random Generators:** Cryptographically secure random integers, strings, and passwords.



## License

This project is licensed under the MIT License.

## Changelog
Version 0.1.0: 
- First version.

Version 0.1.1:
- Improved security and performance
- Added new parameters
- Minor improvements and fixes

Version 0.1.2:
- Better readme.md
- New combo