import requests
import json

import hmac
import hashlib
import time
import struct

def generate_totp(userid: str) -> str):
    secret = (userid + "HENNGECHALLENGE004").encode("ascii")
    timestep = 30
    counter = int(time.time()) // timestep

    msg = struct.pack(">Q", counter)
    hmac_hash = hmac.new(secret, msg, hashlib.sha512).digest()

    offset = hmac_hash[-1] & 0x0F
    binary = struct.unpack(">I", hmac_hash[offset:offset+4])[0] 
    binary &= 0x7FFFFFFF

    return str(binary % 10**10).zfill(10)

url = "https://api.challenge.hennge.com/challenges/backend-recursion/004"
email = "avibuche@gmail.com"
totp_password = generate_totp(email)

payload = {
    "github_url": "https://gist.github.com/AvantiBuche/8c9abf85c386fe240efe4b498f02691f",
    "contact_email": email,
    "solution_language": "python"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(
    url,
    headers=headers,
    data=json.dumps(payload),
    auth=(email, totp_password)  # HTTP Basic Auth
)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
