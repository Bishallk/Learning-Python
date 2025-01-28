
#-------------------- S T R I N G------------------------------#
#----------------- D A T A T Y P E S---------------------------#


#* Strings is a sequence of characters enclosed within single quotes('),double quotes("") and triple quotes (''') or (""")

#*Strings in Python are immutable, meaning once they are created, they cannot be modified. Any operation that seems to modify a string actually creates a new string.

name="bishal kunwar"

#-------- Concatenation

greeting = "Hello"
name = "Bishal"
message = greeting + " " + name  # Concatenate strings
print(message)  # Output: Hello Bishal

#-------- Repetition:

repeat = "Hi! " * 3
print(repeat)  # Output: Hi! Hi! Hi!

#-------- Indexing

print(name[0])
print(name[-1])##Strings are indexed starting from 0 or -1 from end

#-------- Slicing

print(name[6:13:2])
print(name[6:13])
print(len(name))

#-------- Iterate String

if "i" in name:
    print(True)
else:
    print(False)

for i in range(0,len(name),1):
    print(name[i])


#-------------------------------M E T H O D S--------------------------------------|

#* capitalize() -capitalize first char of string and other char to lowercase.
text = "hello world"
result = text.capitalize()
print(result) # Output: "Hello world"

#* upper()  -> Capitalize all letters of string.
#* For Eg.
text = "hello world"
result = text.upper()
print(result) # Output: "HELLO WORLD"
format()
#* title() -> Capitalizes the first letter of each word in the string.
#* For Eg.
text = "hello world, python is FUN"
result = text.title()
print(result)  # Output: "Hello World, Python Is Fun"

#* isnumeric() -> Returns True if the string contains only numeric characters (including Unicode digits,fractions, superscripts).
#* For Eg.
# Basic digits
print("123".isnumeric())  # Output: True

# Unicode numeric characters
print("½".isnumeric())  # Output: True (Unicode fraction)
print("四".isnumeric())  # Output: True (Chinese numeral)

# Not numeric
print("123a".isnumeric())  # Output: False

#* isdigit() -> Returns True if all characters in the string are strictly digits (0–9) or characters categorized as digits in Unicode (e.g., superscript digits).
#* For Eg.
# Basic digits
print("123".isdigit())  # Output: True

# Unicode digit characters
print("²".isdigit())  # Output: True (superscript 2)

# Not digits
print("½".isdigit())  # Output: False (fraction)
print("四".isdigit())  # Output: False (Chinese numeral)

#* isalnum() ->Returns True if the string contains only alphanumeric characters (letters and digits).
#* For Eg.
print("Hello123".isalnum())  # Output: True (contains only letters and numbers)
print("Python2023".isalnum())  # Output: True

# Non-alphanumeric examples
print("Hello 123".isalnum())  # Output: False (contains a space)
print("Hello!".isalnum())     # Output: False (contains a special character)
print("123@#".isalnum())      # Output: False (contains symbols)

# Empty string
print("".isalnum())           # Output: False (empty string is not alphanumeric)

#* isupper() -> Returns True if all characters in the string are uppercase, otherwise False.
#* For Eg.
"HELLO".isupper()  # Output: True

#* islower() -> Returns True if all characters in the string are lowercase, otherwise False.
#* For Eg.
"hello".islower()  # Output: True

#* isalpha() -> Returns True if the string contains only alphabetic characters (no spaces, digits, or special characters).
#* For Eg.
"Hello".isalpha()  # Output: True

#* find(substring) -> Returns the lowest index where the substring is found, or -1 if not found.
#* For Eg.
"hello world".find("world")  # Output: 6

#* count() ->Counts the number of times a substring appears in the string.
#* For Eg.
"hello hello".count("hello")

#* startswith(substring) -> Returns True if the string starts with the specified substring.
#* For Eg.
"hello".startswith("he")  # Output: True

#* endswith(substring) -> Returns True if the string ends with the specified substring.
#* For Eg.
"hello".endswith("lo")  # Output: True

#* strip() -> Removes leading and trailing whitespaces.
#* For Eg.
"  hello  ".strip()  # Output: "hello"

#* replace(old, new) -> Replaces occurrences of a substring with a new substring.

#* split(delimiter) -> Splits the string into a list based on a delimiter.
#* For Eg.
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']

#* join(iterable) -> Joins elements of an iterable into a string with the separator.
#* For Eg.
fruits = ['apple', 'banana', 'orange']
result = ", ".join(fruits)
print(result)  # Output: apple, banana, orange

#* center(width) -> Centers the string within the specified width using spaces (or another specified character).
#* For Eg.
"hello".center(10)  # Output: "  hello   "