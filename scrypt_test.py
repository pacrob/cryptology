import scrypt

salt = b'aa1f2d3f4d23ac44e9c5a6c3d8f9ee8c'
passwd = b'p@$Sw0rD~7'
key = scrypt.hash(passwd, salt, 2048, 8, 1, 32)
print("Derived key:", key.hex())

# scrypt password hashes are stored like this, fields separated by $
# these use p@ss~123

c = '16384$8$1$kytG1MHY1KU=$afc338d494dc89be40e317788e3cd9166d066709db0e6481f0801bd918710f46'
b = '16384$8$1$5gFGlElztY0=$560f6229356c281a525fad4e2fc4c209bb55c21dec789381335a32bb84888a5a'
a = '32768$8$4$VGhlIHF1aWo=$54d657cec8b3aaca675b407e790bccf1dddb0a23665cd5f994820a736d4b58ba'

