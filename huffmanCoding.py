class Node:
    def __init__(self,symbol,freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

def smallest_two(nodes):
    min1=min2=None
    for node in nodes:
        if min1==None or node.freq<min1.freq:
            min2 = min1
            min1 = node
        elif min2==None or node.freq<min2.freq:
            min2=node
    return min1,min2

def tree(characters,freq):
    nodes=[]
    for i in range(len(characters)):
        nodes.append(Node(characters[i],freq[i]))
    while len(nodes)>1:
        n1,n2=smallest_two(nodes)
        nodes.remove(n1)
        nodes.remove(n2)
        newNode = Node(None,n1.freq+n2.freq)
        newNode.left=n1
        newNode.right=n2
        nodes.append(newNode)
    return nodes[0]

def generate_codes(node, code, codes):
    if node==None:
        return
    if node.symbol!=None:
        codes[node.symbol] = code
        return
    generate_codes(node.left,code+"0",codes)
    generate_codes(node.right,code+"1",codes)

# characters = ['a','b','c','d','e','f']
# freq = [10, 15, 30, 5, 20, 25]
characters=input("enter the characters:").split()
freq=list(map(int, input("enter the frequency:").split()))
root = tree(characters, freq)
codes = {}
generate_codes(root, "", codes)
print("Character | Frequency | Huffman Code")
for s in characters:
    print(f"    {s}     |    {freq[characters.index(s)]}     |    {codes[s]}")

total_freq = sum(freq)
bits_before = total_freq*8
bits_after = 0
for i in range(len(characters)):
    bits_after+=freq[i]*len(codes[characters[i]])

print("\nTotal bits before compression is", bits_before)
print("Total bits after compression is", bits_after)
print("Compression Ratio is", round(bits_after / bits_before, 3))
