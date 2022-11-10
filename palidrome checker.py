word = input(" Enter your word : ")
word_revers = word[::-1]
if word == word_revers:
    print("Word is palindrome")
else:
    print("Word is not palindrome")
print("***************")
