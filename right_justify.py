def right_justify(s):
    word_len = len(s)       #assesses length of str arg and concatenates spaces
    word = ''
    while len(word) < 70 - word_len:
        word += " "
    print(word + s)

def main():
    s = "big man on campus"     #program takes str arg and prints out str with the last letter/number in the 70th column
    right_justify(s)

if __name__ == '__main__':
    main()
