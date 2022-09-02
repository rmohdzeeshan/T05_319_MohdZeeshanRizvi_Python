"""
1. Decision making-
    a)Decision making is a anticipation of conditions occuring while execution of the program and specifying actions taking according to the conditions.
    b)Decision structure evaluate multiple expressions which produce True or False as outcome.
    c)You need to determine which action to take and which statements to execute if outcome is TRUE or FALSE otherwise.
    d)Python programming language assumes any non-zero and non-null values as TRUE and if it is either zero or null, then it is assumed as FALSE value.

2. Types of Decision making statements-
    Python programming language provides following types of decision making statements:
        a) if statements.
        b) if-else statements.
        c) nested if statements.
        d) if-elif---else statements.

3. The if statements:
    This statement is used to execute one or more statement depending on whether a condition is true or not.
    The syntax for the if statements is:
        if condition:
            statements
        ex- num=1
            if num==1:
                print("one")

4. The if-else statements:
    The if-else statement executes a group of statements when a condition is True otherwise it will execute another group statements.
    The syntax for if-else statement is:
        if condition:
            statement 1
        else:
            statement 2
    If the condition is true,the it will execute statement 1 and if the condition is false, then it will execute statement 2.
        ex- student_marks=65
            if (student_marks>=60):
                print("The student is pass")
            else:
                print("The student is not pass")

5. Nested if statements:
    Nested if means a if condition inside a if condition. 
    Any number of conditions can be nested inside one another.
    Indetation is the only way to figure out the level of nesting.
    The syntax of Nested if statements are:
        if (condition1):
            # Executes when condition1 is true
            if (condition2): 
                # Executes when condition2 is true
            # if Block is end here
            # if Block is end here
        If condition 1 is true then only the condition 2 will be execute.
    ex- num = 15
        if num >= 0:
            if num == 0:
                print("Zero")
            else:
                print("Positive number")
        else:
            print("Negative number")
        Here if num is greater than 0 then only if condition runs otherwise else condition will execute.
        once if condition satisfies then inside if condition there is another if condition then this condition satisfies then it will execute otherwise its else condition will be executed.

6.  If-elif-else statement:
    Sometimes programmers has to test multiple conditions and execute statements depending upon those conditions. if-elif-else statement is useful in such situation.
    The syntax of the statements is :
        if condition 1:
            statement 1
        elif condition 2:
            statement 2
        elif condition 3:
            statement 3
        else:
            statement 4
    When condition 1 is true, the statement 1 is executed. If condition 1 is false then condition 2 is evaluated. When condition 2 is true, statement 2 will be executed. When condition 2 is false,then condition 3 is tested and if condition 3 is true the statement 3 is executed.when condition 3 is false then statemnet 4 will be executed.
    ex- num=5
        if (num==0):
            print("the num is zero")
        elif (num>0):
            print("the num is positive")
        else:
            print("the num is negative)
             




"""