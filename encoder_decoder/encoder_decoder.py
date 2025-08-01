PREFIX = "dsf"
SUFFIX = "jkr"

def encode_word(word):
    if len(word) >= 3:
        return PREFIX + word[1:] + word[0] + SUFFIX
    return word[::-1]

def decode_word(word):
    if len(word) > 6:
        core = word[3:-3]
        return core[-1] + core[:-1]
    return word[::-1]

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    words = sentence.split(" ")
    coding = input("Enter 1 for Encoding and 0 for Decoding: ")
    coding = coding.strip() == "1"

    print("Encoding..." if coding else "Decoding...")

    finalwords = []

    for word in words:
        try:
            finalwords.append(encode_word(word) if coding else decode_word(word))
        except Exception as e:
            print("An error occurred:", e)

    print("Result:", " ".join(finalwords))
  
