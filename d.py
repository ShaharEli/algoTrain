class Node:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        
    def __str__(self):
        return "(" + str(self.left) + " " + str(self.data) + " " + str(self.right) + ")"
        
def sink_nodes(root):
    if not root:
        return
    sink_nodes(root.left)
    sink_nodes(root.right)
    if root.data == 0:
        sink_nodes_helper(root)
    return root
    
def sink_nodes_helper(root):
    if not root.left and not root.right:
        return
    else:
        if root.data == 0:
            if root.left:
                if root.left.data != 0:
                    root.data, root.left.data = root.left.data, root.data
                    sink_nodes_helper(root.left)
                else:
                    sink_nodes_helper(root.left)

            elif root.right:
                if root.right.data != 0:
                    root.data, root.right.data = root.right.data, root.data
                    sink_nodes_helper(root.right)
                else:
                    sink_nodes_helper(root.right)

        else:
            if root.left:
                sink_nodes_helper(root.left)
            if root.right:
                sink_nodes_helper(root.right)

t = Node(0, Node(0, Node(1)), Node(0, Node(0, Node(6), Node(4)), Node(2, None, Node(3))))

x = sink_nodes(t)
print(x)
print(t)