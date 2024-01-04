JAVASCRIPT WEBSCRAPING
-------------------------------------


    JSON (JavaScript Object Notation)
------------------------------------------------------


- Json is a human-readable, text-based format that represents data.


- It is lightweight and commonly usedd for Application Programming Interfaces (APIs) as it intergrate easily with other programming languages.

- JSON is commonly used for transmitting data. This makes data transmission easier since jason is a string(text-based).

- To acess the data the string has to be deserialized


JSON supports multiple data types including:
- Strings "that always need to be double quoted"
- Numbers of any type
- Boolean data types
- Arrays
- Objects

JSON STRUCTURE
------------------------------

- The structure resembles that of a JavaScript object literal format.

- First create a file name with the .json format and then store your string in it.

EXAMPLE
-------------------------

        user.json 

        [
            {
                "name": "Natalie",
                "age": 26,
                "active": true,
                "friends": [
                    {
                        "name": "Joan",
                        "age": 20,
                        "active": false,
                        "rating": 3.7
                    },
                    {
                        "name": "Raphael",
                        "age": 15,
                        "active": true,
                        "rating": 3.5
                    }
                ],

                "ceo": "Catherine",
                "herage": 49,
                "status": false,
                "friend": null
            }
        ]


This project seeks to dive deeper into the JSON format