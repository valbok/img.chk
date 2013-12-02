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
" Implements average hash
"""
class AHash( Hash ):

    """
    " @return int
    """
    def _calculate( self ):
        img = self._img.grayscale().resize( (8, 8), cv2.INTER_AREA )
        averageValue = 0
        for row in xrange( 8 ):
            for col in xrange( 8 ):
                averageValue += img.pixel( col, row )

        averageValue /= 64
        result = int64()
        for row in xrange( 8 ):
            for col in xrange( 8 ):
                result <<= 1
                result |= 1 * ( img.pixel( col, row ) >= averageValue )

        return result

    """
    " @return bool
    """
    def __eq__( self, h ):
        return self.distanceTo( h ) <= 10
