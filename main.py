#!/usr/bin/env python

import argparse

from apps import app

parser = argparse.ArgumentParser("")
parser.add_argument("-debug", action='store_true')
parser.add_argument("-db", action="store_true")
args = parser.parse_args()

if args.db:
    from apps.data.transgodatabase import init_database
    init_database()
    exit(0)

if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
