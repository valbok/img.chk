"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import unittest
from unittest_data_provider import data_provider
from core import *
import cv2

class ExtractorTest( unittest.TestCase ):

    def testExtract( self ):
        img = Image.read( "tests/core/images/madonna-a.jpg" )
        kp = cv2.SURF( 5000 ).detect( img.img, None )
        imgs = ImageExtractor( img, kp ).extract( (1,2) )

        self.assertEquals( 1, len( imgs ) )
        self.assertEquals( True, isinstance( imgs[0], Image ) )


if __name__ == '__main__':
    unittest.main()
