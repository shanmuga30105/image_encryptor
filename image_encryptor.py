from cryptography.fernet import Fernet

# Replace with the actual key you used for encryption
key = b'your-secure-key-goes-here'
cipher = Fernet(key)

# Step 1: Read the encrypted image
with open("image_encrypted.enc", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# Step 2: Decrypt it
decrypted_data = cipher.decrypt(encrypted_data)

# Step 3: Save the decrypted image
with open("image_decrypted.jpg", "wb") as decrypted_image:
    decrypted_image.write(decrypted_data)


