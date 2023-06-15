#!/usr/bin/python3
"""
	This module runs a script that defines the
	class MyInt that inherits from int
"""


class MyInt(int): #The Derived Class


    """
	The class inherits from int class
    """

    def __eq__(self, other):

        """
		Inverts the == operator
        """

        return int(self) != int(other)


    def __ne__(self, other):

        """
		Inverts the != operator
        """

        return int(self) == int(other)
