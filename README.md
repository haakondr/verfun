# Verfun

[![Build Status](https://travis-ci.org/haakondr/verfun.svg?branch=master)](https://travis-ci.org/haakondr/verfun)

Verfun is a util for generating a checksum for a python function ignoring whitespace, comments, variable names, etc.

## Great, why is this useful?

Given a use case where you want to 

1. Version an algorithm that did something to your data
2. Rerun said algorithm on affected data if the algorithm changes
3. not rerun if you only add comments, refactor variable names, etc

## Features:

Generating a md5 checksum of a given function, ignoring the following:

- function name
- docstrings and comments
- whitespace
- indentation

## Example usage
Example taken from [example.py](example.py)

```
from verfun import version_hash_for_function

def some_strange_looking_function(param1, callback_fn):
    tail = param1[-1]
    return callback_fn(tail)


def same_strange_looking_function(param1, callback_fn):
    """
    This function is documented, but the function is identical to some_strange_looking_function
    and should result in the same hash
    """
    tail = param1[-1]
    # return the callback value from the tail of param whatever that is
    return callback_fn(tail)
   

# generate checksum for each function
print(version_hash_for_function(some_strange_looking_function))
# c4cb4d2638d790016cbee29a6ed5af8c

print(version_hash_for_function(same_strange_looking_function))
# c4cb4d2638d790016cbee29a6ed5af8c
```
