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
    if len( sys.argv ) < 2:
        sys.exit( 1 )

    pathToImage = sys.argv[1]
    img = Image.get( pathToImage )
    kp = img._keypoints
    img2 = cv2.drawKeypoints( img._cv2_img, kp, None, (255, 0, 0), 4 )

    plt.imshow(img2),plt.show()
