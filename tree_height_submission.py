# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:17:11 2019

@author: rcurran
"""
import sys
import threading

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size

class TreeNode():
    child_nodes = []
    parent_index = None
    
    def __init__(self, child_nodes, parent_index, index):
        self.child_nodes = child_nodes
        self.parent_index = parent_index
        
def compute_height_fast(n, parents):
    
    root = construct_tree(n, parents)
    
    return get_height_recursive(root)
    
def get_height_recursive(tree):
    if not tree:
        return 0
    
    if not tree.child_nodes:
        return 1
    
    heights = []
    for node in tree.child_nodes:
        heights.append(1 + get_height_recursive(node))
        
    return max(heights)

def construct_tree(n, parents):
    treeNodes = []
    for i in range(n):
        treeNodes.append(TreeNode([], parents[i], i))
    
    root = None
    for i in range(n):
        parent_index = treeNodes[i].parent_index
        if parent_index == -1:
            root = treeNodes[i]
        else:
            treeNodes[parent_index].child_nodes.append(treeNodes[i])
    
    if root is None:
        print("Root is null")
    return root
    
def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height_fast(n, parents))
    
threading.Thread(target=main).start()