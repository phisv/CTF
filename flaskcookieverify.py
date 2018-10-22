#!/usr/bin/env python3
# encoding: utf-8

from hashlib import sha512
from flask.sessions import session_json_serializer
from itsdangerous import URLSafeTimedSerializer, BadTimeSignature
import base64
import zlib
from cuteprint import PrettyPrinter # Available here : https://github.com/terryvogelsang/cuteprint

EXAMPLE_SESSION = '.eJwlj0FqAzEMAP_icw6WZFtSPhMkWaKl0MJucir9exZ6n4GZ3_aoI8-Pdn8er7y1x-du97ZplTuIOKp0oGQNcTDeaK5ERoUW00EHOhYZwuRenKAu3O1ClPteHmOYOkmh4iTtqYwjdW1GJuuCYlsWcJkv7JNiis9h7dbiPOrx_PnK76tHxk6INSBIogQJEydQXxIDs8JRLnnn5b3OPP4noP29ASDZPZo.DqGV6A.R0LmzHpuuFWryvzFRih2MNzsliMJ6nrtFahkEKtJAI-CDlt0QU4sUKEN-1HN52EV73cKwo7z1pHljLqZ-nlThg'

p = PrettyPrinter()

signer = URLSafeTimedSerializer(
    'secret-key', salt='cookie-session',
    serializer=session_json_serializer,
    signer_kwargs={'key_derivation': 'hmac', 'digest_method': sha512}
)

def readAndVerifyCookie():
    try:
        session_data = signer.loads(EXAMPLE_SESSION)
        p.print_good("Correct Signature !")
        p.print_good("Session Data : {}".format(session_data))
    except BadTimeSignature:
        p.print_bad("Incorrect Signature for cookie : {}".format(EXAMPLE_SESSION))

if __name__ == '__main__':

    p.print_title("Flask Cookie Checker")

    # Decode
    p.print_separator(suffix="DECODING COOKIE", separator='=')
    t1 = p.start_progress(task="Decoding Cookie {} ...".format(EXAMPLE_SESSION), enable_dots=False)
    readAndVerifyCookie()
    p.stop_progress(t1)
