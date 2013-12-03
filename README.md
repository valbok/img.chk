Image check tools
-----------------

Content-based image retrieval implementation based on perceptual hashes used to find similar or duplicates images.
The main feature is to extract fingerprints from an image that can be stored in a database and can be matched/found using simple SQL query.

Since our hash is just unsigned 64-bit integer we could store it into database and use a function like MySQL [BIT_COUNT](http://dev.mysql.com/doc/refman/5.0/en/bit-functions.html#function_bit-count) to calculate [Hamming distance](http://en.wikipedia.org/wiki/Hamming_Distance)

Requires OpenCV.

[Example](https://github.com/valbok/img.chk/blob/master/bin/example.py):

    # Scaled and copyrighted image
    img1 = Image.read( "../tests/core/images/1.jpg" )
    img2 = Image.read( "../tests/core/images/1_500_cr.jpg" ) # scaled image with copyright watermark
    h1 = PHash( img1 )
    h2 = PHash( img2 )
    assert( h1 == h2 )

    # Scaled and cropped image
    img1 = Image.read( "../tests/core/images/madonna-a.jpg" )
    img2 = Image.read( "../tests/core/images/madonna-cropped-face2.jpg" )
    h1 = PHash( img1 )
    h2 = PHash( img2 )
    assert( h1 != h2 ) # should not be true due to huge modifications

    # In this case we could extract hashes from images and compare them
    cv = cv2.SURF( 400 )
    kp1 = cv.detect( img1.img, None )
    kp2 = cv.detect( img2.img, None )

    # Extract sub images
    imgs1 = ImageExtractor( img1, kp1 ).extract()
    imgs2 = ImageExtractor( img2, kp2 ).extract()

    # Match only PHash hashes
    matches = Matcher( [PHash] ).match( imgs1, imgs2 )

    assert( len( matches ) > 10 )
