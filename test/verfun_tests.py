import unittest

from src.verfun import version_hash_for_function


def some_strange_looking_function(param1, callback_fn):
    tail = param1[-1]
    return callback_fn(tail)


def same_function_same_content_different_fn_name(param1, callback_fn):
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


def same_function_but_with_different_variable_names(xxx, callback_yyy):
    trail = xxx[-1]
    return callback_yyy(trail)


def same_function_with_more_whitespace(param1, callback_fn):
    tail = param1[-1]
    return callback_fn(tail)


def different_function_same_args(param1, callback_fn):
    tail = param1[0:1]
    return callback_fn(tail)


class VersionFunctionTest(unittest.TestCase):

    def test_should_ignore_function_name(self):
        hash1 = version_hash_for_function(some_strange_looking_function)
        hash2 = version_hash_for_function(same_function_same_content_different_fn_name)

        self.assertEqual(hash1, hash2)

    def test_should_ignore_comments_and_docstrings(self):
        hash1 = version_hash_for_function(some_strange_looking_function)
        hash2 = version_hash_for_function(same_strange_looking_function)

        self.assertEqual(hash1, hash2)

    def test_should_ignore_whitespaces(self):
        original_hash = version_hash_for_function(some_strange_looking_function)
        more_whitespace_hash = version_hash_for_function(same_function_with_more_whitespace)

        self.assertEqual(original_hash, more_whitespace_hash)

    def test_should_be_deterministic(self):
        hash1 = version_hash_for_function(some_strange_looking_function)
        hash2 = version_hash_for_function(some_strange_looking_function)

        self.assertEqual(hash1, hash2)

    def test_should_differentiate_different_functions(self):
        hash1 = version_hash_for_function(some_strange_looking_function)
        hash2 = version_hash_for_function(different_function_same_args)

        self.assertNotEqual(hash1, hash2)

    @unittest.skip("currently not implemented, see issue https://github.com/haakondr/verfun/issues/1")
    def test_should_ignore_variable_names(self):
        original_hash = version_hash_for_function(some_strange_looking_function)
        different_variables_hash = version_hash_for_function(same_function_but_with_different_variable_names)

        self.assertEqual(original_hash, different_variables_hash)


if __name__ == '__main__':
    unittest.main()
