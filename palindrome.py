def ispalindrome(s):
    return s==s[::-1]
s="boob"
ans=ispalindrome(s)
if ans:
    print("this is palindrome")
else:
    print("not a palindrome")
