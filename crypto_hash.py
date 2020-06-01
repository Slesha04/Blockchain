import hashlib
import json

def crypto_hash(*args):
    '''
    return a sha-256 hash of the given arguments
    '''
    stringified_args = sorted(map(lambda data: json.dumps(data),args))
    joined_data = ''.join(stringified_args)
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()
def main():
    print("crypto_hash : {}".format(crypto_hash('slesha','chu',1)))
    print("crypto_hash : {}".format(crypto_hash('slesha', 1 ,'chu')))
if __name__=='__main__':
    main()