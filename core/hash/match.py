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
        self._h1 = h1
        self._h2 = h2

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
