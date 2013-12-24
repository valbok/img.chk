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
class Extractor( object ):

    """
    " @var Image
    """
    _img = False

    """
    " @var []
    """
    _keypoints = []

    """
    " @var []
    """
    _descriptors = []

    """
    " @param Image
    " @param []
    " @param []
    """
    def __init__( self, img, keypoints, descriptors = [] ):
        self._img = img
        self._keypoints = keypoints
        self._descriptors = descriptors

    """
    " @param ()
    " @return Images[]
    """
    def subImages( self, krange = (0, 20), attempts = 100, multiples = 8 ):
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

                dmiX = int( centroid[0] - miX );
                dmiY = int( centroid[1] - miY );
                dmaX = int( centroid[0] + maX );
                dmaY = int( centroid[1] + maY );

                while dmiX % multiples != 0:
                    dmiX -= 1

                while dmaX % multiples != 0:
                    dmaX += 1

                while dmiY % multiples != 0:
                    dmiY -= 1

                while dmaY % multiples != 0:
                    dmaY += 1

                miX = dmiX
                maX = dmaX
                miY = dmiY
                maY = dmaY

                cropped = img.crop( miX, miY, maX, maY )
                if not cropped or cropped.width < 32 or cropped.height < 32:
                    continue

                result.append( cropped )

        return result

    """
    " @return []
    """
    def descImages( self, draw = False ):
        result = []
        Z = []
        kp = self._keypoints
        desc = self._descriptors
        lkp = len( kp )
        kdesc = {}
        for ki in xrange( lkp ):
            k = kp[ki]
            Z.append( [k.pt[0], k.pt[1]] )
            ds = desc[ki]
            kdesc[(k.pt[0], k.pt[1])] = [(d*255,d*255,d*255) for d in ds]

        Z = np.float32( Z )
        clustersCount = int( len( Z ) / 8 )
        attempts = 100
        ret, label, center = cv2.kmeans( Z, K=clustersCount, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER , 1, 10), attempts=attempts, flags=cv2.KMEANS_PP_CENTERS )
        for k in xrange( clustersCount ):
            centroid = center[k]
            cluster = Z[label.ravel()==k]
            block = []
            for c in cluster:
                ds = kdesc[(c[0],c[1])]
                rs = [ds[i:i+4] for i in range(0, len(ds), 4)]

                b = []
                row = []
                rows = []
                t = True
                for r in rs:
                    if not t:
                        r.reverse()
                    b.append( r )
                    t = not t
                    if t:
                        row.append( b )
                        b = []
                        res = []
                        if len(row) == 4:
                            res1=[]
                            res2=[]
                            for r in row:

                                for bb in r[0]:
                                    res1.append(bb)
                                for bb in r[1]:
                                    res2.append(bb)

                            rows.append(res1)
                            rows.append(res2)
                            row = []


                im = np.float32( rows )
                img = Image( im )
                result.append( img )

        return result
