import inspect
import ast
from types import FunctionType
import hashlib
import pyminifier

m = hashlib.md5()

"""
Module(body=[FunctionDef(name='some_strange_looking_function', args=arguments(args=[arg(arg='param1', annotation=None), arg(arg='callback_fn', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Assign(targets=[Name(id='tail', ctx=Store())], value=Subscript(value=Name(id='param1', ctx=Load()), slice=Index(value=UnaryOp(op=USub(), operand=Num(n=1))), ctx=Load())), Return(value=Call(func=Name(id='callback_fn', ctx=Load()), args=[Name(id='tail', ctx=Load())], keywords=[]))], decorator_list=[], returns=None)])
Module(body=[FunctionDef(name='same_strange_looking_function', args=arguments(args=[arg(arg='param1', annotation=None), arg(arg='callback_fn', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Str(s='\n    This function is documented, but the function is identical to some_strange_looking_function\n    and should result in the same hash\n    ')), Assign(targets=[Name(id='tail', ctx=Store())], value=Subscript(value=Name(id='param1', ctx=Load()), slice=Index(value=UnaryOp(op=USub(), operand=Num(n=1))), ctx=Load())), Return(value=Call(func=Name(id='callback_fn', ctx=Load()), args=[Name(id='tail', ctx=Load())], keywords=[]))], decorator_list=[], returns=None)])
"""

def version_hash_for_function(fn: FunctionType):
    # TODO: this is currently not working
    function_as_str = inspect.getsource(fn)
    pyminifier.pyminify(function_as_str)
    abstract_syntax_tree = ast.parse(function_as_str)
    ast_string = ast.dump(abstract_syntax_tree, annotate_fields=False)

    print(ast_string)
    m.update(ast_string.encode("utf-8"))
    return m.hexdigest()
