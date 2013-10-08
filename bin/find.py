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
import os
sys.path.append( "../" )
from core import *

if __name__ == '__main__':
    if len( sys.argv ) < 3:
        sys.exit(1)

    dump = sys.argv[1]
    img1 = Image.loadFromFile( dump )
    ddir = sys.argv[2]
    print "DIR: ",ddir
    ii = 0
    for r,d,files in os.walk( ddir ):
        l = len( files )
        for f in files:
            if f != "99.dump":
                continue

            ii = ii + 1
            print "[" + str( ii * 100 / l ) + "%] " + f

            p = str( ddir + '/' + f )
            print "p ", p
            img2 = Image.loadFromFile( p )

            if img1.looksLike( img2 ):
                print "         found: ", f
                sys.exit()
