def manual_palindrome(text):
    cleaned = text.replace(" ", "").lower()

    reversed_text = ""

    for char in cleaned:
        reversed_text = char + reversed_text

    return cleaned == reversed_text


print(manual_palindrome("madam"))
print(manual_palindrome("hello"))
print(manual_palindrome("Never Odd Or Even"))