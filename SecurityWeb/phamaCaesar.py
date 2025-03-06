import string

def caesar_decrypt(ciphertext, shift):
    alphabet = string.ascii_uppercase
    decrypted_text = ''

    for char in ciphertext:
        if char in alphabet:
            new_index = (alphabet.index(char) - shift) % 26
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char

    return decrypted_text

ciphertext = "CSYEVIXIVQMREXIH"

# Thử in từng kết quả để kiểm tra
for k in range(1, 26):
    print(f"k = {k}: {caesar_decrypt(ciphertext, k)}")
