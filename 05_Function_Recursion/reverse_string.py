def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

string = input("Enter a string: ")

result = reverse_string(string)

print("Reversed string:", result)
