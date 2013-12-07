Image check tools
-----------------

[Content-based image retrieval](http://en.wikipedia.org/wiki/Content-based_image_retrieval) implementation based on perceptual hashes used to find duplicates images.

Requires OpenCV.

The main feature is to extract fingerprints from an image that can be stored in a database and can be matched/fetched using simple SQL query.

Since our hash is just unsigned 64-bit integer we could store it into database and use a function like [BIT_COUNT](http://dev.mysql.com/doc/refman/5.0/en/bit-functions.html#function_bit-count) to calculate [Hamming distance](http://en.wikipedia.org/wiki/Hamming_Distance).

    SELECT * FROM image_hash WHERE BIT_COUNT( 0x2f1f76767e5e7f33 ^ hash ) <= 10

But this is quite expensive operation and could take a lot of time.

Current implementation extracts around 200 hashes per an image.
For example in case of 1000 image set in database to find a duplicate using just SQL query with BIT_COUNT function could take not less than 3 seconds.
Using custom implementation of hamming distance as MySQL extension takes almost the same time or even worse.
So decided to implement calculation of hamming distance in C++ and it decreased matching time twice.

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

Proof of concept
-----------------

www.artonym.net contains around 1 300 indexed images and it is around 260 000 hashes.
To find duplicate images by one image need to do around 52 000 000 operations of hamming distance calculations.
The simplest our C++ implementation takes ~1 second to match hashes.
To filter false positive matches using python script could take one second more.

* Crop:

http://artonym.net/find/duplicates/80454a83-madonna-cropped-face.jpg

http://artonym.net/find/duplicates/80454a83-madonna-cropped-face2.jpg

http://artonym.net/find/duplicates/80454a83-madonna-cropped-vertical.jpg

* Color, brightness, contrast and other hacks:

http://artonym.net/find/duplicates/80454a83-madonna.jpg

http://artonym.net/find/duplicates/80454a83-madonna-a1.jpg

http://artonym.net/find/duplicates/80454a83-madonna-a2-line.jpg

http://artonym.net/find/duplicates/80454a83-madonna-sq.jpg

http://artonym.net/find/duplicates/80454a83-1_150.jpg

http://artonym.net/find/duplicates/80454a83-1_500_bl.jpg

http://artonym.net/find/duplicates/80454a83-1_500_bl2.jpg

http://artonym.net/find/duplicates/80454a83-1_500_brb.jpg

http://artonym.net/find/duplicates/80454a83-1_500_brightness-100.jpg

http://artonym.net/find/duplicates/80454a83-1_500_brightness.jpg

http://artonym.net/find/duplicates/80454a83-1_500_c1.jpg

http://artonym.net/find/duplicates/80454a83-1_500_contrast.jpg

http://artonym.net/find/duplicates/80454a83-1_500_cr.jpg

http://artonym.net/find/duplicates/80454a83-1_500_f.jpg

http://artonym.net/find/duplicates/80454a83-1_500_inv.jpg negative

http://artonym.net/find/duplicates/80454a83-1_500_l+100.jpg

http://artonym.net/find/duplicates/80454a83-1_500_left.jpg

http://artonym.net/find/duplicates/80454a83-1_500_sh-100.jpg

http://artonym.net/find/duplicates/80454a83-1_500_wb.jpg negative

http://artonym.net/find/duplicates/80454a83-1_500_wl.jpg


