class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_folder = False

class Solution:
    def add_folder(self, root, folder):
        folders = folder.split('/')
        node = root
        for f in folders[1:]:
            if node.is_folder:
                return False
            if f not in node.children:
                node.children[f] = TrieNode()
            node = node.children[f]
        node.is_folder = True
        return True

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        root = TrieNode()
        res = []
        for f in folder:
            if self.add_folder(root, f):
                res.append(f)
        return res