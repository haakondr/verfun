from verfun import version_hash_for_function, version_hash_for_function_list


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


def different_function():
    return "this one is different"


# generate checksum for each function
print(version_hash_for_function(some_strange_looking_function))
# c4cb4d2638d790016cbee29a6ed5af8c

print(version_hash_for_function(same_strange_looking_function))
# c4cb4d2638d790016cbee29a6ed5af8c

print(version_hash_for_function(different_function))
# 8515c1678211e93362800b30ef7234cf

# generate a checksum for multiple functions
print(version_hash_for_function_list([some_strange_looking_function, different_function]))
# 1fa4dc521f63cd5a8faac4cc8402d63d
