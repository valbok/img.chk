#!/usr/bin/env python
"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

"""
" Dumps serialized keypoints and descriptions to stdout or file
"""

import sys
import os
parentdir = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
os.sys.path.insert( 0, parentdir )

from core import *

if __name__ == '__main__':
    if len( sys.argv ) < 2:
        sys.exit(1)

    pathToImage = sys.argv[1]

    try:
        pathToDump = sys.argv[2]
    except:
        pathToDump = None

    img = Image.get( pathToImage )
    if pathToDump is None:
        print img.dump()
    else:
        img.dumpToFile( pathToDump )
