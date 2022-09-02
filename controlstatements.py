"""
1. Control statements:
    In order to change the way a loop is executed from its usual behavior, control statements are used. 
    Control statements are used to control the flow of the execution of the loop based on a condition.

    Python supports following control statements:
    1. break statement.
    2. continue statement.
    3. pass statement.

2. Break statement:
    The break statement can be used inside a for loop or while loop to come out of the loop.
    When break statement is executed, the python interpreter jump out of the loop to process the next statementin the program.
    It breaks the current execution and in case of inner loop, inner loop terminates immediately.    
"""
# from re import X


# lst=[1,2,3,4,5,6,7,8,9,10]
# for i in lst:
#     if i==4:
#         print(i)
#         print("element found")
#         break
#     print(i)

# using break to come out of the loop?
# x=10
# while(x>=1):
#     print("x=",x)
#     x-=1
#     if x==5:   
#         break
# print("out of the loop")
"""
3. Continue statement:
    The continue statement is used in a loop to go back to the begining of the loop.
    It means when continue is executed the next repition will start.
    Python Continue Statement is a jump statement which is used to skip execution of current iteration.
    After skipping, loop continue with next iteration. 
"""
# to display numbers from 1 to 5 using continue statement?
# x=0
# while x<10:
#     x+=1
#     if x>5:
#         continue
#     print("x=",x)
# print("out of the loop")

"""
4. Pass statement:
    The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.
    In Python, pass keyword is used to execute nothing; it means, when we don't want to execute code, the pass can be used to execute empty.
    It just makes the control to pass by without executing any code.
     If we want to bypass any code pass statement can be used.
"""
# a program to know that pass does nothing?
x=0
while x<10:
    x+=1
    if x>5:
        pass 
    print("x=",x)
print("out of the loop")

# A more meaningful usage of the pass statement is to inform the python interpreter not to do anything when we are not interested in the result.