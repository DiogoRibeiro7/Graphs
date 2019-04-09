'''
Uses a recursively called simple generator (with the same arguments as the outer call!) to traverse a tree in breadth first order.
'''

def breadth_first(tree,children=iter):
    """Traverse the nodes of a tree in breadth-first order.
    The first argument should be the tree root; children
    should be a function taking as argument a tree node and
    returning an iterator of the node's children.
    """
    yield tree
    last = tree
    for node in breadth_first(tree,children):
        for child in children(node):
            yield child
            last = child
        if last == node:
            return
            
            
'''
Iterative deepening. It appears that this recipe performs the same sequence of node expansions 
(that is, calls to children) as Korf's depth-first iterative deepening algorithm:
'''           
            
def dfid(T,children,callback):
    def visit(node,i):
        if i == 0:
            callback(node)
        else:
            for c in children(node):
                visit(c,i-1)
    i = 0
    while 1:
        visit(T,i)
        i += 1
        
        
        
'''
Here is an implementation of a breadth-first search, which also returns an iterator object as above, but which uses the 
standard queue algorithm:
'''
def bfs(root,visitable,children=iter):
    """Iterator traverses a tree in breadth-first order.

    The first argument should be the tree root; visitable should be an
    iterable with all searchable nodes; children should be a function
    which takes a node and return an iterator of the node's children.
    """
    queue = []
    # makes a shallow copy, makes it a collection, removes duplicates
    unvisited = list(set(visitable))

    if root in unvisited:
        unvisited.remove(root)
        queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        yield node

        for child in children(node):
            if child in unvisited:
                unvisited.remove(child)
                queue.append(child)
    return
