#!/usr/bin/env python

from apps import app

if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
