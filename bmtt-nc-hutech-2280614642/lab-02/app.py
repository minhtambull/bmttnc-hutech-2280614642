from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher  # Thêm Playfair Cipher

# Initialize Flask app
app = Flask(__name__)

# Instantiate cipher objects
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()  # Khởi tạo đối tượng RailFence Cipher
playfair_cipher = PlayFairCipher()  # Khởi tạo đối tượng PlayFair Cipher

# Route for home page
@app.route("/")
def home():
    return render_template('index.html')

# Route for Caesar cipher page
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Route for Caesar cipher encryption
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# Route for Caesar cipher decryption
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Route for Vigenere cipher page
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

# Route for Vigenere cipher encryption
@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

# Route for Vigenere cipher decryption
@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Route for RailFence cipher page
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')  # Thêm trang RailFence

# Route for RailFence encryption
@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

# Route for RailFence decryption
@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Route for Playfair cipher page
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')  # Thêm trang Playfair

# Route for Playfair encryption
@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

# Route for Playfair decryption
@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

# Main function to run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
