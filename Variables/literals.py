
#-------L I T E R A L S----------|
#* Literal is a raw data given to a variable.

#-Types of literals in python

#-Numeric Literals

## int literals

binary= 0b1010 #binary literals | 0b
decimal= 100   #decimal literals
octal= 0o310   # octal literals | 0o
hexa=0x12c     # Hexadecimal literal | 0x

## float literals

float_1=10.5
float_2=1.5e2 # 1.5 x 10^2
float_2=1.5e-2 # 1.5 x 10^-2

## complex literal

z=0.3+14j 
x=14j # we can init.. only img part 
print(z.real,z.imag)

#-String Literals

s='this is string literals'
s1="This is python literals"
char="c" #internally it is string not char
multiline_str="""this is multiline stinrg with more than one line"""
unicode=u"\u0001f600"
raw_str=r"raw \n stirng"

#-Boolean Literals
a=True +4
b=False +10

print(a,b) #5,10

#-Special Literals
i=None
print(i) # When we need to declare variable we can use none

