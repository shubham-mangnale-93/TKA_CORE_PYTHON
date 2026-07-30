'''
def fun(p1, p2):        # parameter
    #operation ---->data

fun(value1, value2)     # argument

# what is parameter?
: A parameter is a variable in the function definition that acts as a placeholder for the value that will
  be passed to the function when it is called.
  Parameters define what kind of data the function expects.
eg.
def cube(num):   #num is a parameter
        return num**3
cube(3)
------------------------------------------------------------------------------------------------------
# what is argument?
: An argument is the actual value or data that you pass to the function when calling it. 
  The arguments are assigned to the corresponding parameters in the function.
eg.
def cube(num):   #num is a parameter
        return num**3
print(cube(3))   #27   #here 3 is argument
'''

# create a function reverse string:------------->

# def reverse(word):    
#     rev = ""
#     for char in word:
#         rev = char + rev
#     print(rev)
# reverse("pavan")      #pavan---->navap  
#-------------------------------------------------------------------------------------------------

# Input: "the kiran academy" → Output: "eht narik ymedaca"

# def fun(sen):
#     words = sen.split()
#     rev_words = []
#     for word in words:
#         rev = ""
#         for char in word:
#             rev = char + rev
#         rev_words.append(rev)    
#     result = " ".join(rev_words)
#     print(result)
# fun("The Kiran Academy")


# def reverse_each_word(sentence):
#     words = sentence.split()
#     result = ""
    
#     for word in words:
#         reversed_word = ""
#         # print(word)
#         for ch in word:
#             # print(ch)
#             reversed_word = ch + reversed_word
#         result = result + reversed_word + " "
    
#     print(result.strip())

# sentence = "the kiran academy"
# reverse_each_word(sentence)
#-------------------------------------------------------------------------------------------------


# Sentence: "python is simple dynamic programming language"

# "dynamic" → Yes
# "static"  → No

def search(sen, word):
    words = sen.split()
    # print(words)
    for wd in words:
        if wd == word:            
            print("Yes")
            break
    else:
        print("No")

search("python is simple dynamic programming language", "dynamic")
search("python is simple dynamic programming language", "static")







