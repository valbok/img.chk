#!/usr/bin/env python
"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

"""
" Calculates perceptual hashes
"""

import sys
import os
parentdir = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
os.sys.path.insert( 0, parentdir )

from core import *

if __name__ == '__main__':
    if len( sys.argv ) < 2:
        sys.exit(1)

    fn1 = sys.argv[1]

    try:
        fn2 = sys.argv[2]
    except:
        fn2 = None

    img1 = Image.read( fn1 )
    hash1 = abs( img1.phash() )
    print '%(hash)016x' %{"hash": hash1}
    if fn2 is not None:
        img2 = Image.read( fn2 )
        hash2 = abs( img2.phash() )
        print '%(hash)016x' %{"hash": hash2}
        print str( Image.hammingDistance( hash1, hash2 )) + " and " + str( ( ( 64 - Image.hammingDistance( hash1, hash2 ) )  * 100.0 ) / 64.0 ) + "% similar."
