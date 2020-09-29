# Python Program to Check a Given String is Palindrome or Not
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=(input("Enter string:"))
if is_palindrome(a):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")
