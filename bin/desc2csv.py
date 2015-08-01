#!/usr/bin/env python
"""
" @author VaL
" @copyright Copyright (C) 2013 VaL Doroshchuk
" @license GNU GPL v2
"""

"""
" ???
"""
import sys
import os
import glob
import numpy
import math

parentdir = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
os.sys.path.insert( 0, parentdir )

from core import *

if __name__ == '__main__':
    if len( sys.argv ) < 2:
        sys.exit( 1 )

    fn = sys.argv[1]
    mm = False
    try:
        p = int(sys.argv[2])
    except Exception, e:
        pass

    try:
        mm = int(sys.argv[3])
    except Exception, e:
        pass
    
    def srt(item):
        return math.hypot(item['x'], item['y'])


    # Read dir and find files to compute
    fs = glob.glob(fn + "/*")
    for f in fs:
        img = Image.read(f)
        m = img.width * img.height;
        if mm != False:
            m = mm

        kp, desc = cv2.SURF(m).detectAndCompute(img.img, None)

        if desc is None:
            sys.stderr.write("No keypoints found for " + f +"\n")
            continue

        kps = []
        for i in xrange(len(kp)):
            item = {'x': kp[i].pt[0], 'y': kp[i].pt[1], 'desc': desc[i]}
            kps.append(item)

        kps.sort(key = srt)
        sz = len(kps)
        for i in xrange(sz):
            if sz - i < 3:
                break

            d = numpy.append(kps[i]['desc'], kps[i + 1]['desc'])
            d = numpy.append(d, kps[i + 2]['desc'])
            d = numpy.append(d, p) # add positive or negative case.
            print ",".join(map(str, d))


        #for d in desc:
        #    d = numpy.append(d, p)
        #    print ",".join(map(str, d))
