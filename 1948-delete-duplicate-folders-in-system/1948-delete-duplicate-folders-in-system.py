from typing import List
from collections import defaultdict

class Solution:
    class Node:
        def __init__(self, name=""):
            self.name = name
            self.children = {}

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = self.Node()
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = self.Node(folder)
                node = node.children[folder]

        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            subs = []
            for child in sorted(node.children):
                subs.append(child + '(' + serialize(node.children[child]) + ')')
            serial = ''.join(subs)
            serial_map[serial].append(node)
            return serial
        
        serialize(root)

        to_delete = set()

        def mark_delete(node):
            to_delete.add(node)
            for c in node.children.values():
                mark_delete(c)

        for serial, nodes in serial_map.items():
            if serial and len(nodes) > 1:
                for node in nodes:
                    if node not in to_delete:
                        mark_delete(node)

        res = []

        def collect(node, path):
            if node != root and node not in to_delete:
                res.append(path + [node.name])
            for child in node.children.values():
                collect(child, path + ([] if node == root else [node.name]))
        
        collect(root, [])
        return res