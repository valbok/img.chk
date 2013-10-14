#!/usr/bin/env python
"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

"""
"
"""
import sys
sys.path.append( "../" )
from core import *

if __name__ == '__main__':
    if len( sys.argv ) < 3:
        sys.exit(1)

    d1 = sys.argv[1]
    d2 = sys.argv[2]

    img1 = Image.loadFromFile( d1 )
    img2 = Image.loadFromFile( d2 )

    if img1.looksLike( img2 ):
        print "looks like"
        sys.exit( 1 )

