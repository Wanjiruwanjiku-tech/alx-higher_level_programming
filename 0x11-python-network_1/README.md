PYTHON-NETWORK#1
-------------------------------
![urllib.picture](https://github.com/Wanjiruwanjiku-tech/alx-higher_level_programming/blob/master/0x11-python-network_1/Images/url.jpg?raw=true)


urlli.request
------------------------
- This is a python module used for fetching urls.
- Other that HTTP, urllib.request also supports other different schemes such as ftp e.t.c

Fetching URLs would be like

        >>>import urllib.request
        >>>with urllib.request.urlopen('<specified_url>') as response:
            html = response.read()


- urllib.request mirrors the request and response model that occurs between the client and the server.

- To create a customizable request object you can use urllib.request.Request

That would look like.

        >>> from urllib.request import Request
        >>> req = Request.('<specified_url>')
        >>> with urllib.request.urlopen('<specified_url>') as response:
            the_page = response.read()



![requests_module](https://github.com/Wanjiruwanjiku-tech/alx-higher_level_programming/blob/master/0x11-python-network_1/Images/requests.jpg?raw=true)


Requests module
------------------------------------

Make a Request
-----------------------------------------------

- Making a request with Requests is very simple.

Begin by importing the Requests module:

        import requests


Now, let’s try to get a webpage. For this example, let’s get GitHub’s public timeline:

        r = requests.get('https://api.github.com/events')


Now, we have a Response object called r. We can get all the information we need from this object.

- Requests’ simple API means that all forms of HTTP request are as obvious. For example, 

this is how you make an HTTP POST request:

        r = requests.post('https://httpbin.org/post', data={'key': 'value'})


Nice, right? What about the other HTTP request types: PUT, DELETE, HEAD and OPTIONS? These are all just as simple:

        r = requests.put('https://httpbin.org/put', data={'key': 'value'})
        r = requests.delete('https://httpbin.org/delete')
        r = requests.head('https://httpbin.org/get')
        r = requests.options('https://httpbin.org/get')

That’s all well and good, but it’s also only the start of what Requests can do.

- This project seeks to dive deeper