#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)

manages urllib.error.HTTPError exceptions and
print: Error code: followed by the HTTP status code
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError


if __name__ == "__main__":
    req = Request(argv[1])

    try:
        with urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as ex:
        print('Error code:', ex.code)
