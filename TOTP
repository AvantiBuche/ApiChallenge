import hmac
import hashlib
import time
import struct

def generate_totp(email):
    secret = (email + "HENNGECHALLENGE004").encode()
    timestep = 30
    counter = int(time.time() // timestep)

    msg = struct.pack(">Q", counter)
    hmac_hash = hmac.new(secret, msg, hashlib.sha512).digest()

    offset = hmac_hash[-1] & 0x0F
    binary = struct.unpack(">I", hmac_hash[offset:offset+4])[0] & 0x7fffffff

    return str(binary % 10**10).zfill(10)

email = "avibuche@example.com"
print(generate_totp(email))
