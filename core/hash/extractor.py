"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import numpy as np
import cv2
from core import *
import math

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
    def descImages( self ):
        result = []
        Z = []
        kp = self._keypoints
        desc = self._descriptors
        lkp = len( kp )
        for ki in xrange( lkp ):
            k = kp[ki]
            ds = desc[ki]
            rows = Extractor._dscImage( ds )

            im = np.float32( rows )
            img = Image( im )
            result.append( img )

        return result

    def nearestDescImages( self ):
        result = []
        kp = self._keypoints
        desc = self._descriptors
        lkp = len( kp )
        Z = []
        descs = {}
        for ki in xrange( lkp ):
            k = kp[ki]
            Z.append( [k.pt[0], k.pt[1], desc[ki]] )

        for zi in xrange( lkp ):
            z = Z[zi]
            x1 = z[0]
            y1 = z[1]
            d1 = z[2]
            mp = []
            for i in xrange( 4 ):
                mp.append( [99999, [0,0], []] )

            for fi in xrange( zi + 1, lkp ):
                f = Z[fi]
                x2 = f[0]
                y2 = f[1]
                d2 = f[2]
                c = math.hypot( x2 - x1, y2 - y1 )
                m1 = mp[0]
                if x2 <= x1 and y2 >= y1 and c < mp[0][0]:
                    mp[0][0] = c
                    mp[0][1] = [x2,y2]
                    mp[0][2] = d2

                if x2 > x1 and y2 > y1 and c < mp[1][0]:
                    mp[1][0] = c
                    mp[1][1] = [x2,y2]
                    mp[1][2] = d2

                if x2 < x1 and y2 < y1 and c < mp[2][0]:
                    mp[2][0] = c
                    mp[2][1] = [x2,y2]
                    mp[2][2] = d2

                if x2 > x1 and y2 < y1 and c < mp[3][0]:
                    mp[3][0] = c
                    mp[3][1] = [x2,y2]
                    mp[3][2] = d2


            rows = []

            ds = Extractor._dscImage( d1 )
            m1 = ds[0:8,0:8]
            m2 = ds[0:8,8:16]
            m3 = ds[8:16,0:8]
            m4 = ds[8:16,8:16]

            r1 = m1
            if len( mp[0][2] ):
                d22 = Extractor._dscImage(mp[0][2])
                for i in xrange( 8 ):
                    for j in xrange( 8 ):
                        v1 = m1[i][j]
                        v2 = d22[i][j]
                        v1 = int(round(abs( v1 )))
                        v2 = int(round(abs( v2 )))
                        r = v1 ^ v2
                        r1[i][j] = r

            r2 = m2
            if len( mp[1][2] ):
                d22 = Extractor._dscImage(mp[1][2])
                for i in xrange( 8 ):
                    for j in xrange( 8 ):
                        v1 = m2[i][j]
                        v2 = d22[i][j]
                        v1 = int(round(abs( v1 )))
                        v2 = int(round(abs( v2 )))
                        r = v1 ^ v2
                        r2[i][j] = r

            r3 = m3
            if len( mp[2][2] ):
                d22 = Extractor._dscImage(mp[2][2])
                for i in xrange( 8 ):
                    for j in xrange( 8 ):
                        v1 = m3[i][j]
                        v2 = d22[i][j]
                        v1 = int(round(abs( v1 )))
                        v2 = int(round(abs( v2 )))
                        r = v1 ^ v2
                        r3[i][j] = r

            r4 = m4
            if len( mp[3][2] ):
                d22 = Extractor._dscImage(mp[3][2])
                for i in xrange( 8 ):
                    for j in xrange( 8 ):
                        v1 = m4[i][j]
                        v2 = d22[i][j]
                        v1 = int(round(abs( v1 )))
                        v2 = int(round(abs( v2 )))
                        r = v1 ^ v2
                        r4[i][j] = r

            for i in xrange( 8 ):
                rows.append( r1[i] + r2[i] )

            for i in xrange( 8 ):
                rows.append( r3[i] + r4[i] )

            im = np.float32( rows )
            img = Image( im )
            result.append( img )

        return result

    """
    " @param [] Descriptors
    " @return []
    """
    @staticmethod
    def _dscImage( ds ):
        rows = []
        rs = [ds[i:i + 8] for i in range( 0, len( ds ), 8 )]

        b = []
        row = []
        m = 255
        for r in rs:
            item = [r[0]*m, 0     , r[2]*m, 0,\
                    0     , r[1]*m, 0     , r[3]*m,\
                    0     , r[5]*m, 0     , r[7]*m,\
                    r[4]*m, 0     , r[6]*m, 0]

            row.append( item )
            if len( row ) != 4:
                continue

            res1=[]
            res2=[]
            res3=[]
            res4=[]
            for rr in row:
                res1 += rr[0:4]
                res2 += rr[4:8]
                res3 += rr[8:12]
                res4 += rr[12:16]

            rows.append( res1 )
            rows.append( res2 )
            rows.append( res3 )
            rows.append( res4 )
            row = []

        return np.array( rows, np.float64 )
