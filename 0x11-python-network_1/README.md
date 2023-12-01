PYTHON-NETWORK#1
-------------------------------
![urllib.picture]()


urlli.request
------------------------
- This is a python module used for fetching urls.
- Other that HTTP, urllib.request also supports other different schemes such as ftp e.t.c

Fetching URLs would be like

        >>>import urllib.request
        >>>with urllib.request.urlopen('<specified_url>') as response:
            html = response.read()

            