import unittest
import filecmp
import subprocess
from huffman import *
from huffman_helper_tests import *

class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_3_text(self):
        huffman_encode("test3.txt", "test3_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb test3_out.txt test3_soln.txt", shell=True)
        self.assertEqual(err, 0)
    def test_4_text(self):
        huffman_encode("test4.txt", "test4_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb test4_out.txt test4_soln.txt", shell=True)
        self.assertEqual(err, 0)
    def test_5_txt(self):
        huffman_encode("test5.txt", "test5_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb test5_out.txt test5_soln.txt", shell=True)
        self.assertEqual(err, 0)
    def test_6_txt(self):
        huffman_encode("test6.txt", "test6_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb test6_out.txt test6_soln.txt", shell=True)
        self.assertEqual(err, 0)
    def testError(self):
        with self.assertRaises(FileNotFoundError):
            huffman_encode("testkdkdkd.txt", "test5_out.txt")

if __name__ == '__main__': 
   unittest.main()
