
PYTHON - Everything is object

Background Context

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:


		>>> a = 1
		>>> b = a
		>>> a = 2
		>>> b
		1
		>>>

OK. But what about this?


		>>> l = [1, 2, 3]
		>>> m = l
		>>> l[0] = 'x'
		>>> m
		['x', 2, 3]
		>>>

Requirements


Python Scripts


- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- .txt Answer Files
- Only one line
- No Shebang
- All your files should end with a new line
