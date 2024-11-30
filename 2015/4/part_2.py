import hashlib

INPUT = "yzbqklnj"

i = 0
while True:
    if (
        hashlib.md5((INPUT + i.__str__()).encode("utf-8"))
        .hexdigest()
        .startswith("000000")
    ):
        print(i)
        break
    i += 1
