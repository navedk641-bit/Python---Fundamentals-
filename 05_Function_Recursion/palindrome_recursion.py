Check Palindrome Using Recursion

def is_palindrome(text):
if len(text) <= 1:
return True

if text[0] != text[-1]:
    return False

return is_palindrome(text[1:-1])

word = "madam"

if is_palindrome(word):
print(word, "is a Palindrome")
else:
print(word, "is not a Palindrome")
