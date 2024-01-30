import hashlib

def str_to_md5(s: str) -> str:
    h = hashlib.md5(s.encode())
    return h.hexdigest()
