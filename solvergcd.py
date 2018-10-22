import rsa
from sympy import mod_inverse
from Crypto.Util.number import long_to_bytes
from Crypto.PublicKey import RSA
import math

e = 65537
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

#print(gcd(10,8))
pubgs = []
n = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ps = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
q = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0, 20):
    with open(f"/home/me/atom/public_keys/key{i}.pem") as p:
        pubgs.append(rsa.PublicKey.load_pkcs1_openssl_pem(p.read()))
flag = open('/home/me/ctf/static/unbreakable_code', 'rb').read()
flag = int.from_bytes(flag, byteorder='big')

for i in range(0,20):
    for k in range(0,20):
        mygcd = gcd(pubgs[i].n, pubgs[k].n)
        if mygcd != 1 and i < k:
            print(i,k)
            #print(mygcd)
            n[i] = pubgs[i].n
            n[k] = pubgs[k].n
            ps[i] = n[i]//mygcd
            ps[k] = n[k]//mygcd
            q[i] = mygcd
            q[k] = mygcd
#for int in n:
#    print(int)
#print(ps[16])
#print(q[16])

a = 19
while a >= 0:
    #print(a)
    nval = n[a]
    pval = ps[a]
    qval = q[a]
    phi = (pval-1)*(qval-1)
    #print(phi)
    d = mod_inverse(e, phi)

    key = RSA.construct((nval, e, d, pval, qval))
    flag = key.decrypt(flag)
    a-=1

print(long_to_bytes(flag))
