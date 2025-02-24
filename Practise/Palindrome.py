def is_palindrome(value):
    if str(value)==str(value)[::-1] :
        print(f"{value} is palindrome")
    else:
        print(f"{value} is not palindrome")

is_palindrome("12321")
is_palindrome("bishal")