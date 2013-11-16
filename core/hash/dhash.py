"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import numpy as np
import cv2
from hash import *

"""
" Implements difference hash
"""
class DHash( Hash ):

    """
    " @return int
    """
    def _calculate( self ):
        img = self._img.grayscale().resize( (8, 8), cv2.INTER_AREA )

        previous = img.pixel( 7, 7 )
        result = 0
        for row in xrange( 8 ):
            for col in xrange( 8 ):
                result <<= 1
                pixel = img.pixel( col, row )
                result |= 1 * ( pixel >= previous )
                previous = pixel

        return result

    def __eq__( self, h ):
        return Hash.hammingDistance( self._value, h._value ) <= 11
