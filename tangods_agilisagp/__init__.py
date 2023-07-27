from .AgilisAGP import AgilisAGP


def main():
    import sys
    import tango.server

    args = ["AgilisAGP"] + sys.argv[1:]
    tango.server.run((AgilisAGP,), args=args)
