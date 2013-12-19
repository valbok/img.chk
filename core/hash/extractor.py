"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import numpy as np
import cv2
from core import *

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
    def extract( self, krange = (0, 30), attempts = 100, multiples= ((4, 4), (4, 4)) ):
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
                    x = v[0]
                    y = v[1]
                    if x < miX:
                        miX = x
                    if y < miY:
                        miY = y
                    if x > maX:
                        maX = x
                    if y > maY:
                        maY = y

                dmiX = int( centroid[0] - miX )
                dmiY = int( centroid[1] - miY )
                dmaX = int( abs(centroid[0] - maX) )
                dmaY = int( abs(centroid[1] - maY) )

                # This is a magic which helps to compare subimages using hashes
                while dmiX % multiples[0][0] != 0:
                    dmiX -= 1

                while dmiY % multiples[0][1] != 0:
                    dmiY -= 1

                while dmaX % multiples[1][0] != 0:
                    dmaX += 1

                while dmaY % multiples[1][1] != 0:
                    dmaY += 1

                miX = int( centroid[0] - dmiX )
                miY = int( centroid[1] - dmiY )
                maX = int( centroid[0] + dmaX )
                maY = int( centroid[1] + dmaY )

                cropped = img.crop( miX, miY, maX, maY )
                if not cropped or cropped.width < 32 or cropped.height < 32:
                    continue

                result.append( cropped )

        return result
