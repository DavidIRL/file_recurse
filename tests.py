import unittest

from find_files import *


class FileRecursion(unittest.TestCase):
    def test_empty_output(self):
        self.assertEqual(find_files(".w", "testdir"), [])


    def test_invalid_directory(self):
        with self.assertRaises(FileExistsError):
            find_files(".a", "etc")


    def test_directory_as_file(self):
        with self.assertRaises(FileExistsError):
            find_files("3", "find_files.py")


    def test_proper_output(self):
        output = find_files(".c", "testdir")
        self.assertEqual(find_files(".c", "testdir"), output)


                         
if __name__ == '__main__':
    unittest.main()
