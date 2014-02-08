Image check tools
-----------------

Prototype of [Content-based image retrieval](http://en.wikipedia.org/wiki/Content-based_image_retrieval) based on perceptual hashes mostly used to find duplicate images.

Requires OpenCV.

The main feature is to extract fingerprints from an image.
These fingerprints should be very simple and easy comparable.

Such fingerprint is a 64 bit hash.

It can be matched/fetched using simple SQL query.
In case if it it very slow to match it would be good idea to use [HEngine](https://github.com/valbok/HEngine).

Following example shows matches using extracted hashes

    $ cd bin; ./bdm.py ../tests/images/lenna_cropped.jpg ../tests/images/lenna.jpg

[Example](https://github.com/valbok/img.chk/blob/master/bin/example.py):

    """ Scaled and copyrighted image """
    img1 = Image.read( "../tests/images/1.jpg" )
    img2 = Image.read( "../tests/images/1_500_cr.jpg" ) # scaled image with copyright watermark
    h1 = PHash( img1 )
    h2 = PHash( img2 )
    assert( h1 == h2 )

    """ Scaled and cropped image """
    img1 = Image.read( "../tests/images/madonna-a.jpg" )
    img2 = Image.read( "../tests/images/madonna-cropped-face2.jpg" )
    h1 = PHash( img1 )
    h2 = PHash( img2 )
    assert( h1 != h2 ) # should not be true due to huge modifications

    # In this case we could extract hashes from images and compare them
    cv = cv2.SURF( 400 )
    kp1 = cv.detect( img1.img, None )
    kp2 = cv.detect( img2.img, None )

    # Extract sub images
    imgs1 = Extractor( img1, kp1 ).subImages()
    imgs2 = Extractor( img2, kp2 ).subImages()

    # Match only PHash hashes
    matches = Matcher( [PHash] ).match( imgs1, imgs2 )

    assert( len( matches ) > 10 )

    """ Totally different image """
    img1 = Image.read( "../tests/images/lenna.jpg" )
    img2 = Image.read( "../tests/images/3_500.jpg" )

    kp1 = cv.detect( img1.img, None )
    kp2 = cv.detect( img2.img, None )

    imgs1 = Extractor( img1, kp1 ).subImages()
    imgs2 = Extractor( img2, kp2 ).subImages()

    matches = Matcher( [PHash] ).match( imgs1, imgs2 )

    assert( len( matches ) == 0 )

    """ Binary images """
    img1 = Image.read( "../tests/images/lenna_face.jpg" )
    img2 = Image.read( "../tests/images/lenna_full.jpg" )

    h1 = PHash( img1 )
    h2 = PHash( img2 )

    # No matches comparing whole images
    assert( h1 != h2 )

    cv = cv2.SURF( 400 )
    kp1 = cv.detect( img1.img, None )
    kp2 = cv.detect( img2.img, None )

    imgs1 = Extractor( img1, kp1 ).subImages()
    imgs2 = Extractor( img2, kp2 ).subImages()

    matches = Matcher( [PHash] ).match( imgs1, imgs2 )

    # No matches using sub images
    assert( len( matches ) == 0 )

    m = ( img1.width + img1.height ) / 2
    kp1, desc1 = cv2.ORB( m ).detectAndCompute( img1.img, None )
    e1 = Extractor( img1, kp1, desc1 )
    imgs1 = e1.binImages()

    m = ( img2.width + img2.height ) / 2
    kp2, desc2 = cv2.ORB( m ).detectAndCompute( img2.img, None )
    e2 = Extractor( img2, kp2, desc2 )
    imgs2 = e2.binImages()
    imgs2.append( img2 )

    matcher = Matcher( [PHash] )
    matches = matcher.match( imgs1, imgs2, 5 )

    # Found matches
    assert( len( matches ) > 0 )
