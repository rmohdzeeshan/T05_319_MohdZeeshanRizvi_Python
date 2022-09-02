"""
1. Loops-
    Loops are similar to conditionals because they run on true/false value set.
    The loops continuosly runs when the condition is true and terminates when the condition is false.
    Loops can be run upto a desired length or until a flg will terminate them.
    Great technique to reuse code and therefor limit amount of statements a program needs.
    When a program repeatedly runs a set of statements it is refereed as a loop, iteration or repitition structure.

2. Types of loops-
    There are three types of loops:
        1. for loop
        2. while loop
        3. nested loop

3. for loop:
    the for loop is used to iterate over the elements in a sequence.
    It means a for loop can be used to execute a group of statements repeatedly depending upon the number of elements in the sequence.
    When we know the number of iterations, then we use for loop.
    Syntax:
        for var in sequence:
            staterments
    ex- to display each character from a string?
        str="HELLO"
        for ch in str:
            print(ch)
        output:
        H
        E
        L
        L
        O

4. while loop:
    The whille loop is useful to execute a group of stetements several times repeatedly depending on whether the condition is True or False.
    when  we don't know the number of iterations then we use While loop.
    Syntax:
        while condition:
            statements
    ex- to display the numbers from 1 to 10?
        x=1
        while x<=10:
            print(x)
            x+=1
        print("end")
        output:
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        end

5. Nested loops:
    It is possible to write one loop inside another loop means we can write a for loop inside a while loop or a while loop inside a for loop. Such loops are called 'nested loops.'
    In nested loops first the inner loop will execute and then the outer loop will be executed.
    Syntax-
        # outer for loop
            for element in sequence 
            # inner for loop
                for element in sequence:
                    body of inner for loop
                body of outer for loop
"""
    # to print multiplication table in python?
    # outer loop
for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
    for j in range(1, 11):
        # print multiplication
        print(i * j, end=' ')
    print()