import argparse
import time
import hashlib
from pprint import pprint 

import requests


api = "http://gateway.marvel.com/v1/public/characters"

def hasbuilder(rand,privkey,pubkey):
    return hashlib.md5((f"{rand}{privkey}{pubkey}").endcode('utf-8')).hexdigest()

def marvelcharcall(rand,keyhash,pubkey,lookmeup):
    r = reqeusts.get(f"{api}?name={lookmeup}&ts={rand}%apikey={pubkey}&hash={keyhash}")

    if r.status_code != 200:
        response = None
    else:
        response = r.json()
    return response

def main():
    with open(args.dev) as pkey:
        privkey = pkey.read().rstrip('/n')

    with open(args.pub) as pkey:
        pubkey = pkey.read().rstrip('/n')
rand =str(time.time()).rstrip('.')
keyhash = hasbuilder(rand,privkey,pubkey)

result = marvelcharcall(rand,keyhash,pubkey,"wolverine")

pprint(result)
if __name__=="__main__":
    parser = arparse.ArgumentParser()

    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')
    
    args =parser.parse_args()
    main()

