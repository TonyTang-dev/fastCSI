import hashlib 

def passwordToMD5(password):
    result = hashlib.md5(password.encode('utf-8'))
    print(result)
    print(result.hexdigest())
    return result.hexdigest()