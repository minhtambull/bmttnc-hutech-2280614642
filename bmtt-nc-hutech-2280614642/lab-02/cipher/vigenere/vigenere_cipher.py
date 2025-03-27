class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0

        for char in plain_text:
            if char.isalpha():  # Nếu ký tự là chữ cái
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')  # Tính toán dịch chuyển từ khóa
                
                if char.isupper():  # Nếu ký tự là chữ hoa
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:  # Nếu ký tự là chữ thường
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))

                key_index += 1  # Di chuyển đến ký tự tiếp theo của key
            else:
                encrypted_text += char  # Nếu không phải chữ cái, giữ nguyên ký tự

        return encrypted_text

    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        key_index = 0

        for char in encrypted_text:
            if char.isalpha():  # Nếu ký tự là chữ cái
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')  # Tính toán dịch chuyển từ khóa
                
                if char.isupper():  # Nếu ký tự là chữ hoa
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:  # Nếu ký tự là chữ thường
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))

                key_index += 1  # Di chuyển đến ký tự tiếp theo của key
            else:
                decrypted_text += char  # Nếu không phải chữ cái, giữ nguyên ký tự

        return decrypted_text