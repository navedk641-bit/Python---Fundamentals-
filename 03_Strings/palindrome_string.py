# Palindrome String Check

text = input("Enter a string: ")

# Remove spaces and convert to lowercase
cleaned_text = text.replace(" ", "").lower()

# Check palindrome
if cleaned_text == cleaned_text[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")
