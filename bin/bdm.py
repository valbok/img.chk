#!/usr/bin/env python
"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

"""
" Draws keypoints
"""
import sys
import os
parentdir = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
os.sys.path.insert( 0, parentdir )

from core import *
from matplotlib import pyplot as plt

if __name__ == '__main__':
    if len( sys.argv ) < 3:
        sys.exit( 1 )

    matcher = Matcher ( [PHash] )

    fn1 = sys.argv[1]
    img1 = Image.read( fn1 )
    m = ( img1.width * img1.height )
    kp1, desc1 = cv2.ORB(m).detectAndCompute( img1.img, None )
    e1 = Extractor( img1, kp1, desc1 )
    imgs1 = e1.binImages()
    imgs1.append( img1 )
    print "[" + str( len( imgs1 ) ) + "]", fn1

    fn2 = sys.argv[2]
    img2 = Image.read( fn2 )
    m = ( img2.width * img2.height )
    kp2, desc2 = cv2.ORB(m).detectAndCompute( img2.img, None )
    e2 = Extractor( img2, kp2, desc2 )
    imgs2 = e2.binImages()
    imgs2.append( img2 )
    print "[" + str( len( imgs2 ) ) + "]", fn2

    d = 7
    matches = matcher.match( imgs1, imgs2, d )

    print "found", len(matches), "matches"

    oimg1 = plt.imread( fn1 )
    oimg2 = plt.imread( fn2 )

    for kp in kp1:
        x = kp.pt[0]
        y = kp.pt[1]

        cv2.circle( oimg1, ( int( x ), int( y ) ), 1, (32,32,32), 1 )

    for kp in kp2:
        x = kp.pt[0]
        y = kp.pt[1]

        cv2.circle( oimg2, ( int( x ), int( y ) ), 1, (32,32,32), 1 )

    for m in matches:
        h1,h2 = m.hashes
        d1 = h1.dict()
        d2 = h2.dict()

        cv2.circle( oimg1, ( int( d1["x"] ), int( d1["y"] ) ), 2, (0,255,0), -1 )
        cv2.circle( oimg2, ( int( d2["x"] ), int( d2["y"] ) ), 2, (0,255,0), -1 )

    #cv2.imwrite( "fn_out1.jpg", oimg1.img )
    #cv2.imwrite( "fn_out2.jpg", oimg2.img )
    #plt.imshow( oimg.img),plt.show()

    # create BFMatcher object
    bf = cv2.BFMatcher( cv2.NORM_HAMMING, crossCheck=True )

    # Match descriptors.
    matches = bf.match(desc1,desc2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    mc = 0
    for i in xrange( len( matches ) ):
        m = matches[i]
        ts = m.trainIdx
        qs = m.queryIdx
        kp = kp1[qs]
        x = kp.pt[0]
        y = kp.pt[1]
        if m.distance > 7:
            break
        mc += 1

        cv2.circle( oimg1, ( int( x ), int( y ) ), 1, (255,0,0), 1 )

        kp = kp2[ts]
        x = kp.pt[0]
        y = kp.pt[1]

        cv2.circle( oimg2, ( int( x ), int( y ) ), 1, (255,0,0), 1 )

    print "found", mc, "orb bf matches"

    fig = plt.figure()
    a=fig.add_subplot(1,2,1)
    imgplot = plt.imshow(oimg1)

    a=fig.add_subplot(1,2,2)
    imgplot = plt.imshow(oimg2)

    plt.show()
