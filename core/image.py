"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import cv2

"""
" Base class to handle image comparisons
"""
class Image( object ):

    """
    " @var np.array
    """
    _img = False

    """
    " @param np.array
    """
    def __init__( self, img ):
        self._img = img

    """
    " @return Image
    """
    @staticmethod
    def read( filename, channel = 1 ):
        i = cv2.imread( filename, channel )
        if i is None:
            raise Exception( "Could not read file: ", filename )

        return Image( i )

    """
    " @return Image
    """
    def grayscale( self ):
        return Image( cv2.cvtColor( self._img, cv2.COLOR_BGR2GRAY ) )

    """
    " @return Image
    """
    def resize( self, size, inter = cv2.INTER_NEAREST ):
        return Image( cv2.resize( self._img, size, interpolation=inter ) )

    """
    " @return (height, width)
    """
    def shape( self ):
        return self._img.shape

    """
    " @return np.array
    """
    @property
    def img( self ):
        return self._img

    """
    " @return int
    """
    def pixel( self, x, y ):
        return self._img[x,y]
