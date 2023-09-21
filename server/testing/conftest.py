#!/usr/bin/env python3

def pytest_itemcollected(item):
    # Get the parent and child nodes.
    par = item.parent.obj
    node = item.obj

    # Get the node descriptions.
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__

    # Set the node ID.
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))