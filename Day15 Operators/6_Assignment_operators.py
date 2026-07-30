'''
Assignment Operator : It is used to assign a value to a variable.
It can also combine an arithmetic operation with assignment
in a shortcut way.

=    -> assigns value
+=   -> adds and assigns    (a = a + b)
-=   -> subtracts and assigns (a = a - b)
*=   -> multiplies and assigns (a = a * b)
/=   -> divides and assigns (a = a / b)
//=  -> floor divides and assigns
%=   -> modulus and assigns
**=  -> exponent and assigns
'''

a = 10        # simple assignment
print(a)      # 10

a += 5        # same as a = a + 5
print(a)      # 15

a -= 3        # same as a = a - 3
print(a)      # 12

a *= 2        # same as a = a * 2
print(a)      # 24

a /= 4        # same as a = a / 4
print(a)      # 6.0

a //= 2       # same as a = a // 2
print(a)      # 3.0

a **= 2       # same as a = a ** 2
print(a)      # 9.0

a %= 4        # same as a = a % 4
print(a)      # 1.0