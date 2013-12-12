Image check tools
-----------------

[Content-based image retrieval](http://en.wikipedia.org/wiki/Content-based_image_retrieval) implementation based on perceptual hashes mostly used to find duplicate images.

Requires OpenCV.

The main feature is to extract fingerprints from an image that can be stored in a database and can be matched/fetched using simple SQL query.

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

    img1 = Image.read( "../tests/core/images/lenna.png" )
    # Totally different image
    img2 = Image.read( "../tests/core/images/3_500.jpg" )

    kp1 = cv.detect( img1.img, None )
    kp2 = cv.detect( img2.img, None )

    imgs1 = ImageExtractor( img1, kp1 ).extract()
    imgs2 = ImageExtractor( img2, kp2 ).extract()

    matches = Matcher( [PHash] ).match( imgs1, imgs2 )

    assert( len( matches ) == 0 )

Also it should be noted about Random Number Generator that is used in cv.kmeans using KMEANS_PP_CENTERS.
Each time when ImageExtractor().extract() is called using the same data different centroids will be generated.
That means that on each iteration extracted images will differ. It may produce wrong results within matching.

Following example shows how RNG may affect to matching.
There are 2 different images but with the same content. First image is a photo, second is a painted version of this photo.

For example first iteration did not return matched images at all.
But second returns 2 matches:

    cv = cv2.SURF( 400 )

    # Face with closed eyes and text
    img1 = Image.read( "../tests/core/images/madonna-bad-girl.jpg" )
    # Painted the same face without text
    img2 = Image.read( "../tests/core/images/madonna-cropped-face2.jpg" )

    kp1 = cv.detect( img1.img, None )
    kp2 = cv.detect( img2.img, None )

    # NOTE: Due to RNG extracted images are different per each iteration
    matches = []
    i = 0
    while len( matches ) == 0:
        imgs1 = ImageExtractor( img1, kp1 ).extract()
        imgs2 = ImageExtractor( img2, kp2 ).extract()
        matches = Matcher( [PHash] ).match( imgs1, imgs2 )
        i += 1

    print "Found", len( matches ), "matches on", i, "iteration"



