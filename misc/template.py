import os
import requests
import argparse

__author__ = "Heeraj"


class Recon():
    """
    A class to Recon a given website
    """

    def __init__(self):
        self.target = ""
        return

    def assign_target(self, target):
        self.target = target
        return

    def headers(self, target):
        req = requests.get(self, target)
        print "=============================================================="
        print "Response Headers:\n"
        for name, value in req.headers.item():
            length = len(name)
            length = 25 - length
            print name + ": ".rjust(length) + value
        return

    def cookies(self):
        req = requests.get(self.target)
        print "=============================================================="
        print "Response Cookies:\n"
        for name, value in req.cookies.item():
            length = len(name)
            length = 25 - length
            print name + ": ".rjust(length) + value
        return


def main():
    recon = Recon()

    parser = argparse.ArgumentParser(description='Web description')

    parser.add_argument('-u', '-url', type=str, help='Target URL to recon')

    parser.add_argument('-c', help="Print cookies", action="store_true")

    parser.add_argument('-a', help="Print all values", action="store_true")

    args = parser.parse_args()

    if args.c:
        recon.cookies()
        exit(0)

    if args.a:
        args.c = True

main()
