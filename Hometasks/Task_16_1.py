import re


def abbv(fr):
    sk = re.findall(r'\b\w', fr)
    return "".join(sk)


print(abbv(input()).upper())

