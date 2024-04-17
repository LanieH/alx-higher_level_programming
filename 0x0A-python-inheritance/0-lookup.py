#!/usr/bin/python3
"""
This module defines a function to retrieve an object's attributes and methods.
"""

def lookup(obj):
    """
    Retrieve and return a list of attributes and methods of the given object.

    Args:
        obj: An object to inspect.

    Returns:
        A list of strings containing the names of the object's attributes and methods.
    """
    return dir(obj)
