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

    fn1 = sys.argv[1]
    img1 = Image.read( fn1 )
    surf = cv2.SURF( 400 )
    matcher = Matcher( [PHash] )
    kp1 = surf.detect( img1.img, None )
    k = 30
    a = 10
    m = 32
    d = 8

    imgs1 = ImageExtractor( img1, kp1 ).extract( (0,k), a, (32,32) )
    matcher = Matcher( [PHash] )

    print "imgs1 len", len( imgs1 )
    print len( matcher.hashes( imgs1 )[PHash] )

    fn2 = sys.argv[2]
    img2 = Image.read( fn2 )
    kp2 = surf.detect( img2.img, None )

    imgs2 = ImageExtractor( img2, kp2 ).extract( (0,k), a, (32,32) )
    print "imgs2 len", len(imgs2)
    print len(matcher.hashes( imgs2 )[PHash])

    matches = matcher.match( imgs1, imgs2, d )

    print len(matches)

    d = [m.type for m in matches if m.type == "DHash"]
    a = [m.type for m in matches if m.type == "AHash"]
    p = [m.type for m in matches if m.type == "PHash"]
    print "a", len(a)
    print "d", len(d)
    print "p", len(p)

    for k in xrange( len(matches) ):
        m = matches[k]
        i1 = m.hashes[0].img.img
        i2 = m.hashes[1].img.img
        path1 = '1/' + str(k) + "-" + m.type + '.jpg'
        path2 = '2/' + str(k) + "-" + m.type + '.jpg'
        cv2.imwrite(path1,i1)
        cv2.imwrite(path2,i2)
