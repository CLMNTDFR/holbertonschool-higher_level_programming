#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        #  Try to execute a function passed by a pointer
        #  And return the result
        result = fct(*args)
        return result

    except Exception as e:
        #  If function doesn't run, an ErrorMessage is writted in stderr
        #  And return None
        sys.stderr.write("Exception: {}\n".format(e))
        return None
