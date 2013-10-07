"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import unittest
from core import *

class ImageTest( unittest.TestCase ):

    def testWrongFN( self ):
        with self.assertRaises( Exception ):
            Image.get( "wrong/path.jpg" )

    def testCorretFN( self ):
        img = Image.get( "tests/core/images/1.jpg" )
        self.assertEquals( True, isinstance( img, Image ) )

    def tes1tDumpToFile( self ):
        img = Image.get( "tests/core/images/1.jpg" )
        img.dumpToFile( "tests/core/dumps/1.dump" )

        f = open( "tests/core/dumps/1.dump.exp" )
        lines = f.readlines()
        f.close()
        f = open( "tests/core/dumps/1.dump" )
        lines2 = f.readlines()
        f.close()
        self.assertEquals( lines, lines2 )

    def testDump( self ):
        img = Image.get( "tests/core/images/1.jpg" )
        lines = img.dump()
        img = Image.load( lines )
        img.dumpToFile( "tests/core/dumps/1.dump.tmp" )
        f = open( "tests/core/dumps/1.dump.tmp" )
        lines = f.readlines()
        f.close()

        f = open( "tests/core/dumps/1.dump" )
        lines2 = f.readlines()
        f.close()
        self.assertEquals( lines, lines2 )

    def testLoadFromFile( self ):
        img = Image.loadFromFile( "tests/core/dumps/1.dump" )
        f = open( "tests/core/dumps/1.dump.exp" )
        lines = f.readlines()
        f.close()
        img.dumpToFile( "tests/core/dumps/1.dump" )
        f = open( "tests/core/dumps/1.dump" )
        lines2 = f.readlines()
        f.close()
        self.assertEquals( lines, lines2 )

    def testCompareToSelf( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/1.jpg" )
        ps = img1.compareInPercent( img2 )

        self.assertEquals( 100, ps )

    def testCompareTo( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/1_500.jpg" )
        ps = img1.compareInPercent( img2 )

        self.assertEquals( True, ps  > 70 )

    def testCompareToR( self ):
        img1 = Image.get( "tests/core/images/1_500.jpg" )
        img2 = Image.get( "tests/core/images/1.jpg" )
        ps = img1.compareInPercent( img2 )

        self.assertEquals( True, ps  > 50 )

    def testCompareTo2( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/2.jpg" )
        ps = img1.compareInPercent( img2 )

        self.assertEquals( True,  ps < 10 )

    def testLooksLike( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/2.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( False, ps )

    def testLooksLikeTrue( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/1.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )

    def testLooksLikeTrue2( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/1_500.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )

    def testLooksLikeTrue3( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/1_150.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )

    def testLooksLikeTrue4( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/1_150_2.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )

    def testLooksLikeTrue500( self ):
        img1 = Image.get( "tests/core/images/1_500.jpg" )
        img2 = Image.get( "tests/core/images/1_150.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )

    def testLooksLikeTrueR( self ):
        img1 = Image.get( "tests/core/images/1_500.jpg" )
        img2 = Image.get( "tests/core/images/1.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )

    def testLooksLikeTrueR1( self ):
        img1 = Image.get( "tests/core/images/1_150.jpg" )
        img2 = Image.get( "tests/core/images/1.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )

    def testLooksLikeTrueR2( self ):
        img1 = Image.get( "tests/core/images/1_150_2.jpg" )
        img2 = Image.get( "tests/core/images/1.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )

if __name__ == '__main__':
    unittest.main()
