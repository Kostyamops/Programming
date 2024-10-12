alphabet_len = 26
start_index_higher = 65
start_index_lower = 97
shift = 3

def encrypt_caesar(text) -> str:
    """
        Encrypts plaintext using a Caesar cipher.

        >>> encrypt_caesar("PYTHON")
        'SBWKRQ'
        >>> encrypt_caesar("python")
        'sbwkrq'
        >>> encrypt_caesar("Python3.6")
        'Sbwkrq3.6'
        >>> encrypt_caesar("")
        ''
        """

    code = ""
    for i in range(0, len(text)):
        symbol_code = ord(text[i])
        if start_index_higher <= symbol_code < start_index_higher + alphabet_len:
            symbol_code = (symbol_code - start_index_higher + shift) % alphabet_len + start_index_higher
        if start_index_lower <= symbol_code < start_index_lower + alphabet_len:
            symbol_code = (symbol_code - start_index_lower + shift) % alphabet_len + start_index_lower
        code += chr(symbol_code)
    return code



def decrypt_caesar(code) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """

    text = ""
    for i in range(0, len(code)):
        symbol_code = ord(code[i])
        if start_index_higher <= symbol_code < start_index_higher + alphabet_len:
            symbol_code = (symbol_code - start_index_higher - shift + alphabet_len) % alphabet_len + start_index_higher
        if start_index_lower <= symbol_code < start_index_lower + alphabet_len:
            symbol_code = (symbol_code - start_index_lower - shift + alphabet_len) % alphabet_len + start_index_lower
        text += chr(symbol_code)
    return text


# text = str(input())
# shift = int(input())
#
# #Кодирование сообщения
# print(encrypt_caesar(text, shift))
# #Декодированние закодированного сообщения (обратное действие)
# print(decrypt_caesar(encrypt_caesar(text, shift), shift))