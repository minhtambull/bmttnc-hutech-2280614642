class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # Create an empty list for rails
        rails = [[] for _ in range(num_rails)]
        
        rail_index = 0
        direction = 1  # 1 means down, -1 means up
        
        # Iterate through the plaintext and assign each character to the appropriate rail
        for char in plain_text:
            rails[rail_index].append(char)

            # Change direction at the top or bottom rail
            if rail_index == 0:
                direction = 1  # Going down
            elif rail_index == num_rails - 1:
                direction = -1  # Going up

            rail_index += direction
        
        # Join all the rails to form the ciphertext
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Calculate the lengths of each rail in the ciphertext
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        # Calculate the number of characters in each rail
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1

            # Change direction at the top or bottom rail
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        # Fill the rails with the characters from the cipher text
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # Decrypt the cipher by reading characters from the rails
        plain_text = []
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            plain_text.append(rails[rail_index][0])  # Take the first character from the current rail
            rails[rail_index] = rails[rail_index][1:]  # Remove the used character from the rail

            # Change direction at the top or bottom rail
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        # Return the decrypted plain text as a string
        return ''.join(plain_text)
