# Floating Point

import sys

# print the attribute max of the object float_info
print("Max. floating point number", sys.float_info.max)  # Output: Max. floating point number 1.7976931348623157e+308

# print the attribute min of the object float_info
print("Min. floating point number ", sys.float_info.min)  # Output: Min. floating point number 2.2250738585072014e-308


i = 0
for j in range(11):
    i += 0.1  # Output: 1.0999999999999999
print(i)
