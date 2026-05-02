import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

def encrypt_file(input_filename, output_filename):
    key = 5
    with open(input_filename, 'r') as f:
        data = f.read()

    cipher_data = ''.join(chr(ord(c) + key) for c in data)

    with open(output_filename, 'w') as f:
        f.write(cipher_data)


def decrypt_file(input_filename, output_filename):
    key = 5
    with open(input_filename, 'r') as f:
        data = f.read()

    plain_data = ''.join(chr(ord(c) - key) for c in data)

    with open(output_filename, 'w') as f:
        f.write(plain_data)


input_filename = "plain_text.txt"
encrypted_filename = "cipher_text.txt"
decrypted_filename = "decoded_cipher_text.txt"

encrypt_file(input_filename, encrypted_filename)
print("Encryption Completed")

decrypt_file(encrypted_filename, decrypted_filename)
print("Decryption Completed")
