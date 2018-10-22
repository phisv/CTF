def decode_flask_cookie(secret_key, cookie_str):
    import hashlib
    from itsdangerous import URLSafeTimedSerializer
    from flask.sessions import TaggedJSONSerializer
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    # return s.loads(cookie_str)
    print(s.loads(cookie_str))

decode_flask_cookie("a155eb4e1743baef085ff6ecfed943f2", ".eJwlj0FqAzEMAP_icw6WZFtSPhMkWaKl0MJucir9exZ6n4GZ3_aoI8-Pdn8er7y1x-du97ZplTuIOKp0oGQNcTDeaK5ERoUW00EHOhYZwuRenKAu3O1ClPteHmOYOkmh4iTtqYwjdW1GJuuCYlsWcJkv7JNiis9h7dbiPOrx_PnK76tHxk6INSBIogQJEydQXxIDs8JRLnnn5b3OPP4nANrfG15nPcs.DqGUug.GhhuolnNyvK3MIZ3SVjUjki-VFA")
