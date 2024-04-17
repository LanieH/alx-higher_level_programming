#!/usr/bin/python3
"""
    This module returns an object's available properties and methods.

"""

def lookup(obj):
    """
        This function checks for all attributes and methods of an object.
    """
    return dir(obj)
