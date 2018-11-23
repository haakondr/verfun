import inspect
import ast
from types import FunctionType
import hashlib

def version_hash_for_function(fn: FunctionType):
    # TODO: this is currently not working
    function_as_str = inspect.getsource(fn)
    abstract_syntax_tree = ast.parse(function_as_str)
    ast_string = ast.dump(abstract_syntax_tree, annotate_fields=False)

    return hashlib.md5(ast_string.encode('utf-8')).hexdigest()
