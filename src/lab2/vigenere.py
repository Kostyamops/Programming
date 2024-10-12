alphabet_len = 26
start_index_higher = 65
start_index_lower = 97


def encrypt_vigenere(text: str, key: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    code = ""
    key_len = len(key)
    for i in range(0, len(text)):
        symbol_code = ord(text[i])
        shift_symbol = key[i % key_len].lower()
        if shift_symbol.isalpha():
            shift = ord(key[i % key_len].lower()) - start_index_lower
        else:
            shift = 0
        #print(text[i], symbol_code)
        if start_index_higher <= symbol_code < start_index_higher + alphabet_len:
            symbol_code = (symbol_code - start_index_higher + shift) % alphabet_len + start_index_higher
        if start_index_lower <= symbol_code < start_index_lower + alphabet_len:
            symbol_code = (symbol_code - start_index_lower + shift) % alphabet_len + start_index_lower
        #print(text[i], symbol_code)
        code += chr(symbol_code)
    return code


def decrypt_vigenere(code: str, key: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    text = ""
    key_len = len(key)
    for i in range(0, len(code)):
        symbol_code = ord(code[i])
        shift_symbol = key[i % key_len].lower()
        if shift_symbol.isalpha():
            shift = ord(key[i % key_len].lower()) - start_index_lower
        else:
            shift = 0
        if start_index_higher <= symbol_code < start_index_higher + alphabet_len:
            symbol_code = (symbol_code - start_index_higher - shift + alphabet_len) % alphabet_len + start_index_higher
        if start_index_lower <= symbol_code < start_index_lower + alphabet_len:
            symbol_code = (symbol_code - start_index_lower - shift + alphabet_len) % alphabet_len + start_index_lower
        text += chr(symbol_code)
    return text

# code = str(input())
# key = str(input())
#
# #Кодирование сообщения
# print(encrypt_vigenere(code, key))
# #Декодированние закодированного сообщения (обратное действие)
# print(decrypt_vigenere(encrypt_vigenere(code, key), key))