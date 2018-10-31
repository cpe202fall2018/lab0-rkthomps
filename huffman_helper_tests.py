import unittest
import subprocess
from huffman import *
class TestFile (unittest.TestCase):
    def testfile2(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell=True)
        self.assertEqual(err, 0)
    def testmultiline(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell=True)
        self.assertEqual(err, 0)
    def testdeclaration(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell=True)
        self.assertEqual(err, 0)

if __name__ == '__main__':
   unittest.main()
