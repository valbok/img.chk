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

    matcher = Matcher()
    fn1 = sys.argv[1]
    img1 = Image.read( fn1 )
    m = ( img1.width + img1.height ) / 2
    kp1, desc1 = cv2.ORB(m).detectAndCompute( img1.img, None )
    e1 = Extractor( img1, kp1, desc1 )
    imgs1 = e1.binImages()
    imgs1.append( img1 )
    print "[" + str( len( imgs1 ) ) + "]", fn1

    fn2 = sys.argv[2]
    img2 = Image.read( fn2 )
    m = ( img2.width + img2.height ) / 2
    kp2, desc2 = cv2.ORB(m).detectAndCompute( img2.img, None )
    e2 = Extractor( img2, kp2, desc2 )
    imgs2 = e2.binImages()
    imgs2.append( img2 )
    print "[" + str( len( imgs2 ) ) + "]", fn2

    d = 7
    matches = matcher.match( imgs1, imgs2, d )

    print "Total matches = ", len(matches)

    #p = [m.type for m in matches if m.type == "PHash"]
    #print "p", len(p)
