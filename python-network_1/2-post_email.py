#!/usr/bin/python3
"""Script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
displays the body of the response"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    data = urlencode({
                        'email': argv[2]
                    }).encode('ascii')
    req = Request(argv[1], data)

    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
