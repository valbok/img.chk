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
    " @var Image
    " @see parent()
    """
    _parent = False

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
    @property
    def shape( self ):
        return self._img.shape

    """
    " @return int
    """
    @property
    def width( self ):
        return self.shape[1]

    """
    " @return int
    """
    @property
    def height( self ):
        return self.shape[0]

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

    """
    " @return {img, x, y}
    """
    def parent( self, parent = False, x = False, y = False ):
        if x or y:
            self._parent = {"img": parent, 'x': int( x ), 'y': int( y )}
            return self

        return self._parent

    """
    " @return Image
    """
    def crop( self, x1, y1, x2, y2 ):
        cropped = self._img[y1:y2, x1:x2]
        if len( cropped ) == 0:
            return False

        i = Image( cropped )
        i.parent( self, x1, y1 )

        return i
