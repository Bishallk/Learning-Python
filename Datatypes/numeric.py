
#--------------------N U M E R I C-----------------------------#
#----------------- D A T A T Y P E S---------------------------#

#*Integers (+ve, -ve, zero)

#* Used for whole numbers, positive or negative.
#* No size limit in Python (depends on system memory).
a = 10
b = -5
print(a + b)  # Output: 5
print(a * 3)  # Output: 30
print(a // 3) # Integer division: Output 3
print(a ** 2) # Exponentiation: Output 100

#* Float
#* Used for decimal numbers.
#* Supports scientific notation (e) ie. 10^xx

#* Python uses IEEE 754 double-precision for floating-point representation, which provides 15-16 decimal digits of precision.
#* For  high precision use decimal module 
c = 3.14
d = 1.5
print(c * d)     # Output: 4.71
print(c ** 2)    # Output: 9.8596
print(1.2e3)     # Scientific notation: 1.2×10^3 : Output 1200.0

#* Complex Numbers
#* Numbers with real and imaginary parts (a + bj)
#* we can use the cmath module to handle complex numbers more efficiently.. cmath.phase(), cmath.polar(), etc.

z = 2 + 3j
print(z.real)   # Real part: 2.0
print(z.imag)   # Imaginary part: 3.0
print(z ** 2)   # Output: (-5+12j)



