
def hash_it(string):
    q = 0
    z = 127
    for i in [int(byte) for byte in bytearray(string, "utf-8")]:
        q += i
        z *= i
    return (((q << 3)+1)*z) % (2**32 - 1)

with open("/home/me/pass.txt") as file:
    for line in file:
        line = line.strip()
        if hash_it(line) == 293366475:
            print(line)
#print(hash_it("aaaaab"))
print(293366475)


#for i in [int(byte) for byte in bytearray("A", "utf-8")]:
    #print(i)
#print((*127*65)%(2**32 - 1))
#print(60 << 2)
