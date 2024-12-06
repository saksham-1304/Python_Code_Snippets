try:
    if True:
    print("This line has an indentation error.")
except IndentationError as e:
    print("An IndentationError occurred",e)    


"""
Output
File "c:\Users\HP\Desktop\Codes\Python_Code_Snippets\04_Conditional_Execution\_13_try_catch_or_try_except.py", line 3
    print("This line has an indentation error.")
    ^
IndentationError: expected an indented block

"""