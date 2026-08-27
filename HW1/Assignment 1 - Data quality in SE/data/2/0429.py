from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import os
import time

kB = 1024 # 1kB
with open('small_file.txt', 'wb') as f:
    f.write(os.urandom(kB))

mB = 10485760 # 1GB
with open('large_file.txt', 'wb') as f:
    f.write(os.urandom(mB))

Begin = time.time()
key = DSA.generate(2048)
with open("public_key.pem", "wb") as f:
    f.write(key.publickey().export_key())
    f.close()
End = time.time()
print("Key Generation Time: ", End-Begin)

def DSA_2048(filename,key):
    with open(filename, 'rb') as f:
        message = f.read()
        hash_obj = SHA256.new(message)
        signer = DSS.new(key, 'fips-186-3')
        signature = signer.sign(hash_obj)
        # Load the public key
        f = open("public_key.pem", "r")
        hash_obj = SHA256.new(message)
        pub_key = DSA.import_key(f.read())
        verifier = DSS.new(pub_key, 'fips-186-3')
        # Verify the authenticity of the message
        try:
            verifier.verify(hash_obj, signature)
            print ("The message is authentic.")
        except ValueError:
            print ("The message is not authentic.")

Begin=time.time()
DSA_2048('small_file.txt',key)
End=time.time()
print("Time taken for  DSA_2048 with 1 kb file: ",End-Begin)
if End-Begin != 0:
    print("DSA_2048 speed for 1 kb file: ",1024/(End-Begin),"bytes/sec")

Begin=time.time()
DSA_2048('large_file.txt',key)
End=time.time()
print("Time taken for  DSA_2048 with 10 mb file: ",End-Begin)
if End-Begin != 0:
    print("DSA_2048 speed for 1 kb file: ",10485760/(End-Begin),"bytes/sec")
exit()