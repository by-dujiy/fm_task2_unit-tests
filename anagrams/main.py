def str_reverse(str_obj):
    temp = [char for char in str_obj if char.isalpha()]
    new_str = []
    for char in str_obj:
        if char.isalpha():
            new_str.append(temp.pop())
        else:
            new_str.append(char)
    return ''.join(new_str)


def phrase_anagram(str_obj):
    word_list = str_obj.split(' ')
    reverse_list = [str_reverse(word) for word in word_list]
    return ' '.join(reverse_list)


if __name__ == '__main__':
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e")
    ]

    for text, reversed_text in cases:
        assert phrase_anagram(text) == reversed_text
