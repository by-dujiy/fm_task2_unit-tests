import anagrams


def msg_to_str(msg_obj):
    return anagrams.phrase_anagram(str(msg_obj))


if __name__ == '__main__':
    msg = input("Enter anyway: \n")
    print(msg_to_str(msg))
