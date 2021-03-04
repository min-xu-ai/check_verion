#!/usr/bin/env python3

import sys
import importlib

def main(args):
    """ Returns:

        0: everything ok and version satisfied.
        1: something went wrong
    """
    if len(args) < 4:
        print("Not enough args")
        return 1
    mod_name, op, req_ver = args[1:4]
    #              >     <     ==    >=    <=    !=
    assert op in ["gt", "lt", "eq", "ge", "le", "ne"], op
    try:
        mod = importlib.import_module(mod_name)
        def convert_ver(x):
            l = x.split('.')
            for i, v in enumerate(l):
                try:
                    l[i] = int(v)
                except:
                    pass
            return l

        req = convert_ver(req_ver)
        v = convert_ver(mod.__version__)
        if len(v) < len(req):
            raise ValueError(f"version {v} too short")
        v = v[:len(req)]
        if op == "ge" and v < req:
            raise ValueError(f"version {v} too low")
        if op == "le" and v > req:
            raise ValueError(f"version {v} too high")
        if op == "eq" and v != req:
            raise ValueError(f"version {v} not equal")
        if op == "gt" and v <= req:
            raise ValueError(f"version {v} too low")
        if op == "lt" and v >= req:
            raise ValueError(f"version {v} too high")
        if op == "ne" and v == req:
            raise ValueError(f"version {v} equal")
        return 0
    except Exception as e:
        print(e)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
