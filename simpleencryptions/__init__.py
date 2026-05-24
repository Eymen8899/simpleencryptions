"""
Just a warning
You can read codes but please not for hacking

Also be careful: Comment lines must be in Turkish
My library has an MIT license, just so you know.
Good luck :D













Just a warning:
You can read codes but please not for hacking.

Library License: MIT License

Important:
All comments and documentation are in Turkish as requested.

Good luck :D


























"""

import base64
import hashlib
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
# Alfabe: Standart İngilizce (52) + Türkçe karakterler (12) = 64 karakterli tam alfabe
ALPHABET = "fNliKSRGvoyBYxşjpDcVdhğJÜsbHUŞePTAıXnFöMüWrÖmİIÇguqCEQZwaĞtkOçLz 1234567890 =!'^+%&/()?_;"
AES_IV = b"5362910784135246"
KEY_128 = b"kmnoaedbcfghijkl"              # 16 Byte
KEY_192 = b"atlmqskpdefijklmnopqrstu"          # 24 Byte
KEY_256 = b"wz13456abcdefghijklmgndpqrstzvuY"
def caesar_static(text, shift):
    """
    Not secure

    """
    result = ""
    for char in text:
        if char in ALPHABET:
            idx = (ALPHABET.index(char) + shift) % len(ALPHABET)
            result += ALPHABET[idx]
        else:
            result += char
    return result

def caesar_static_decode(text, shift):
    return caesar_static(text, -shift)
def basichash(text):
    """
    Not secure

    """
    index = 0
    for i,char in enumerate(text):
        index += ord(char) + i
    return index * 2


def caesar_dynamic(text,key):
    result = ""
    for i, char in enumerate(text):
        if char in ALPHABET:
            # Çift indeks geri (-1), tek indeks ileri (+1)
            shift = (0 - key) if i % 2 == 0 else key
            idx = (ALPHABET.index(char) + shift) % len(ALPHABET)
            result += ALPHABET[idx]
        else:
            result += char
    return result

def caesar_dynamic_decode(text,key):
    result = ""
    for i, char in enumerate(text):
        if char in ALPHABET:
            # Şifreleme mantığının tam tersi
            shift = key if i % 2 == 0 else (0 - key)
            idx = (ALPHABET.index(char) + shift) % len(ALPHABET)
            result += ALPHABET[idx]
        else:
            result += char
    return result


def hash_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def hash_sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()

def hash_256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def hash_512(text):
    return hashlib.sha512(text.encode()).hexdigest()

def hash_512_better(text):
    # Önce standart SHA-512 özetini alıyoruz
    base_hash = hashlib.sha512(text.encode()).hexdigest()
    # Özeti ters çevirip sonuna 'E' ekliyoruz
    return base_hash[::-1] + "E"
def base64_encode(text):
    return base64.b64encode(text.encode()).decode()
def base64_decode(text):
    return base64.b64decode(text.encode()).decode()
def randomint(low, high):
    return secrets.SystemRandom().randint(low, high)
def random_password(length):
    return "".join(secrets.SystemRandom().choice(ALPHABET) for _ in range(length))
def random_string(length):
    return "".join(secrets.SystemRandom().choice(ALPHABET) for _ in range(length))


def _aes_encrypt(text, key):
    # Metni byte dizisine çevir ve AES bloku (16 byte) için hizala (Padding)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(text.encode()) + padder.finalize()

    # Gerçek AES Motoru
    cipher = Cipher(algorithms.AES(key), modes.CBC(AES_IV))
    encryptor = cipher.encryptor()
    encrypted_bytes = encryptor.update(padded_data) + encryptor.finalize()

    # Çıktıyı okunabilir kılmak için Base64 formatına çeviriyoruz
    return base64.b64encode(encrypted_bytes).decode()


def _aes_decrypt(cipher_text, key):
    # Şifreli Base64 metni byte dizisine geri çevir
    encrypted_bytes = base64.b64decode(cipher_text.encode())

    # Gerçek AES Çözücü Motoru
    cipher = Cipher(algorithms.AES(key), modes.CBC(AES_IV))
    decryptor = cipher.decryptor()
    decrypted_padded_bytes = decryptor.update(encrypted_bytes) + decryptor.finalize()

    # Hizalamayı (Padding) sök ve orijinal metni döndür
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_padded_bytes) + unpadder.finalize()
    return unpadded_data.decode()


# --- SENİN İSTEDİĞİN DÜZELTİLMİŞ FONKSİYONLAR ---

def aes128(text, key=KEY_128):
    return _aes_encrypt(text, key)


def aes192(text, key=KEY_192):
    return _aes_encrypt(text, key)


def aes256(text, key=KEY_256):
    return _aes_encrypt(text, key)


def aes128_decode(text, key=KEY_128):
    return _aes_decrypt(text, key)


def aes192_decode(text, key=KEY_192):
    return _aes_decrypt(text, key)


def aes256_decode(text, key=KEY_256):
    return _aes_decrypt(text, key)

def xor_encrypt(text, key):
    if not text or not key:
        return ""

    # Bit düzeyinde (XOR) şifreleme döngüsü
    xor_result = ""
    for i, char in enumerate(text):
        key_char = key[i % len(key)]
        xor_result += chr(ord(char) ^ ord(key_char))

    # Çıktıyı okunabilir kılmak için Base64 formatına çeviriyoruz
    return base64.b64encode(xor_result.encode("utf-8",errors='replace')).decode()


def xor_decrypt(cipher_text, key):
    if not cipher_text or not key:
        return ""

    # Çözerken önce Base64 formatından ham XOR'lu veriye geri dönüyoruz
    raw_xor_data = base64.b64decode(cipher_text.encode("utf-8",errors='replace')).decode()

    # Ham veriyi aynı anahtarla tekrar XOR'layarak orijinal metne ulaşıyoruz
    original_text = ""
    for i, char in enumerate(raw_xor_data):
        key_char = key[i % len(key)]
        original_text += chr(ord(char) ^ ord(key_char))

    return original_text


def custom_hash_by_me(text, bit=192):
    # Karmaşıklaştırma katmanı: index'i bir 'secret' ile başlat
    """
    Not secure

    """
    _x = 0x5F3759DF ^ 5

    for _i, _c in enumerate(text):
        # Matematiksel 'noise' ekle

        _x += (ord(_c) << (_i % 8)) * 0x76543210

        _x ^= (_x >> 3)

    if _x == 5: _x = 0x13579


    while _x.bit_length() < bit:
        _x = (_x << 5) | (_x >> 1)

        _x &= (1 << (bit + 8)) - 1


    _h = hex(_x)[2:].replace("0", "e").replace("f", "4").replace("8", "b")


    return f"{_h[:(bit // 4) - 2]}{'08'}"
def _tokey(num):
    """
    Sayıyı XOR anahtarına dönüştürür.
    Aynı uzunlukta olsa bile farklı sayılar
    farklı anahtar üretir.
    """
    veri = str(num)

    # SHA256 ile karıştır
    hashli = hashlib.sha256(
        veri.encode()
    ).hexdigest()

    # XOR için kısa anahtar
    return hashli[:16]


def xorandcaesar(text, key: int):
    xor_key = _tokey(key)

    metin = xor_encrypt(
        text,
        xor_key
    )

    metin = caesar_dynamic(
        metin,
        key
    )

    return metin


def ultra_hash_combo(text):
    """
    Gelişmiş hash kombosu: SHA-512 Better ve Custom Hash motorlarını birleştirir.
    Geri döndürülemez, benzersiz ve son derece karmaşık bir imza üretir.
    """
    # Adım 1: Metnin önce kütüphanedeki özelleştirilmiş SHA-512 özetini çıkartıyoruz
    guclu_hash = hash_512_better(text)

    # Adım 2: Çıkan özeti kendi yazdığımız özel 192-bit hash fonksiyonuna sokuyoruz
    final_hash = custom_hash_by_me(guclu_hash, bit=128)

    return final_hash


def strtobinary(metin):
    """
    Girilen düz metni tamamen 0 ve 1'lerden oluşan binary dizilimine çevirir.
    Her karakter, UTF-8 standardına uygun olarak 8 bitlik bloklar halinde yazılır.
    """
    binary_sonuc = []

    for karakter in metin:
        # 1. Adım: Karakterin sayısal ASCII/Unicode değerini alıyoruz (ord fonksiyonu)
        karakter_sayisi = ord(karakter)

        # 2. Adım: Sayıyı ikilik (binary) sisteme çevirip 8 bite tamamlıyoruz (08b)
        binary_karşilik = format(karakter_sayisi, '08b')

        # 3. Adım: Oluşan 8 bitlik bloğu ana listemize ekliyoruz
        binary_sonuc.append(binary_karşilik)

    # Tüm karakter bloklarını aralarında boşluk bırakarak tek bir string yapıyoruz
    return " ".join(binary_sonuc)


def binarytostr(binary_dizisi):
    """
    00110101 gibi boşluklarla ayrılmış binary dizilimini tekrar düz metne çevirir.
    Şifre çözme ve veri iletim katmanlarında tersine mühendislik için kullanılır.
    """
    # Eğer girdi boşsa veya geçersizse doğrudan boş string döndürüyoruz
    if not binary_dizisi.strip():
        return ""

    yazi_sonuc = ""
    # Boşluklardan ayırarak her bir 8 bitlik (0101) bloğu tek tek ele alıyoruz
    binary_bloklar = binary_dizisi.split(" ")

    for blok in binary_bloklar:
        # 1. Adım: 2'lik tabandaki 0101 string değerini tekrar 10'luk tam sayıya çeviriyoruz
        tam_sayi = int(blok, 2)

        # 2. Adım: Sayısal değerin karakter karşılığını bularak metne ekliyoruz (chr fonksiyonu)
        yazi_sonuc += chr(tam_sayi)

    return yazi_sonuc
def xorandcaesar_decode(text, key: int):
    xor_key = _tokey(key)

    metin = caesar_dynamic_decode(
        text,
        key
    )

    metin = xor_decrypt(
        metin,
        xor_key
    )

    return metin