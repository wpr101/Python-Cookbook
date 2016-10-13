def isPalindrome(text):
    i = 0
    j = len(text)
    found = True
    for _ in range(len(text)):
        if (text[i] != text[j-1]):
            found = False
        i += 1
        j -= 1

    print(found)


def betterPalindrome(text):
    # [begin:end:step]
    print(text == text[::-1])


def otherPalindrome(text):
    print(text == ''.join(reversed(text)))

# isPalindrome("xpopx")
# betterPalindrome("xpopx")
otherPalindrome("xpopx")
