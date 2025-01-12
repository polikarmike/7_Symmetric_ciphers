def encrypt_caesar(k, m):
    """
    Функция для шифрования текста шифром Цезаря.
    :param k: Ключ - целое число
    :param m: Текст для шифрования
    :return: Зашифрованный текст
    """
    return ''.join(chr((ord(char) + k) % 65536) for char in m)


def decrypt_caesar(k, c):
    """
    Функция для дешифрования текста шифром Цезаря.
    :param k: Ключ - целое число
    :param c: Зашифрованный текст
    :return: Дешифрованный текст
    """
    return ''.join(chr((ord(char) - k) % 65536) for char in c)


def caesar_brute_force(ciphertext):
    """
    Функция для восстановления текста, зашифрованного шифром Цезаря, без знания ключа.
    :param ciphertext: Зашифрованный текст
    :return: Наиболее вероятный расшифрованный текст
    """
    freq = {}
    for char in ciphertext:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Находим символ с максимальной частотой
    most_freq_char = max(freq, key=freq.get)

    # Предполагаем, что этот символ - пробел
    space_char_code = ord(' ')
    most_freq_char_code = ord(most_freq_char)

    key_guess = (most_freq_char_code - space_char_code) % 65536

    # Дешифруем с помощью найденного ключа
    return decrypt_caesar(key_guess, ciphertext)


def vigenere_cipher(text, key):
    """
    Функция для шифрования и дешифрования текста шифром Вижинера с использованием XOR.
    :param text: Исходный текст
    :param key: Ключ (строка)
    :return: Зашифрованный или дешифрованный текст
    """
    key_repeated = (key * ((len(text) // len(key)) + 1))[:len(text)]
    return ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, key_repeated))


# Примеры использования:
if __name__ == "__main__":
    # Пример использования шифра Цезаря
    message = "Hello, World!"
    caesar_key = 3
    encrypted_text = encrypt_caesar(caesar_key, message)
    decrypted_text = decrypt_caesar(caesar_key, encrypted_text)
    print("Зашифрованный текст (Цезарь):", encrypted_text)
    print("Дешифрованный текст (Цезарь):", decrypted_text)

    # Пример использования частотного анализа для взлома шифра Цезаря
    encrypted_text = '''To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune,
    Or to take arms against a sea of troubles'''

    recovered_text = caesar_brute_force(encrypted_text)
    print("Восстановленный текст:", recovered_text)

    # Пример использования шифра Вижинера
    vigenere_key = "mysecretkey"
    vernam_encrypted = vigenere_cipher("Hello, World!", vigenere_key)
    vernam_decrypted = vigenere_cipher(vernam_encrypted, vigenere_key)
    print("Зашифрованный текст (Вижинер):", vernam_encrypted)
    print("Дешифрованный текст (Вижинер):", vernam_decrypted)

