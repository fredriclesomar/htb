
def decrypt(key, msg):
    key = list(key)
    msg = list(msg)
    for char_key in reversed(key):
        for i in reversed(range(len(msg))):
            if i == 0:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[-1]))
            else:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[i-1]))
            while tmp < 0:
                tmp += 256
            msg[i] = chr(tmp)
    return ''.join(msg)



ciphertext = open('ciphertext', 'r').read().rstrip()
for i in range(1, 165):
    for j in range(33, 127):
        key = chr(j) * i
        msg = decrypt(key, ciphertext)
        if 'the' in msg or 'be ' in msg or 'and ' in msg or 'of ' in msg:
            exit("Key: {0}, Key length: {1}, Msg: {2}".format(key, len(key), msg))
