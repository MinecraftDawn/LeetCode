# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial = ""
        queue = [[root],[]]
        
        while queue[0]:
            curNode = queue[0].pop(0)
            if curNode:
                serial += "," + str(curNode.val)
                queue[1].append(curNode.left)
                queue[1].append(curNode.right)
            else:
                serial += ",N"
            
            if not queue[0]:
                queue[0],queue[1] = queue[1],queue[0]
                    
            
        return serial
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        preRoot = TreeNode(0)
        queue = [preRoot]
        data = ['N'] + data[1:].split(",")
        
        nodeIndex = 0
        
        while queue:
            curNode = queue.pop(0)
            if data[nodeIndex] == "N":
                createdNode = None
            else:
                createdNode = TreeNode(int(data[nodeIndex]))
                queue.append(createdNode)
            nodeIndex += 1
            curNode.left = createdNode
            
            if data[nodeIndex] == "N":
                createdNode = None
            else:
                createdNode = TreeNode(int(data[nodeIndex]))
                queue.append(createdNode)
            nodeIndex += 1
            curNode.right = createdNode
        
            
        return preRoot.right
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))