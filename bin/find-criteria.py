#!/usr/bin/env python
"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

"""
" tmp
"""
import sys
import os
parentdir = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
os.sys.path.insert( 0, parentdir )

import json
from core import *

if __name__ == '__main__':
    cv = cv2.SURF( 400 )
    matcher = Matcher( [PHash] )

    dir = "../tests/core/images/"
    samples = ["madonna-cropped-face2.jpg", "madonna-cropped-vertical.jpg","madonna-cropped-face.jpg","madonna-a1.jpg","madonna-a2-line.jpg","madonna-sq.jpg", "madonna.jpg"]
    targets = ["madonna-a.jpg"]

    simgs = []
    timgs = []
    for s in samples:
        img = Image.read( dir + s )
        kp = cv.detect( img.img, None )
        simgs.append( {"img": img, "kp": kp, "fn": s} )

    for s in targets:
        img = Image.read( dir + s )
        kp = cv.detect( img.img, None )
        timgs.append( {"img": img, "kp": kp, "fn": s} )

    mx = {}
    for s in simgs:
        img1 = s["img"]
        kp1 = s["kp"]
        fn1 = s["fn"]
        print fn1
        for t in timgs:
            img2 = t["img"]
            kp2 = t["kp"]
            fn2 = t["fn"]
            print "\t",fn1
            mx = 0
            mxi = {}

            for d in xrange( 0, 10 ):
                for k in xrange( 10, 40 ):
                    for a in xrange( 10, 105, 5 ):
                        for m in xrange( 1, 9 ):
                            imgs1 = ImageExtractor( img1, kp1 ).extract( (0, k), a, ((m,m),(m,m)) )
                            imgs2 = ImageExtractor( img2, kp2 ).extract( (0, k), a, ((m,m),(m,m)) )

                            matches = matcher.match( imgs1, imgs2, d )
                            if len( matches ) > mx:
                                mx = len( matches )
                                mxi = {"d":d, "k": k, "a": a, "m": m}


            print "\t\t",mxi
