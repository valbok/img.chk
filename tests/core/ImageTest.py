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

    def testDumpToFile( self ):
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

    def testLooksLike( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/2.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( False, ps )

    def testLooksLikeFalse( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/2_150.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( False, ps )

    def testLooksLikeFalse1150( self ):
        img1 = Image.get( "tests/core/images/1_150.jpg" )
        img2 = Image.get( "tests/core/images/2.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( False, ps )

    def testLooksLikeFalse11502( self ):
        img1 = Image.get( "tests/core/images/1_150_2.jpg" )
        img2 = Image.get( "tests/core/images/2.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( False, ps )

    def testLooksLikeFalse1115022150( self ):
        img1 = Image.get( "tests/core/images/1_150_2.jpg" )
        img2 = Image.get( "tests/core/images/2_150.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( False, ps )

    def testLooksLikeFalse1115022150( self ):
        img1 = Image.get( "tests/core/images/1_150_2.jpg" )
        img2 = Image.get( "tests/core/images/2.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( False, ps )

    def testLooksLikeFalse13( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/3.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( False, ps )

    def testLooksLikeFalse14( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/4.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( False, ps )

    def testLooksLikeFalse34( self ):
        img1 = Image.get( "tests/core/images/3.jpg" )
        img2 = Image.get( "tests/core/images/4.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( False, ps )

    def testLooksLikeTrue4500( self ):
        img1 = Image.get( "tests/core/images/4.jpg" )
        img2 = Image.get( "tests/core/images/4_500.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )

    def testLoadFromFileSelf( self ):
        img1 = Image.loadFromFile( "tests/core/dumps/1.dump" )
        img2 = Image.loadFromFile( "tests/core/dumps/1.dump" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )


    def testLooksLikeTrueRDumpLoad( self ):
        img1 = Image.loadFromFile( "tests/core/dumps/1.dump" )
        img2 = Image.get( "tests/core/images/1.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )

    def testLooksLikeTrueRDump( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        img2 = Image.get( "tests/core/images/1_150.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )
        img1.dumpToFile( "tests/core/dumps/tmp/1.dump" )
        img2.dumpToFile( "tests/core/dumps/tmp/1_150.dump" )

        img11 = Image.loadFromFile( "tests/core/dumps/tmp/1.dump" )
        img22 = Image.loadFromFile( "tests/core/dumps/tmp/1_150.dump" )
        ps = img11.looksLike( img22 )

        self.assertEquals( True, ps )

    def testLooksLikeTrueRDumpLoad150( self ):
        img1 = Image.loadFromFile( "tests/core/dumps/1_150.dump" )
        img2 = Image.get( "tests/core/images/1_150.jpg" )
        ps = img1.looksLike( img2 )

        self.assertEquals( True, ps )


if __name__ == '__main__':
    unittest.main()
