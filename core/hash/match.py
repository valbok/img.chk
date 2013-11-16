"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

"""
" Wrapper for 2 hashes to check similarity
"""
class Match( object ):

    """
    " @var Hash
    """
    _h1 = False

    """
    " @var Hash
    """
    _h2 = False

    """
    " @param Hash
    " @param Hash
    """
    def __init__( self, h1, h2 ):
        if h1.__class__.__name__ != h2.__class__.__name__:
            raise TypeError( "Hashes must have the same types" )

        self._h1 = h1
        self._h2 = h2

    """
    " @var (Hash, Hash)
    """
    @property
    def hashes( self ):
        return (self._h1, self._h2)

    """
    " @var str
    """
    @property
    def type( self ):
        return self._h1.__class__.__name__

    """
    " @return int
    """
    @property
    def distance( self ):
        return self._h1.distanceTo( self._h2 )

    """
    " @return bool
    """
    def matched( self ):
        return self._h1 == self._h2
