"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

from ahash import *
from dhash import *
from phash import *
from match import *

"""
" Matches 2 images using hashes
"""
class Matcher( object ):

    """
    " @var []
    """
    _hashes = []

    """
    " @param Image
    """
    def __init__( self, hashes = [PHash, DHash, AHash] ):
        self._hashes = hashes

    """
    " @return Match[]
    """
    def match( self, imgs1, imgs2, distance = None ):
        result = []
        hashes1 = self.hashes( imgs1 )
        hashes2 = self.hashes( imgs2 )
        for ht in hashes1:
            hs1 = hashes1[ht]
            hs2 = hashes2[ht]
            for h1 in hs1:
                for h2 in hs2:
                    matched = h1 == h2 if distance == None else h1.distanceTo( h2 ) <= distance
                    if matched:
                        result.append( Match( h1, h2 ) )

        return result

    """
    " Excludes duplicates
    "
    " @return {}
    " @example print Matcher( PHash ).hashes( imgs1 )[PHash]
    """
    def hashes( self, imgs ):
        result = {}
        for h in self._hashes:
            if h not in result:
                result[h] = []

            for i in imgs:
                hash = h( i )
                found = False
                for sh in result[h]:
                    if sh == hash:
                        found = True
                        break

                if not found:
                    result[h].append( hash )

        return result
