"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import numpy as np
import cv2
from core import *

"""
" Extracts sub images
"""
class ImageExtractor( object ):

    """
    " @var Image
    """
    _img = False

    """
    " @var []
    """
    _keypoints = []

    """
    " @param Image
    " @param []
    """
    def __init__( self, img, keypoints ):
        self._img = img
        self._keypoints = keypoints

    """
    " @param ()
    " @return Images[]
    """
    def extract( self, krange = (0, 25) ):
        result = []
        height, width, channel = self._img.shape()
        kp = self._keypoints
        klen = len( kp )
        hashes = []
        Z = []
        for k in kp:
            Z.append( [k.pt[0], k.pt[1]] )

        Z = np.float32( Z )
        for clustersCount in xrange( krange[0], krange[1] ):
            if clustersCount == 0:
                result.append( self._img )
                continue

            ret, label, center = cv2.kmeans( Z, K=clustersCount, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER, 1, 10), attempts=100, flags=cv2.KMEANS_PP_CENTERS )

            for k in xrange( clustersCount ):
                img = self._img.img.copy()

                cluster = Z[label.ravel()==k]
                centroid = center[k]

                miX = min( v[0] for v in cluster )
                miY = min( v[1] for v in cluster )
                maX = max( v[0] for v in cluster )
                maY = max( v[1] for v in cluster )

                #print "miX", miX
                #print "miY", miY
                #print "maX", maX
                #print "maY", maY

                w = abs(maX - miX)
                h = abs(maY - maX)
                #print "w", w
                #print "h", h
                if h < 32 or w < 32:
                    continue

                cy1 = miY
                cy2 = maY
                cx1 = miX
                cx2 = maX

                cropped = img[cy1:cy2, cx1:cx2]
                if len( cropped ) == 0:
                    continue

                result.append( Image( cropped ) )

        return result
