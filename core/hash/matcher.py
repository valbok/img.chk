"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

from dhash import *
from phash import *
from match import *

"""
" Matches 2 images using hashes
"""
class Matcher( object ):

    _hashes = []

    """
    " @param Image
    """
    def __init__( self, hashes = [PHash, DHash] ):
        self._hashes = hashes

    """
    " @return Match[]
    """
    def match( self, imgs1, imgs2, distance = False ):
        result = []
        for i1 in imgs1:
            hashes1 = []
            for h in self._hashes:
                hashes1.append( h( i1 ) )

            for i2 in imgs2:
                hashes2 = []
                for h in self._hashes:
                    hashes2.append( h( i2 ) )

                for h1 in hashes1:
                    for h2 in hashes2:
                        matched = h1 == h2 if distance == False else h1.distanceTo( h2 ) <= distance
                        if matched:
                            result.append( Match( h1, h2 ) )

        return result
