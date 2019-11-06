def palindrome(mot):
    w = ""
    for i in mot:
        w = i + w
    if (mot == w):
        print("Palindrome")
    else:
        print("Non Palindrome")

palindrome("kayak")