import hashlib
import json
def crypto_hash(data):
    '''
    return a sha-256 hash of the given data
    '''
    stringified_data = json.dumps(data)
    return hashlib.sha256(stringified_data).hexdigest()
def main():
    print("crypto_hash : {}".format(crypto_hash('slesha')))
if __name__=='__main__':
    main()