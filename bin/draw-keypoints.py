#!/usr/bin/env python
"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

"""
"""
import sys
sys.path.append( "../" )
from core import *
from matplotlib import pyplot as plt

if __name__ == '__main__':
    if len( sys.argv ) < 2:
        sys.exit( 1 )

    pathToImage = sys.argv[1]
    img = Image.get( pathToImage )
    kp = img._keypoints
    img2 = cv2.drawKeypoints( img._img, kp, None, (255, 0, 0), 4 )

    plt.imshow(img2),plt.show()
