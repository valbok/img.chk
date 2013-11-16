"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import unittest
from unittest_data_provider import data_provider
from core import *

class ImageTest( unittest.TestCase ):

    def testWrongFN( self ):
        with self.assertRaises( Exception ):
            Image.read( "wrong/path.jpg" )

    def testCorretFN( self ):
        img = Image.get( "tests/core/images/1.jpg" )
        self.assertEquals( True, isinstance( img, Image ) )

    def testDump( self ):
        img = Image.get( "tests/core/images/1.jpg" )
        lines = img.dump()
        img = img.load( lines )
        img.dumpToFile( "tests/core/dumps/1.dump.tmp" )
        f = open( "tests/core/dumps/1.dump.tmp" )
        lines = f.readlines()
        f.close()

        f = open( "tests/core/dumps/1.dump" )
        lines2 = f.readlines()
        f.close()
        self.assertEquals( lines, lines2 )

    def testDumpIdentity( self ):
        img1 = Image.get( "tests/core/images/1.jpg" )
        lines = img1.dump()
        img2 = img1.load( lines )
        for i in xrange( len( img1._keypoints ) ):
            k1 = img1._keypoints[i]
            k2 = img2._keypoints[i]
            self.assertEquals( k1.pt, k2.pt )
            self.assertEquals( k1.size, k2.size )
            self.assertEquals( k1.angle, k2.angle )
            self.assertEquals( k1.response, k2.response )
            self.assertEquals( k1.octave, k2.octave )
            self.assertEquals( k1.class_id, k2.class_id )
            desc1 = img1._descriptors[i]
            desc2 = img2._descriptors[i]
            self.assertEquals( len( desc1 ), len( desc2 ) )
            for d in xrange( len( desc1 ) ):
                self.assertEquals( desc1[d], desc2[d] )

    imgMatches = lambda: \
                (
                    ( "1_500.jpg", "1_500_bl.jpg", True ),
                    ( "1_500.jpg", "1_500_bl2.jpg", True ),
                    ( "1_500.jpg", "1_500_brb.jpg", True ),
                    ( "1_500.jpg", "1_500_c1.jpg", True ),
                    ( "1_500.jpg", "1_500_cr.jpg", True ),
                    ( "1_500.jpg", "1_500_f.jpg", True ),
                    ( "1_500.jpg", "1_500_left.jpg", True ),
                    ( "1_500.jpg", "1_500_wb.jpg", True ),
                    ( "1_500.jpg", "1_500_wl.jpg", True ),
                    ( "1_500.jpg", "1_500_sh-100.jpg", True ),
                    ( "1_500.jpg", "1_500_l+100.jpg", True ),
                    #( "1_500.jpg", "1_500_inv.jpg", True ),
                    ( "1_500.jpg", "1_500_brightness.jpg", True ),
                    ( "1_500.jpg", "1_500_brightness-100.jpg", True ),
                    ( "1_500.jpg", "1_500_contrast.jpg", True ),

                    ( "1.jpg", "1.jpg", True ),
                    ( "1.jpg", "1_500.jpg", True ),
                    ( "1.jpg", "1_150.jpg", True ),
                    ( "1.jpg", "2.jpg", False ),
                    ( "1.jpg", "2_500.jpg", False ),
                    ( "1.jpg", "3.jpg", False ),
                    ( "1.jpg", "3_500.jpg", False ),
                    ( "1.jpg", "4.jpg", False ),
                    ( "1.jpg", "4_500.jpg", False ),
                    ( "1.jpg", "5.jpg", False ),
                    ( "1.jpg", "5_500.jpg", False ),
                    ( "1.jpg", "6.jpg", False ),
                    ( "1.jpg", "6_500.jpg", False ),
                    ( "1.jpg", "7.jpg", False ),
                    ( "1.jpg", "7_500.jpg", False ),

                    ( "2.jpg", "1.jpg", False ),
                    ( "2.jpg", "1_500.jpg", False ),
                    ( "2.jpg", "2.jpg", True ),
                    ( "2.jpg", "2_500.jpg", True ),
                    ( "2.jpg", "3.jpg", False ),
                    ( "2.jpg", "3_500.jpg", False ),
                    ( "2.jpg", "4.jpg", False ),
                    ( "2.jpg", "4_500.jpg", False ),
                    ( "2.jpg", "5.jpg", False ),
                    ( "2.jpg", "5_500.jpg", False ),
                    ( "2.jpg", "6.jpg", False ),
                    ( "2.jpg", "6_500.jpg", False ),
                    ( "2.jpg", "7.jpg", False ),
                    ( "2.jpg", "7_500.jpg", False ),

                    ( "3.jpg", "1.jpg", False ),
                    ( "3.jpg", "1_500.jpg", False ),
                    ( "3.jpg", "2.jpg", False ),
                    ( "3.jpg", "2_500.jpg", False ),
                    ( "3.jpg", "3.jpg", True ),
                    ( "3.jpg", "3_500.jpg", True ),
                    ( "3.jpg", "4.jpg", False ),
                    ( "3.jpg", "4_500.jpg", False ),
                    ( "3.jpg", "5.jpg", False ),
                    ( "3.jpg", "5_500.jpg", False ),
                    ( "3.jpg", "6.jpg", False ),
                    ( "3.jpg", "6_500.jpg", False ),
                    ( "3.jpg", "7.jpg", False ),
                    ( "3.jpg", "7_500.jpg", False ),

                    ( "4.jpg", "1.jpg", False ),
                    ( "4.jpg", "1_500.jpg", False ),
                    ( "4.jpg", "2.jpg", False ),
                    ( "4.jpg", "2_500.jpg", False ),
                    ( "4.jpg", "3.jpg", False ),
                    ( "4.jpg", "3_500.jpg", False ),
                    ( "4.jpg", "4.jpg", True ),
                    ( "4.jpg", "4_500.jpg", True ),
                    ( "4.jpg", "5.jpg", False ),
                    ( "4.jpg", "5_500.jpg", False ),
                    ( "4.jpg", "6.jpg", False ),
                    ( "4.jpg", "6_500.jpg", False ),
                    ( "4.jpg", "7.jpg", False ),
                    ( "4.jpg", "7_500.jpg", False ),

                    ( "5.jpg", "1.jpg", False ),
                    ( "5.jpg", "1_500.jpg", False ),
                    ( "5.jpg", "2.jpg", False ),
                    ( "5.jpg", "2_500.jpg", False ),
                    ( "5.jpg", "3.jpg", False ),
                    ( "5.jpg", "3_500.jpg", False ),
                    ( "5.jpg", "4.jpg", False ),
                    ( "5.jpg", "4_500.jpg", False ),
                    ( "5.jpg", "5.jpg", True ),
                    ( "5.jpg", "5_500.jpg", True ),
                    ( "5.jpg", "6.jpg", False ),
                    ( "5.jpg", "6_500.jpg", False ),
                    ( "5.jpg", "7.jpg", False ),
                    ( "5.jpg", "7_500.jpg", False ),

                    ( "6.jpg", "1.jpg", False ),
                    ( "6.jpg", "1_500.jpg", False ),
                    ( "6.jpg", "2.jpg", False ),
                    ( "6.jpg", "2_500.jpg", False ),
                    ( "6.jpg", "3.jpg", False ),
                    ( "6.jpg", "3_500.jpg", False ),
                    ( "6.jpg", "4.jpg", False ),
                    ( "6.jpg", "4_500.jpg", False ),
                    ( "6.jpg", "5.jpg", False ),
                    ( "6.jpg", "5_500.jpg", False ),
                    ( "6.jpg", "6.jpg", True ),
                    ( "6.jpg", "6_500.jpg", True ),
                    ( "6.jpg", "7.jpg", False ),
                    ( "6.jpg", "7_500.jpg", False ),

                    ( "7.jpg", "1.jpg", False ),
                    ( "7.jpg", "1_500.jpg", False ),
                    ( "7.jpg", "2.jpg", False ),
                    ( "7.jpg", "2_500.jpg", False ),
                    ( "7.jpg", "3.jpg", False ),
                    ( "7.jpg", "3_500.jpg", False ),
                    ( "7.jpg", "4.jpg", False ),
                    ( "7.jpg", "4_500.jpg", False ),
                    ( "7.jpg", "5.jpg", False ),
                    ( "7.jpg", "5_500.jpg", False ),
                    ( "7.jpg", "6.jpg", False ),
                    ( "7.jpg", "6_500.jpg", False ),
                    ( "7.jpg", "7.jpg", True ),
                    ( "7.jpg", "7_500.jpg", True ),

                )

    @data_provider( imgMatches )
    def testLooksLike( self, f1, f2, e ):
        img1 = Image.get( "tests/core/images/" + f1 )
        img2 = Image.get( "tests/core/images/" + f2 )
        ps = img1.knnMatched( img2 )

        self.assertEquals( e, ps )

    imgdDiff = lambda: \
                (
                    ( "1_500.jpg", "1_500_bl.jpg", True ),
                    ( "1_500.jpg", "1_500_bl2.jpg", True ),
                    #( "1_500.jpg", "1_500_c1.jpg", True ),
                    ( "1_500.jpg", "1_500_cr.jpg", True ),
                    ( "1_500.jpg", "1_500_f.jpg", True ),
                    ( "1_500.jpg", "1_500_left.jpg", True ),
                    #( "1_500.jpg", "1_500_wb.jpg", True ),
                    #( "1_500.jpg", "1_500_wl.jpg", True ),
                    ( "1_500.jpg", "1_500_sh-100.jpg", True ),
                    ( "1_500.jpg", "1_500_l+100.jpg", True ),
                    #( "1_500.jpg", "1_500_inv.jpg", True ),
                    ( "1_500.jpg", "1_500_brightness.jpg", True ),
                    ( "1_500.jpg", "1_500_brightness-100.jpg", True ),
                    #( "1_500.jpg", "1_500_contrast.jpg", True ),

                    ( "1.jpg", "1.jpg", True ),
                    ( "1.jpg", "1_500.jpg", True ),
                    ( "1.jpg", "1_150.jpg", True ),
                    ( "1.jpg", "2.jpg", False ),
                    ( "1.jpg", "2_500.jpg", False ),
                    ( "1.jpg", "3.jpg", False ),
                    ( "1.jpg", "3_500.jpg", False ),
                    ( "1.jpg", "4.jpg", False ),
                    ( "1.jpg", "4_500.jpg", False ),
                    ( "1.jpg", "5.jpg", False ),
                    ( "1.jpg", "5_500.jpg", False ),
                    ( "1.jpg", "6.jpg", False ),
                    ( "1.jpg", "6_500.jpg", False ),
                    ( "1.jpg", "7.jpg", False ),
                    ( "1.jpg", "7_500.jpg", False ),

                    ( "2.jpg", "1.jpg", False ),
                    ( "2.jpg", "1_500.jpg", False ),
                    ( "2.jpg", "2.jpg", True ),
                    ( "2.jpg", "2_500.jpg", True ),
                    ( "2.jpg", "3.jpg", False ),
                    ( "2.jpg", "3_500.jpg", False ),
                    ( "2.jpg", "4.jpg", False ),
                    ( "2.jpg", "4_500.jpg", False ),
                    ( "2.jpg", "5.jpg", False ),
                    ( "2.jpg", "5_500.jpg", False ),
                    ( "2.jpg", "6.jpg", False ),
                    ( "2.jpg", "6_500.jpg", False ),
                    ( "2.jpg", "7.jpg", False ),
                    ( "2.jpg", "7_500.jpg", False ),

                    ( "3.jpg", "1.jpg", False ),
                    ( "3.jpg", "1_500.jpg", False ),
                    ( "3.jpg", "2.jpg", False ),
                    ( "3.jpg", "2_500.jpg", False ),
                    ( "3.jpg", "3.jpg", True ),
                    ( "3.jpg", "3_500.jpg", True ),
                    ( "3.jpg", "4.jpg", False ),
                    ( "3.jpg", "4_500.jpg", False ),
                    ( "3.jpg", "5.jpg", False ),
                    ( "3.jpg", "5_500.jpg", False ),
                    ( "3.jpg", "6.jpg", False ),
                    ( "3.jpg", "6_500.jpg", False ),
                    ( "3.jpg", "7.jpg", False ),
                    ( "3.jpg", "7_500.jpg", False ),

                    ( "4.jpg", "1.jpg", False ),
                    ( "4.jpg", "1_500.jpg", False ),
                    ( "4.jpg", "2.jpg", False ),
                    ( "4.jpg", "2_500.jpg", False ),
                    ( "4.jpg", "3.jpg", False ),
                    ( "4.jpg", "3_500.jpg", False ),
                    ( "4.jpg", "4.jpg", True ),
                    ( "4.jpg", "4_500.jpg", True ),
                    ( "4.jpg", "5.jpg", False ),
                    ( "4.jpg", "5_500.jpg", False ),
                    ( "4.jpg", "6.jpg", False ),
                    ( "4.jpg", "6_500.jpg", False ),
                    ( "4.jpg", "7.jpg", False ),
                    ( "4.jpg", "7_500.jpg", False ),

                    ( "5.jpg", "1.jpg", False ),
                    ( "5.jpg", "1_500.jpg", False ),
                    ( "5.jpg", "2.jpg", False ),
                    ( "5.jpg", "2_500.jpg", False ),
                    ( "5.jpg", "3.jpg", False ),
                    ( "5.jpg", "3_500.jpg", False ),
                    ( "5.jpg", "4.jpg", False ),
                    ( "5.jpg", "4_500.jpg", False ),
                    ( "5.jpg", "5.jpg", True ),
                    ( "5.jpg", "5_500.jpg", True ),
                    ( "5.jpg", "6.jpg", False ),
                    ( "5.jpg", "6_500.jpg", False ),
                    ( "5.jpg", "7.jpg", False ),
                    ( "5.jpg", "7_500.jpg", False ),

                    ( "6.jpg", "1.jpg", False ),
                    ( "6.jpg", "1_500.jpg", False ),
                    ( "6.jpg", "2.jpg", False ),
                    ( "6.jpg", "2_500.jpg", False ),
                    ( "6.jpg", "3.jpg", False ),
                    ( "6.jpg", "3_500.jpg", False ),
                    ( "6.jpg", "4.jpg", False ),
                    ( "6.jpg", "4_500.jpg", False ),
                    ( "6.jpg", "5.jpg", False ),
                    ( "6.jpg", "5_500.jpg", False ),
                    ( "6.jpg", "6.jpg", True ),
                    ( "6.jpg", "6_500.jpg", True ),
                    ( "6.jpg", "7.jpg", False ),
                    ( "6.jpg", "7_500.jpg", False ),

                    ( "7.jpg", "1.jpg", False ),
                    ( "7.jpg", "1_500.jpg", False ),
                    ( "7.jpg", "2.jpg", False ),
                    ( "7.jpg", "2_500.jpg", False ),
                    ( "7.jpg", "3.jpg", False ),
                    ( "7.jpg", "3_500.jpg", False ),
                    ( "7.jpg", "4.jpg", False ),
                    ( "7.jpg", "4_500.jpg", False ),
                    ( "7.jpg", "5.jpg", False ),
                    ( "7.jpg", "5_500.jpg", False ),
                    ( "7.jpg", "6.jpg", False ),
                    ( "7.jpg", "6_500.jpg", False ),
                    ( "7.jpg", "7.jpg", True ),
                    ( "7.jpg", "7_500.jpg", True ),

                    ( "madonna.jpg", "madonna-a.jpg", True ),
                    ( "madonna-a.jpg", "madonna-a1.jpg", True ),
                    ( "madonna-a.jpg", "madonna-a2-line.jpg", True ),
                    ( "madonna-a.jpg", "madonna-sq.jpg", True ),

                )

    imgpDiff = lambda: \
                (
                    ( "1_500.jpg", "1_500_bl.jpg", True ),
                    ( "1_500.jpg", "1_500_bl2.jpg", True ),
                    #( "1_500.jpg", "1_500_c1.jpg", True ),
                    ( "1_500.jpg", "1_500_cr.jpg", True ),
                    ( "1_500.jpg", "1_500_f.jpg", True ),
                    ( "1_500.jpg", "1_500_left.jpg", True ),
                    #( "1_500.jpg", "1_500_wb.jpg", True ),
                    #( "1_500.jpg", "1_500_wl.jpg", True ),
                    ( "1_500.jpg", "1_500_sh-100.jpg", True ),
                    ( "1_500.jpg", "1_500_l+100.jpg", True ),
                    #( "1_500.jpg", "1_500_inv.jpg", True ),
                    ( "1_500.jpg", "1_500_brightness.jpg", True ),
                    ( "1_500.jpg", "1_500_brightness-100.jpg", True ),
                    ( "1_500.jpg", "1_500_contrast.jpg", True ),

                    ( "1.jpg", "1.jpg", True ),
                    ( "1.jpg", "1_500.jpg", True ),
                    ( "1.jpg", "1_150.jpg", True ),
                    ( "1.jpg", "2.jpg", False ),
                    ( "1.jpg", "2_500.jpg", False ),
                    ( "1.jpg", "3.jpg", False ),
                    ( "1.jpg", "3_500.jpg", False ),
                    ( "1.jpg", "4.jpg", False ),
                    ( "1.jpg", "4_500.jpg", False ),
                    ( "1.jpg", "5.jpg", False ),
                    ( "1.jpg", "5_500.jpg", False ),
                    ( "1.jpg", "6.jpg", False ),
                    ( "1.jpg", "6_500.jpg", False ),
                    ( "1.jpg", "7.jpg", False ),
                    ( "1.jpg", "7_500.jpg", False ),

                    ( "2.jpg", "1.jpg", False ),
                    ( "2.jpg", "1_500.jpg", False ),
                    ( "2.jpg", "2.jpg", True ),
                    ( "2.jpg", "2_500.jpg", True ),
                    ( "2.jpg", "3.jpg", False ),
                    ( "2.jpg", "3_500.jpg", False ),
                    ( "2.jpg", "4.jpg", False ),
                    ( "2.jpg", "4_500.jpg", False ),
                    ( "2.jpg", "5.jpg", False ),
                    ( "2.jpg", "5_500.jpg", False ),
                    ( "2.jpg", "6.jpg", False ),
                    ( "2.jpg", "6_500.jpg", False ),
                    ( "2.jpg", "7.jpg", False ),
                    ( "2.jpg", "7_500.jpg", False ),

                    ( "3.jpg", "1.jpg", False ),
                    ( "3.jpg", "1_500.jpg", False ),
                    ( "3.jpg", "2.jpg", False ),
                    ( "3.jpg", "2_500.jpg", False ),
                    ( "3.jpg", "3.jpg", True ),
                    ( "3.jpg", "3_500.jpg", True ),
                    ( "3.jpg", "4.jpg", False ),
                    ( "3.jpg", "4_500.jpg", False ),
                    ( "3.jpg", "5.jpg", False ),
                    ( "3.jpg", "5_500.jpg", False ),
                    ( "3.jpg", "6.jpg", False ),
                    ( "3.jpg", "6_500.jpg", False ),
                    ( "3.jpg", "7.jpg", False ),
                    ( "3.jpg", "7_500.jpg", False ),

                    ( "4.jpg", "1.jpg", False ),
                    ( "4.jpg", "1_500.jpg", False ),
                    ( "4.jpg", "2.jpg", False ),
                    ( "4.jpg", "2_500.jpg", False ),
                    ( "4.jpg", "3.jpg", False ),
                    ( "4.jpg", "3_500.jpg", False ),
                    ( "4.jpg", "4.jpg", True ),
                    ( "4.jpg", "4_500.jpg", True ),
                    ( "4.jpg", "5.jpg", False ),
                    ( "4.jpg", "5_500.jpg", False ),
                    ( "4.jpg", "6.jpg", False ),
                    ( "4.jpg", "6_500.jpg", False ),
                    ( "4.jpg", "7.jpg", False ),
                    ( "4.jpg", "7_500.jpg", False ),

                    ( "5.jpg", "1.jpg", False ),
                    ( "5.jpg", "1_500.jpg", False ),
                    ( "5.jpg", "2.jpg", False ),
                    ( "5.jpg", "2_500.jpg", False ),
                    ( "5.jpg", "3.jpg", False ),
                    ( "5.jpg", "3_500.jpg", False ),
                    ( "5.jpg", "4.jpg", False ),
                    ( "5.jpg", "4_500.jpg", False ),
                    ( "5.jpg", "5.jpg", True ),
                    ( "5.jpg", "5_500.jpg", True ),
                    ( "5.jpg", "6.jpg", False ),
                    ( "5.jpg", "6_500.jpg", False ),
                    ( "5.jpg", "7.jpg", False ),
                    ( "5.jpg", "7_500.jpg", False ),

                    ( "6.jpg", "1.jpg", False ),
                    ( "6.jpg", "1_500.jpg", False ),
                    ( "6.jpg", "2.jpg", False ),
                    ( "6.jpg", "2_500.jpg", False ),
                    ( "6.jpg", "3.jpg", False ),
                    ( "6.jpg", "3_500.jpg", False ),
                    ( "6.jpg", "4.jpg", False ),
                    ( "6.jpg", "4_500.jpg", False ),
                    ( "6.jpg", "5.jpg", False ),
                    ( "6.jpg", "5_500.jpg", False ),
                    ( "6.jpg", "6.jpg", True ),
                    ( "6.jpg", "6_500.jpg", True ),
                    ( "6.jpg", "7.jpg", False ),
                    ( "6.jpg", "7_500.jpg", False ),

                    ( "7.jpg", "1.jpg", False ),
                    ( "7.jpg", "1_500.jpg", False ),
                    ( "7.jpg", "2.jpg", False ),
                    ( "7.jpg", "2_500.jpg", False ),
                    ( "7.jpg", "3.jpg", False ),
                    ( "7.jpg", "3_500.jpg", False ),
                    ( "7.jpg", "4.jpg", False ),
                    ( "7.jpg", "4_500.jpg", False ),
                    ( "7.jpg", "5.jpg", False ),
                    ( "7.jpg", "5_500.jpg", False ),
                    ( "7.jpg", "6.jpg", False ),
                    ( "7.jpg", "6_500.jpg", False ),
                    ( "7.jpg", "7.jpg", True ),
                    ( "7.jpg", "7_500.jpg", True ),

                    ( "madonna.jpg", "madonna-a.jpg", True ),
                    ( "madonna-a.jpg", "madonna-a1.jpg", True ),
                    ( "madonna-a.jpg", "madonna-a2-line.jpg", True ),
                    #( "madonna-a.jpg", "madonna-sq.jpg", True ),

                )

    @data_provider( imgdDiff )
    def testDifferenceHash( self, f1, f2, e ):
        img1 = Image.get( "tests/core/images/" + f1 )
        img2 = Image.get( "tests/core/images/" + f2 )
        h1 = img1.dhash()
        h2 = img2.dhash()
        b = Image.hammingDistance( h1, h2 )

        self.assertEquals( e, b <= 11 )


    @data_provider( imgpDiff )
    def testPerceptualHash( self, f1, f2, e ):
        img1 = Image.get( "tests/core/images/" + f1 )
        img2 = Image.get( "tests/core/images/" + f2 )
        h1 = img1.phash()
        h2 = img2.phash()
        b = Image.hammingDistance( h1, h2 )

        self.assertEquals( e, b <= 11 )


if __name__ == '__main__':
    unittest.main()
