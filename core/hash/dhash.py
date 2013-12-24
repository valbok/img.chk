"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import numpy as np
import cv2
from hash import *
from numpy import int64

"""
" Implements difference hash
"""
class DHash( Hash ):

    """
    " @return int
    """
    def _calculate( self ):
        g = type(self._img.pixel( 0, 0 )) == np.ndarray
        img = self._img
        if g:
            img = img.grayscale()

        img = img.resize( (8, 8), cv2.INTER_AREA )

        previous = img.pixel( 7, 7 )
        result = int64()
        for row in xrange( 8 ):
            for col in xrange( 8 ):
                result <<= 1
                pixel = img.pixel( col, row )
                result |= 1 * ( pixel >= previous )
                previous = pixel

        return result

    """
    " @return bool
    """
    def __eq__( self, h ):
        return self.distanceTo( h ) <= 11
