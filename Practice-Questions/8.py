def isPalindrome(s: str) -> bool:
    s=s.lower()
    p=""
    for char in s:
        if char.isalnum():
            p+=char
    if p==p[::-1]:
        return True
    else:
        return False

print(isPalindrome("Mam"))
print(isPalindrome("Madam"))
print(isPalindrome("String"))
