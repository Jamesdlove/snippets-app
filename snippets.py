import logging
import csv
import argparse
import sys

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file".format(name, snippet))
        writer.writerow([name, snippet])
    logging.debug("Write sucessful")
    return name, snippet

def get(name, filename):
    """ retrieve a snippet with and assocaiate name in the CSV file"""
    logging.info ("Reading {} from {}".format(name,filename))
    logging.debug("Opening file")
    with open(filename, "rb") as f:
        reader =csv.reader(f)
        selection = [row for row in reader if row[0] == name]
    logging.debug("read sucessful")
    return selection


def make_parser():
    """ Construct the command line parser """
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers(help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename")
    put_parser.set_defaults(command="put")
    # Subparser for the get command
    get_parser = subparsers.add_parser("get", help="Read a snippet")
    get_parser.add_argument("name", help="The name of the snippet")
    get_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename")
    get_parser.set_defaults(command="get")
    return parser

def main():
    """ Main function """
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print "Stored '{}' as '{}'".format(snippet, name)
    if command == "get":
        name = get(**arguments)
        print "snippet: '{}'".format(name)

if __name__ == "__main__":
    main()


