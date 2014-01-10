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
        imgs = Extractor( img, kp ).subImages( (1,2) )

        self.assertEquals( 1, len( imgs ) )
        self.assertEquals( True, isinstance( imgs[0], Image ) )

    imgDiff = lambda: \
                (
                    ( "1_500.jpg", "1_500_bl.jpg", True ),
                    ( "1_500.jpg", "1_500_bl2.jpg", True ),
                    ( "1_500.jpg", "1_500_c1.jpg", True ),
                    ( "1_500.jpg", "1_500_cr.jpg", True ),
                    ( "1_500.jpg", "1_500_f.jpg", True ),
                    ( "1_500.jpg", "1_500_left.jpg", True ),
                    #( "1_500.jpg", "1_500_wb.jpg", True ),
                    ( "1_500.jpg", "1_500_wl.jpg", True ),
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
                    ( "madonna-a1.jpg", "madonna-a.jpg", True ),
                    ( "madonna-a2-line.jpg", "madonna-a.jpg", True ),
                    ( "madonna-sq.jpg", "madonna-a.jpg", True ),
                    ( "madonna-cropped-face.jpg", "madonna-a.jpg", True ),
                    ( "madonna-cropped-face2.jpg", "madonna-a.jpg", True ),
                    ( "madonna-cropped-vertical.jpg", "madonna-a.jpg", True ),

                    ( "lenna_top.jpg", "lenna_full.jpg", True ),
                    ( "lenna_face.jpg", "lenna_full.jpg", True ),
                    ( "lenna_ass.jpg", "lenna_full.jpg", True ),
                    ( "lenna_cropped.png", "lenna.png", True ),

                )

    @data_provider( imgDiff )
    def testDescHashes( self, f1, f2, e ):
        cv = cv2.ORB()

        img1 = Image.read( "tests/core/images/" + f1 )
        kp1,desc1 = cv.detectAndCompute( img1.img, None )
        img2 = Image.read( "tests/core/images/" + f2 )
        kp2,desc2 = cv.detectAndCompute( img2.img, None )

        e1 = Extractor( img1, kp1, desc1 )
        e2 = Extractor( img2, kp2, desc2 )

        imgs1 = e1.descImages()
        imgs2 = e2.descImages()
        d = 3
        matcher = Matcher()
        matches = matcher.match( imgs1, imgs2, d )

        d = [m.type for m in matches if m.type == "DHash"]
        a = [m.type for m in matches if m.type == "AHash"]
        p = [m.type for m in matches if m.type == "PHash"]

        self.assertEquals( e, len( p ) > 0 )

    @data_provider( imgDiff )
    def testBinHashes( self, f1, f2, e ):
        img1 = Image.read( "tests/core/images/" + f1 )
        m = ( img1.width + img1.height ) / 2
        kp1,desc1 = cv2.ORB(m).detectAndCompute( img1.img, None )
        img2 = Image.read( "tests/core/images/" + f2 )
        m = ( img2.width + img2.height ) / 2
        kp2,desc2 = cv2.ORB(m).detectAndCompute( img2.img, None )

        e1 = Extractor( img1, kp1, desc1 )
        e2 = Extractor( img2, kp2, desc2 )

        imgs1 = e1.binImages()
        imgs1.append( img1 )
        imgs2 = e2.binImages()
        imgs2.append( img2 )
        d = 5
        matcher = Matcher()
        matches = matcher.match( imgs1, imgs2, d )

        d = [m.type for m in matches if m.type == "DHash"]
        a = [m.type for m in matches if m.type == "AHash"]
        p = [m.type for m in matches if m.type == "PHash"]

        #self.assertEquals( e, len( p ) > 0 )
        self.assertEquals( e, len( a ) > 0 )

if __name__ == '__main__':
    unittest.main()
