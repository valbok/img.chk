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

import json
from core import *

if __name__ == '__main__':
    if len( sys.argv ) < 3:
        sys.exit( 1 )

    fn1 = sys.argv[1]
    img1 = Image.read( fn1 )
    cv = cv2.SURF( 400 )
    kp1 = cv.detect( img1.img, None )
    imgs1 = ImageExtractor( img1, kp1 ).extract()

    print "imgs1 len", len( imgs1 )

    fn2 = sys.argv[2]
    img2 = Image.read( fn2 )
    kp2 = cv.detect( img2.img, None )
    imgs2 = ImageExtractor( img2, kp2 ).extract()

    print "imgs2 len", len(imgs2)

    matches = Matcher( [PHash] ).match( imgs1, imgs2 )

    print len(matches)

    d = [m.type for m in matches if m.type == "DHash"]
    a = [m.type for m in matches if m.type == "AHash"]
    p = [m.type for m in matches if m.type == "PHash"]
    print "a", len(a)
    print "d", len(d)
    print "p", len(p)
