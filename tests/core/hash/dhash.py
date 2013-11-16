"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

import unittest
from unittest_data_provider import data_provider
from core import *

class DHashTest( unittest.TestCase ):

    def testValue( self ):
        img = Image.read( "tests/core/images/1_500.jpg" )
        h = DHash( img )
        v = h.value
        s = str( h )
        self.assertEquals( True, isinstance( h, DHash ) )
        self.assertEquals( True, isinstance( v, int ) )
        self.assertEquals( True, abs( v ) > 0 )
        self.assertEquals( True, isinstance( s, str ) )

    imgdDiff = lambda: \
                (
                    ( "1_500.jpg", "1_500_bl.jpg", True ),
                    ( "1_500.jpg", "1_500_bl2.jpg", True ),
                    ( "1_500.jpg", "1_500_c1.jpg", True ),
                    ( "1_500.jpg", "1_500_cr.jpg", True ),
                    ( "1_500.jpg", "1_500_f.jpg", True ),
                    ( "1_500.jpg", "1_500_left.jpg", True ),
                    #( "1_500.jpg", "1_500_wb.jpg", True ),
                    #( "1_500.jpg", "1_500_wl.jpg", True ),
                    ( "1_500.jpg", "1_500_sh-100.jpg", True ),
                    ( "1_500.jpg", "1_500_l+100.jpg", True ),
                    ( "1_500.jpg", "1_500_inv.jpg", True ),
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
                    ( "madonna-a.jpg", "madonna-sq.jpg", True ),

                )


    @data_provider( imgdDiff )
    def testDifferenceHash( self, f1, f2, e ):
        img1 = Image.read( "tests/core/images/" + f1 )
        img2 = Image.read( "tests/core/images/" + f2 )
        h1 = DHash( img1 )
        h2 = DHash( img2 )

        self.assertEquals( e, h1 == h2 )
        self.assertEquals( e, h1.distanceTo( h2 ) <= 11 )


if __name__ == '__main__':
    unittest.main()
