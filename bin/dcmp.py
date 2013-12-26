#!/usr/bin/env python
"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

"""
" Compares 2 images using hashes
"""
import sys
import os
parentdir = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
os.sys.path.insert( 0, parentdir )

from core import *

if __name__ == '__main__':
    if len( sys.argv ) < 3:
        sys.exit( 1 )

    cv = cv2.SURF( 400 )
    matcher = Matcher()

    fn1 = sys.argv[1]
    img1 = Image.read( fn1 )
    kp1, desc1 = cv.detectAndCompute( img1.img, None )
    e1 = Extractor( img1, kp1, desc1 )
    imgs1 = e1.descImages()
    print "[" + str( len( imgs1 ) ) + ":" + str( len( matcher.hashes( imgs1 )[PHash] ) ) + "]", fn1

    fn2 = sys.argv[2]
    img2 = Image.read( fn2 )
    kp2, desc2 = cv.detectAndCompute( img2.img, None )
    e2 = Extractor( img2, kp2, desc2 )
    imgs2 = e2.descImages()
    print "[" + str( len( imgs2 ) ) + ":" + str( len( matcher.hashes( imgs2 )[PHash] ) ) + "]", fn2

    d = 1
    matches = matcher.match( imgs1, imgs2, d )

    print len(matches)

    d = [m.type for m in matches if m.type == "DHash"]
    a = [m.type for m in matches if m.type == "AHash"]
    p = [m.type for m in matches if m.type == "PHash"]
    print "a", len(a)
    print "d", len(d)
    print "p", len(p)
