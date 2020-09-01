deorin = input("do you want to encode or decode? ")
if deorin == "encode":
    word = input("enter a word in lowercase: ")
    word = list(word)
    codenum =[]
    for letter in word:
        codenum.append(ord(letter))
    codeword = []
    for num in codenum:
        if num >= 100:
            codeword.append(chr(num - 3))
        else:
            codeword.append(chr(num + 23))
    print("codeword =","".join(codeword))
if deorin == "decode":
    word = input("enter a codeword in lowercase: ")
    word = list(word)
    codenum =[]
    for letter in word:
        codenum.append(ord(letter))
    codeword = []
    for num in codenum:
        if num <= 119:
            codeword.append(chr(num + 3))
        else:
            codeword.append(chr(num - 23))
    print("Decoded word =","".join(codeword))

