class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq < b.freq or b.freq < a.freq:
        return a.freq < b.freq
    else:
        return a.char < b.char

def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    newNode = HuffmanNode(a.char, a.freq + b.freq)
    newNode.set_left(a)
    newNode.set_right(b)
    return newNode


def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    fin = open(filename, 'r')
    file = fin.readlines()
    ascii_arr = [0] * 256
    for line in file:
        for i in line:
            ascii_arr[ord(i)] += 1
    fin.close()
    return ascii_arr



def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    treeList = []
    for i in range(0, len(char_freq)):
        if char_freq[i] != 0:
            treeList += [HuffmanNode(i, char_freq[i])]
    _sort_tree(treeList)
    return _create_huff_tree(treeList)

def _create_huff_tree(treeList):
    while len(treeList) > 1:
        internal = combine(treeList[0], treeList[1])
        treeList.append(internal)
        treeList.pop(0)
        treeList.pop(0)
        _sort_tree(treeList)
    return treeList.pop(0)


def _sort_tree(treeList):
    for i in range(0, len(treeList) - 1):
        for j in range(0, len(treeList) - i - 1):
            if comes_before(treeList[j+1], treeList[j]):
                temp = treeList[j]
                treeList[j] = treeList[j + 1]
                treeList[j + 1] = temp
    return treeList


def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    arr = [None] * 255
    _create_code(node, '', arr)
    return arr


def _create_code(node, code, arr):
    if node.right == None and node.left == None:
        arr[node.char] = code
    if node.left != None:
       _create_code(node.left, code + "0", arr)
    if node.right != None:
       _create_code(node.right, code + "1", arr)


def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    header = ""
    for i in range(0, len(freqs)):
        if freqs[i] != 0:
            header += '{} '.format(i)
            header += '{} '.format(freqs[i])
    return header.strip()


def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    try:
        freq_arr = cnt_freq(in_file)
    except:
        raise FileNotFoundError
    try:
        fout = open(out_file, 'w')
    except:
        raise FileNotFoundError
    header = create_header(freq_arr)
    count = 0
    for i in freq_arr:
        if i > 0:
            count += 1
    if count == 1:
        fout.write(header)
        fout.close()
        return
    if count == 0:
        fout.close()
        return

    node = create_huff_tree(freq_arr)
    code_arr = create_code(node)

    fin = open(in_file, 'r')

    lines = fin.readlines()


    if count > 1:
        fout.write(header + '\n')
        for line in lines:
            for i in line:
                ascii_in = ord(i)
                fout.write(code_arr[ascii_in])
    fin.close()
    fout.close()

