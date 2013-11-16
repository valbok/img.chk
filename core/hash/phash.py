"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import numpy as np
import cv2
from hash import *

"""
" Implements perceptual hash using DCT
"""
class PHash( Hash ):

    """
    " @return int
    """
    def _calculate( self ):
        img = self._img.grayscale().resize( (32, 32), cv2.INTER_NEAREST )
        imf = np.float32( img._img ) / 255.0
        dsty = cv2.dct( imf )[0:8]
        dst = []
        for i in xrange( len( dsty ) ):
            dst.append( dsty[i][0:8] )

        c = a = 0
        for j in xrange( len( dst ) ):
            y = dst[j]
            for i in xrange( len( y ) ):
                if i == 0 and j == 0:
                    continue

                c += 1
                a += y[i]

        median = a / c
        result = 0
        for row in xrange( 8 ):
            for col in xrange( 8 ):
                result <<= 1
                result |= 1 * ( dst[col][row] > median )

        return result

    """
    " @return bool
    """
    def __eq__( self, h ):
        return self.distanceTo( h ) <= 11


