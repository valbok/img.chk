#!/usr/bin/env python
"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

"""
" Compares 2 images using surf
"""

import sys
import os
parentdir = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
os.sys.path.insert( 0, parentdir )

import cv2
from core import *

def filterMatches( kp1, kp2, matches, ratio = 0.75 ):
    mkp1, mkp2 = [], []
    for m in matches:
        if len( m ) == 2 and m[0].distance < m[1].distance * ratio:
            m = m[0]
            mkp1.append( kp1[m.queryIdx] )
            mkp2.append( kp2[m.trainIdx] )

    pairs = zip( mkp1, mkp2 )

    return pairs

if __name__ == '__main__':
    if len( sys.argv ) < 3:
        sys.exit( 1 )

    fn1 = sys.argv[1]
    img1 = Image.read( fn1 )
    cv = cv2.SURF( 400 )
    kp1,desc1 = cv.detectAndCompute( img1.img, None )

    fn2 = sys.argv[2]
    img2 = Image.read( fn2 )
    kp2,desc2 = cv.detectAndCompute( img2.img, None )

    matcher = cv2.BFMatcher( cv2.NORM_L2 )
    matches = matcher.knnMatch( desc1, trainDescriptors = desc2, k = 2 )
    pairs = filterMatches( kp1, kp2, matches )

    l1 = len( kp1 )
    l2 = len( kp2 )
    lp = len( pairs )
    r = ( lp * 100 ) / l1

    print r, "%"

