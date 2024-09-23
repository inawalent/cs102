def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    k = 0

    for i in plaintext:
        if i.isalpha():
            if i.isupper():
                ciphertext += chr((ord(i) + ord(keyword[k%len(keyword)]) - 2*ord('A')) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(i) + ord(keyword[k%len(keyword)]) - 2*ord('a')) % 26 + ord('a'))
        else:
            ciphertext += i

        k += 1

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    k = 0

    for i in ciphertext:
        if i.isalpha():
            if i.isupper():
                plaintext += chr((ord(i) - ord(keyword[k%len(keyword)])) % 26 + ord('A'))
            else:
                plaintext += chr((ord(i) - ord(keyword[k%len(keyword)])) % 26 + ord('a'))
        else:
            plaintext += i

        k += 1

    return plaintext