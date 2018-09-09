messages = (

    "This is the secret message one. It is the best one",
    "I am typing things to fill up space. La La La LA LAH LAH LAH LAH LAH",
    "Why are the ponies attacking my brain?! I DON'T KNOW!",
    "The chicken crossed the road in order to murder all of the babies",
    "I think the most evil thing is the chocolate on the road that kills",
    "There is a light above my head and it is bright and should die",
    "bunnies are cute and I want to squeeze them to DEATH",
    "All this talk about death is making me hungry. I should find food",
    "I really want chipotle. My wife should eat it too because okay yes",
    "I want a GIANT BURRITO because it is good and I can eat it",
    "This is my most super secret target message"
)


def strxor(a, b):
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def ciphertexts(msgs=messages):
    ## Generate ciphertexts from messages using random (but reused) key
    key = open("/dev/urandom").read(1024)
    return [strxor(key, msg) for msg in msgs]


def main():
    ctexts = ciphertexts()
    # Deduce partial key from scratch using spaces as a crib
    key=[" "] * len(max(ctexts, key=len))
    for a in range(0,len(ctexts)):
        for b in range(0,len(ctexts)):
            if a == b: pass
            xored = strxor(ctexts[a],ctexts[b])
            for p in range(0,len(xored)):
                if xored[p].isalpha():
                        key[p] = strxor(xored[p].lower(),ctexts[a][p])

    # Attempt decryption of all ciphertexts using partial key
    for ciphertext in ctexts:
        attempt=[" "] * len(ciphertext)
        for index, keychar in enumerate(key):
            if index < len(ciphertext) and keychar is not ' ':
                attempt[index] = strxor(keychar,ciphertext[index])
        print("".join(attempt))

if __name__ == '__main__':
    main()
