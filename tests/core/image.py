"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import unittest
from unittest_data_provider import data_provider
from core import *
import numpy as np

class ImageTest( unittest.TestCase ):

    def testWrongFN( self ):
        with self.assertRaises( Exception ):
            Image.read( "wrong/path.jpg" )

    def testCorretFN( self ):
        img = Image.read( "tests/core/images/1.jpg" )
        self.assertEquals( True, isinstance( img, Image ) )

    def testResize( self ):
        img = Image.read( "tests/core/images/5.jpg" )
        img2 = img.resize( (32, 32) )
        self.assertEquals( 32, img2.width )
        self.assertEquals( 32, img2.height )

    def testShape( self ):
        img = Image.read( "tests/core/images/5.jpg" )
        s = img.shape
        self.assertEquals( 399, s[0] )
        self.assertEquals( 500, s[1] )

    def testWidth( self ):
        img = Image.read( "tests/core/images/5.jpg" )
        s = img.width
        self.assertEquals( 500, s )

    def testHeight( self ):
        img = Image.read( "tests/core/images/5.jpg" )
        s = img.height
        self.assertEquals( 399, s )

    def testPixel( self ):
        img = Image.read( "tests/core/images/1.jpg", 0 )
        self.assertEquals( 4, img.pixel( 0, 0 ) )

    def testCrop( self ):
        img = Image.read( "tests/core/images/3.jpg", 0 )
        img2 = img.crop( 0, 0, 20, 10 )
        self.assertEquals( 20, img2.width )
        self.assertEquals( 10, img2.height )

if __name__ == '__main__':
    unittest.main()
