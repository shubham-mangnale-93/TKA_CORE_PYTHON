# import sys

l = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5)
# print(sys.getsizeof(l))
# print(sys.getsizeof(t))

from sys import getsizeof
 
print(getsizeof(l))
print(getsizeof(t))
#----------------------------------------------------------------------------------------

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(getsizeof(l))

r = range(1,1000000001,1)
print(getsizeof(r))

#---------------------------------------------------------------------------------------
'''
# ============================================================
# Two ways to import the sys module
# ============================================================
# import sys                  --> Method 1: need to write, sys.getsizeof(l)
# from sys import getsizeof   --> Method 2: can directly write, getsizeof(l), no need for "sys." prefix


# ============================================================
# LIST vs TUPLE - memory comparison
# ============================================================
l = [1, 2, 3, 4, 5]     # list -> mutable (can be changed)
t = (1, 2, 3, 4, 5)     # tuple -> immutable (cannot be changed)

print(getsizeof(l))     # Output: 104
print(getsizeof(t))     # Output: 80

# Observation: even with the same 5 elements, list (104) takes more memory than tuple (80)
#
# Reason:
# - List is MUTABLE -> elements can be added/removed later
#   so Python already reserves some extra space (over-allocation),
#   so that if something is appended in future, space is immediately available
#
# - Tuple is IMMUTABLE -> once created, it can never be changed,
#   Python already knows this, so it only needs exactly the required (fixed) space
#
# Summary: Tuple is more memory-efficient than List, because it is immutable


# ============================================================
# LIST vs RANGE - memory comparison
# ============================================================
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(getsizeof(l))     # Output: 216   -> size increased because there are 20 elements

r = range(1,1000000001,1)
print(getsizeof(r))     # Output: 48    -> size stays small even with 1 billion numbers

# Observation: list's size increases with the number of elements,
# but range's size always stays CONSTANT (fixed) - no matter how many numbers it represents
#
# Reason:
# - range() only stores 3 things -> start, stop, step
# - It does NOT store all the numbers, it calculates each value mathematically (on the fly) when needed
#
# Summary: Range is the most memory-efficient option for large sequences
'''

#---------------------------------------------------------------------------------------
'''
# ============================================================
# sys module import karaychya don pddhati
# ============================================================
# import sys                  --> Method 1: sys.getsizeof(l) asa vaprava lagta
# from sys import getsizeof   --> Method 2: sarla getsizeof(l) vaprata yeta, "sys." lavaychi garaj nahi


# ============================================================
# LIST vs TUPLE - memory comparison
# ============================================================
l = [1, 2, 3, 4, 5]     # list -> mutable (badalta yete)
t = (1, 2, 3, 4, 5)     # tuple -> immutable (badalta yet nahi)

print(getsizeof(l))     # Output: 104
print(getsizeof(t))     # Output: 80

# Nireekshan: same 5 elements astana suddha list (104) hi tuple (80) peksha jasta memory gheते
#
# Karan:
# - List MUTABLE aahe -> pudhe elements add/remove hou shaktat
#   mhanun Python adhich thodi extra jaga rakhun thevto (over-allocation),
#   jenekaruna future madhe append kelं tar lagech jaga milel
#
# - Tuple IMMUTABLE aahe -> ekda tayar zalyavar tyat kadhihi badal honar nahi,
#   he Python la adhich mahit asta, mhanun tyala fakt nemki tevadhich (fixed) jaga lagte
#
# Sar: Tuple he List peksha jasta memory-efficient aahe, karan te immutable aahe


# ============================================================
# LIST vs RANGE - memory comparison
# ============================================================
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(getsizeof(l))     # Output: 216   -> 20 elements astana size vadhli

r = range(1,1000000001,1)
print(getsizeof(r))     # Output: 48    -> 100 koti numbers astoonhi size kami

# Nireekshan: list cha size elements chya sankhyene wadhto,
# pan range cha size nehmi CONSTANT (fixed) rahto - kiti hi numbers asले tari
#
# Karan:
# - range() fakt 3 goshti store karto -> start, stop, step
# - Prattyaksh sagle numbers store karत nahi, gaznitane (on the fly) calculate karto
#
# Sar: Range he sarvat memory-efficient aahe motha sequence sathi

'''