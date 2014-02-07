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
    m = ( img1.width * img1.height ) / 1000
    kp1, desc1 = cv2.ORB(m).detectAndCompute( img1.img, None )
    e1 = Extractor( img1, kp1, desc1 )
    imgs1 = e1.binImages()
    imgs1.append( img1 )
    print "[" + str( len( imgs1 ) ) + "]", fn1

    fn2 = sys.argv[2]
    img2 = Image.read( fn2 )
    m = ( img2.width * img2.height ) / 1000
    kp2, desc2 = cv2.ORB(m).detectAndCompute( img2.img, None )
    e1 = Extractor( img2, kp2, desc2 )
    imgs2 = e1.binImages()
    imgs2.append( img2 )
    print "[" + str( len( imgs2 ) ) + "]", fn2

    oimg1 = plt.imread( fn1 )
    oimg2 = plt.imread( fn2 )

    for kp in kp1:
        x = kp.pt[0]
        y = kp.pt[1]

        cv2.circle( oimg1, ( int( x ), int( y ) ), 1, (255,0,0), 1 )

    for kp in kp2:
        x = kp.pt[0]
        y = kp.pt[1]

        cv2.circle( oimg2, ( int( x ), int( y ) ), 1, (255,0,0), 1 )

    fig = plt.figure()
    a=fig.add_subplot(1,2,1)
    imgplot = plt.imshow(oimg1)

    a=fig.add_subplot(1,2,2)
    imgplot = plt.imshow(oimg2)
    plt.show()
