Image check tools
-----------------

Is supposed to use CBIR and CV techniques

Example:

    img1 = Image( "tests/core/images/1.jpg" )
    img2 = Image( "tests/core/images/1_500_cr.jpg" ) # scaled image with copyright watermark
    h1 = img1.getPerceptualHash()
    h2 = img2.getPerceptualHash()
    b = Image.getHammingDistance( h1, h2 )
    if b < 10:
        print "is similar" # will print this
    else:
        print "is NOT similar"
