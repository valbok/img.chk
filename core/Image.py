"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import numpy
import cv2
import cPickle as pickle

"""
" Base class to handle image comparisons
"""
class Image( object ):
    _keypoints = []
    _descriptors = []

    def __init__( self ):
        pass

    """
    " @return (Image) By image filename
    """
    @staticmethod
    def get( filename ):
        img = Image()
        img._img = cv2.imread( filename, 0 )
        if img._img is None:
            raise Exception( 1, "Could not open file" )

        surf = cv2.SURF( 400 )
        img._keypoints, img._descriptors = surf.detectAndCompute( img._img, None )

        return img

    @staticmethod
    def _toArray( keypoints, descriptors ):
        result = []
        i = 0
        for point in keypoints:
            temp = ( point.pt, point.size, point.angle, point.response, point.octave, point.class_id, descriptors[i] )
            ++i
            result.append( temp )

        return result

    @staticmethod
    def _fromArray( array ):
        keypoints = []
        descriptors = []
        for point in array:
            temp_feature = cv2.KeyPoint( x = point[0][0], y = point[0][1], _size = point[1], _angle = point[2], _response = point[3], _octave = point[4], _class_id = point[5] )
            temp_descriptor = point[6]
            keypoints.append( temp_feature )
            descriptors.append( temp_descriptor )

        return keypoints, numpy.array( descriptors )

    """
    " @return (array)
    """
    def serialize( self ):
        return Image._toArray( self._keypoints, self._descriptors )

    """
    " @return (Image)
    " @see serialize()
    """
    @staticmethod
    def unserialize( array ):
        img = Image()
        img._keypoints, img._descriptors = Image._fromArray( array )

        return img

    """
    " @return (Image)
    """
    def dumpToFile( self, fn ):
        pickle.dump( self.serialize(), open( fn, "wb" ) )

        return self

    """
    " @return (string)
    """
    def dump( self ):
        return pickle.dumps( self.serialize() )

    """
    " @return (Image)
    """
    @staticmethod
    def loadFromFile( fn ):
        db = pickle.load( open( fn, "rb" ) )

        return Image.unserialize( db )

    """
    " @return (Image)
    """
    @staticmethod
    def load( st ):
        db = pickle.loads( st )
        return Image.unserialize( db )

    """
    " @return (zip)
    """
    @staticmethod
    def _filterMatches( kp1, kp2, matches, ratio = 0.75 ):
        mkp1, mkp2 = [], []
        for m in matches:
            if len( m ) == 2 and m[0].distance <= m[1].distance * ratio:
                m = m[0]
                mkp1.append( kp1[m.queryIdx] )
                mkp2.append( kp2[m.trainIdx] )

        pairs = zip( mkp1, mkp2 )

        return pairs

    def _match( self, img ):
        matcher = cv2.BFMatcher( cv2.NORM_L2 )
        kp1 = self._keypoints
        desc1 = self._descriptors
        kp2 = img._keypoints
        desc2 = img._descriptors
        matches = matcher.knnMatch( desc1, trainDescriptors = desc2, k = 2 )
        pairs = Image._filterMatches( kp1, kp2, matches )

        return pairs

    """
    " @return (float)
    """
    def compareInPercent( self, img ):
        pairs = self._match( img )
        l1 = len( self._keypoints )
        l2 = len( img._keypoints )
        lp = len( pairs )
        r = ( lp * 100 ) / l1

        return r

    """
    " @return (bool)
    """
    def looksLike( self, img ):
        p12 = self.compareInPercent( img )
        p21 = img.compareInPercent( self )

        return p12 > 40 or p21 > 40
