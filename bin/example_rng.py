#!/usr/bin/env python
"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

"""
" Example usage
"""
import sys
import os
parentdir = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
os.sys.path.insert( 0, parentdir )

from core import *

if __name__ == '__main__':
    cv = cv2.SURF( 400 )

    # Face with closed eyes and text
    img1 = Image.read( "../tests/core/images/madonna-bad-girl.jpg" )
    # Painted the same face without text
    img2 = Image.read( "../tests/core/images/madonna-pop-art.jpg" )

    kp1 = cv.detect( img1.img, None )
    kp2 = cv.detect( img2.img, None )

    # NOTE: Due to RNG extracted images are different per each iteration
    matches = []
    i = 0
    while len( matches ) == 0:
        imgs1 = ImageExtractor( img1, kp1 ).extract()
        imgs2 = ImageExtractor( img2, kp2 ).extract()
        matches = Matcher( [PHash] ).match( imgs1, imgs2 )
        i += 1

    print "Found", len( matches ), "matches on", i, "iteration"
