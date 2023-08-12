import secrets
import pyscrypt


password_msg = input("Enter password, then message, separated by a space: ")
password_msg_list = password_msg.split()
password = bytes(password_msg_list[0], encoding='utf8')
msg = bytes(password_msg_list[1], encoding='utf8')

random_128_bit_salt = secrets.token_bytes(128)

# password - a password
# salt - a cryptographic salt
# N - general work factor
# r - memory cost
# p - computation cost (parallelization factor)
# dkLen - the output length (in bytes) to return
scrypt_512_bit_key = pyscrypt.hash(
    password=password, salt=random_128_bit_salt, N=2048, r=16, p=1, dkLen=512
)

print(scrypt_512_bit_key)