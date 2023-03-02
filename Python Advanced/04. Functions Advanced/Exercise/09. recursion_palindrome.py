def palindrome(word, first=0, last=-1):

    if word[first] != word[last]:
        return f"{word} is not a palindrome"

    if first == len(word) // 2 or first == len(word) - 1:
        return f"{word} is a palindrome"

    return palindrome(word, first + 1, last - 1)




print(palindrome("abcba", 0))
print(palindrome("neven", 0))