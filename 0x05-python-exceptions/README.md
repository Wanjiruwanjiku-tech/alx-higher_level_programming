0x05. Python - Exceptions
Python
 By: Guillaume
 Weight: 1


Learning Objectives

- Why Python programming is awesome

 What’s the difference between errors and exceptions

- What are exceptions and how to use them

- When do we need to use exceptions

- How to correctly handle an exception

- What’s the purpose of catching exceptions

- How to raise a builtin exception

- When do we need to implement a clean-up action after an exception

Exceptions are objects in Python that represent exceptional or erronous conditions that occur during program execution

They are used in situations where you anticipate errors or exceptional conditions and prevent the program from crushing

They are raised using the 'raise' keyword

		raise ValueError("Invalid input")

and can be caught and handled using the 'try' 'except' blocks

		try:
			result = 10 / 0
		except ZeroDivisionError:
			print("Error")

