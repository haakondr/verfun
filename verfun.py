import inspect
import ast
from types import FunctionType
import hashlib
from typing import List

import astunparse
from pyminifier import minification


def version_hash_for_function(fn: FunctionType) -> str:
    abstract_syntax_tree = ast.parse(inspect.getsource(fn)).body[0]
    abstract_syntax_tree.name = "replaced_functionname"
    generated = astunparse.unparse(abstract_syntax_tree)

    result = minification.remove_comments_and_docstrings(generated)
    result = minification.remove_blank_lines(result)

    return hashlib.md5(result.encode('utf-8')).hexdigest()


def version_hash_for_function_list(functions: List[FunctionType]) -> str:
    checksums = [version_hash_for_function(f) for f in functions]
    joined = "".join(checksums)

    print(joined)

    return hashlib.md5(joined.encode('utf-8')).hexdigest()
