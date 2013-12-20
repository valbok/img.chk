"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import numpy as np
import cv2
from core import *
from matplotlib import pyplot as plt

"""
" Extracts sub images from an image
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
    def extract( self, krange = (0, 30), attempts = 10, multiples = (32, 32) ):
        result = []
        height, width, channel = self._img.shape
        kp = self._keypoints
        Z = []
        for k in kp:
            Z.append( [k.pt[0], k.pt[1]] )

        Z = np.float32( Z )

        for clustersCount in xrange( krange[0], krange[1] ):
            if clustersCount == 0:
                result.append( self._img.parent( self._img, 0, 0 ) )
                continue

            ret, label, center = cv2.kmeans( Z, K=clustersCount, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER , 1, 10), attempts=attempts, flags=cv2.KMEANS_PP_CENTERS )
            for k in xrange( clustersCount ):
                centroid = center[k]
                img = self._img
                cluster = Z[label.ravel()==k]

                miX = miY = 99999
                maX = maY = 0
                for v in cluster:
                    x = int( v[0] )
                    y = int( v[1] )

                    if x < miX:
                        miX = x
                    if y < miY:
                        miY = y
                    if x > maX:
                        maX = x
                    if y > maY:
                        maY = y

                t = True

                while ( maX - miX ) % multiples[0] != 0:
                    if t:
                        miX -= 1
                    else:
                        maX += 1

                    t = not t

                while ( maY - miY ) % multiples[1] != 0:
                    if t:
                        miY -= 1
                    else:
                        maY += 1

                    t = not t

                cropped = img.crop( miX, miY, maX, maY )
                if not cropped or cropped.width < 64 or cropped.height < 64:
                    continue

                result.append( cropped )

        return result
