
import time
import copy

########################################
# Functions that don't belong to a class
########################################
def get_unique_nodes(graph):
    """ Function to get the unique nodes in a graph [list of tuples] """
    return list(set(reduce(lambda x,y: x+y, graph)))    


########################################
# Classes
########################################
class NodeTree():
    """ Node tree will hold nodes """
    def __init__(self,root_node_id,graph):
        self.root_node_id = root_node_id # Only supply the ID of the node, and let the class handle the rest
        self.graph = graph
        self.root = None
        self.setUp()
        self.buildTree()

    def setUp(self):
        """ Function to setup the initial tree (root node) before populating """
        #root_edges = self.find_node_edges(self.root_node_id)
        #root_children = self.get_children_from_edges(self.root_node_id,root_edges)
        self.root = Node(self.root_node_id,parent_node=None,children_nodes=None,current_path=None)

    def get_children_from_edges(self,node_id,edges):
        """ Function to get the children from the edges (who are not the node id) """
        return [edge[edge[0] == node_id] for edge in edges]

    def find_node_edges(self,node_id):
        """ Function to get the possible edges for a node """
        return [edge for edge in self.graph if node_id in edge]

    def buildTree(self):
        """ Fuction to build the tree. Starting from the already created root node. """
        self.rec_buildTree(self.root)

    def rec_buildTree(self,node,curr_path=None,parent_node=None):
        """ Function to recursively build the tree """
        if curr_path == None:
            curr_path = []
        # Get the current_node edges to children
        edges = self.find_node_edges(node.node_id)
        # Remove existing tuples
        edges = [edge for edge in edges if edge not in curr_path]
        # Check to make sure that any edges exist
        if len(edges) == 0:
            return
        # For each edge, add a child node
        for edge in edges:
            child_id = edge[edge[0] == node.node_id]
            new_path = curr_path + [edge]
            node.children.append(Node(child_id, node, current_path = new_path))
            self.rec_buildTree(node.children[-1],new_path)
        return

    def printTree(self):
            print self.root.node_id
            level = 1
            self.printNodes(self.root.children,level)

    def printNodes(self,nodes,level):
        for node in nodes:
            print "|"*(level) + "-", node.node_id
            self.printNodes(node.children,level+1)

class Node():
    """ Node class will contain information for each node to be used by the tree """
    def __init__(self, node_id, parent_node = None, children_nodes = None, current_path = None):
        self.node_id = node_id
        self.parent = parent_node
        if children_nodes == None:
            children_nodes = []
        self.children = children_nodes
        if current_path == None:
            current_path = []
        self.current_path = current_path


if __name__ == "__main__":
    input_1 = [(1,2),(2,3),(3,1)]
    print "Tree for graph:",input_1
    nodeTree = NodeTree(1,input_1)
    nodeTree.printTree()

    print "\n------------------------------------------\n"
    input_2 = [(0,1), (1,5), (1,7), (4,5), (4,8), (1,6), (3,7), (5,9), (2,4), (0,4), (2,5), (3,6), (8,9)]
    print "Tree for graph:",input_2
    nodeTree = NodeTree(1,input_2)
    nodeTree.printTree()




