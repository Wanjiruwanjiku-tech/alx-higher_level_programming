MORE DATA STRUCTURES

DICTIONARIES AND SETS

0x04. Python - More Data Structures: Set, Dictionary
Python
 By: Guillaume
 Weight: 1

Dictionaries are unordered collections of Key : value pairs where each key is unique. They are represented by curly braces and key-value pairs seperated by colons

Example 1


	my_dictionary = {"key" : value}, "key" : value}


Example 2


	my_dictionary = dict(key=value, key=value)
	

Sets are unordered collections with no duplicate elements. Main characteristics of sets is that they are Mutable and they don't allow duplicate values

Example 3


	basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
	print(basket) # show that duplicates have been removed
	{'orange', 'banana', 'pear', 'apple'}
