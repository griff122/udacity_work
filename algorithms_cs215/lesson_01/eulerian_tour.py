
"""
This program is designed to find the eulerian tour of a supplied graph.

A Eulerian tour is a path through a graph in which all edges are used, 
    every node is touched, and the last node of the path is the same as
    the starting node.

The graph is a list of tuples representing the edges between nodes.
Example: [(1,2), (2,3), (3,1)]
    This represents a graph with three nodes and three edges.
    An edge between node 1 and node 2, between node 2 and node 3, and
       node 3 and node 1.
"""


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

    def get_eulerian_tours(self):
        """ Function to get the paths which are eulerian tours """
        leaves = self.get_leaf_nodes(self.root)
        eulerian_tours = []
        for node in leaves:
            if node.node_id == self.root_node_id and len(node.current_path) == len(self.graph):
                tmp_node = node
                tour = []
                while tmp_node != None:
                    tour.insert(0,tmp_node.node_id)
                    tmp_node = tmp_node.parent
                eulerian_tours.append(tour)
                #eulerian_tours.append(node.current_path)
        return eulerian_tours

    def get_leaf_nodes(self,node):
        if len(node.children) == 0: # Leaf
            return [node]
        leaves = []
        for child in node.children:
            leaves.extend(self.get_leaf_nodes(child))
        return leaves

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
    nodeTree.buildTree()
    nodeTree.printTree()
    print "\n Eulerian Tours:"
    for tour in nodeTree.get_eulerian_tours():
        print tour

    print "\n------------------------------------------\n"
    input_2 = [(0,1), (1,5), (1,7), (4,5), (4,8), (1,6), (3,7), (5,9), (2,4), (0,4), (2,5), (3,6), (8,9)]
    print "Tree for graph:",input_2
    nodeTree = NodeTree(0,input_2)
    nodeTree.buildTree()
    #nodeTree.printTree()
    print "\n Eulerian Tours:"
    for tour in nodeTree.get_eulerian_tours():
        print tour




