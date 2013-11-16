Image check tools
-----------------

Is supposed to use CBIR and other CV techniques.
Requires opencv lib.

Example:

    img1 = Image.read( "tests/core/images/1.jpg" )
    img2 = Image.read( "tests/core/images/1_500_cr.jpg" ) # scaled image with copyright watermark
    h1 = PHash( img1 )
    h2 = PHash( img2 )
    if h1 == h2 < 10:
        print "is similar" # will print this
