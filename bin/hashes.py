#!/usr/bin/env python
"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

"""
" Extractes hashes from an image
"""
import sys
import os
parentdir = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
os.sys.path.insert( 0, parentdir )

import json
from core import *

if __name__ == '__main__':
    if len( sys.argv ) < 2:
        sys.exit( 1 )

    fn1 = sys.argv[1]
    img1 = Image.read( fn1 )
    cv = cv2.SURF( 400 )
    kp1 = cv.detect( img1.img, None )
    e = Extractor( img1, kp1 )
    a = 10
    k = 30
    imgs1 = []
    for m in [8]:
        imgs = e.subImages( (0,k), a, m )
        imgs1 += imgs

    matcher = Matcher( [PHash] )
    result = {'PHash': {}}
    phs = {}
    hashes = matcher.hashes( imgs1 )[PHash]
    for h in hashes:
        phs[str( h )] = h.dict()

    result['PHash'] = phs
    print json.dumps( result )
