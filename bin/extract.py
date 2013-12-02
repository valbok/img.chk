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
    imgs1 = ImageExtractor( img1, kp1 ).extract()
    result = {'AHash': {}, 'DHash': {}, 'PHash': {}}
    for ii in xrange( len(imgs1) ):
        i = imgs1[ii]
        a = AHash( i )
        d = DHash( i )
        p = PHash( i )
        result['AHash'][str( a )] = a.dict()
        result['DHash'][str( d )] = d.dict()
        result['PHash'][str( p )] = p.dict()

    print json.dumps( result )
