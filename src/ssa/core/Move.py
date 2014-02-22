
from TeXableEntity import TeXableEntity
class Move(TeXableEntity):
    """A function from G, v -> G'

    Create an action like so:
    
        >>> action = Move(lambda G, v: v['marked'] = True,
                            'v.marked \gets True',
                            'Marks $v$')
    
    You can retrieve the documentation and TeX representation of the
    object as you would a `TeXableEntity`:
    
        >>> action.doc
        'Mark $v$'
        >>> action.TeX
        'v.marked \gets True'
    
    You can also *call* `Move` objects, passing a graph and node as
    arguments.  This functionality is deferred to the member function
    `Move.action`.
    """
    #% move %#
    def __init__(self, move = lambda node, neighborhood: node, neighborhood,
                       as_TeX = None,
                       doc    = None):
        TeXableEntity.__init__(self, as_TeX, doc)
        self.move = move

    def __call__(self, graph, node):
        return self.move(graph, node)
    #% endmove %#