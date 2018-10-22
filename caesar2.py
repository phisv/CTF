ct = "e^Xd8I;pX6ZhVGT8^E]:gHT_jHITVG:cITh:XJg:r"
shift = 1
while shift < 128:
    pt = ""
    for a in ct:
        pt = pt + chr((ord(a)+shift)%128)
    shift += 1
    print(pt)
