# Doctstrings in Python and PEP-8 in Python

# Python Docstrings are basically the string literals that appear just after the definition of a function, method, class or a module.
# A python Docstring and Comment are different
# Like comments, Docstrings are not ignored in python. It is given an special treatment.
# Docstring are string literals enclosed within ''' ''' just above the function definition
# Changing of the docstring may also change the program.

def tp():
    '''This is a simple function to denote the use of Docstrings in Python'''
    print("Hello User")
    
tp()
print(tp.__doc__)


# PEP-8 is a guideline and provides best practice of writing python codes
# Focus was to make your python program consistent, readable, maintanable.
# PEP stands for Python Enhancement Proposal


# Zen of Python
'''
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''