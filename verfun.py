import inspect
import ast
from types import FunctionType
import hashlib
import astunparse
from pyminifier import minification


def version_hash_for_function(fn: FunctionType):
    abstract_syntax_tree = ast.parse(inspect.getsource(fn)).body[0]
    abstract_syntax_tree.name = "replaced_functionname"
    generated = astunparse.unparse(abstract_syntax_tree)

    result = minification.remove_comments_and_docstrings(generated)
    result = minification.remove_blank_lines(result)

    return hashlib.md5(result.encode('utf-8')).hexdigest()
