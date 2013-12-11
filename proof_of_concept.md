Proof of concept
-----------------

Since our hash is just unsigned 64-bit integer we could store it into database and use a function like [BIT_COUNT](http://dev.mysql.com/doc/refman/5.0/en/bit-functions.html#function_bit-count) to calculate [Hamming distance](http://en.wikipedia.org/wiki/Hamming_Distance).

    SELECT * FROM image_hash WHERE BIT_COUNT( 0x2f1f76767e5e7f33 ^ hash ) <= 10

But this is quite expensive operation and could take a lot of time.

Current implementation extracts around 50 hashes per an image.
For example in case of 1000 image set in database to find a duplicate using just SQL query with BIT_COUNT function could take not less than 2 seconds.
Using custom implementation of hamming distance as MySQL extension takes almost the same time or even worse.
So decided to implement calculation of hamming distance in C++ and it decreased matching time twice.

www.artonym.net contains 1 235 indexed images and it is 85 465 hashes.
To find duplicate images by one image need to do 4 273 250 operations of hamming distance calculations.
The simplest our C++ implementation takes ~1 second to match hashes.
To filter false positive matches using python script could take one second more.

* Crop:

http://artonym.net/find/duplicates/1-madonna-cropped-face.jpg

http://artonym.net/find/duplicates/1-madonna-cropped-face2.jpg

http://artonym.net/find/duplicates/1-madonna-cropped-vertical.jpg

* Color, brightness, contrast and other hacks:

http://artonym.net/find/duplicates/1-madonna.jpg

http://artonym.net/find/duplicates/1-madonna-a1.jpg

http://artonym.net/find/duplicates/1-madonna-a2-line.jpg

http://artonym.net/find/duplicates/1-madonna-sq.jpg

http://artonym.net/find/duplicates/1-1_150.jpg

http://artonym.net/find/duplicates/1-1_500_bl.jpg

http://artonym.net/find/duplicates/1-1_500_bl2.jpg

http://artonym.net/find/duplicates/1-1_500_brb.jpg

http://artonym.net/find/duplicates/1-1_500_brightness-100.jpg

http://artonym.net/find/duplicates/1-1_500_brightness.jpg

http://artonym.net/find/duplicates/1-1_500_c1.jpg

http://artonym.net/find/duplicates/1-1_500_contrast.jpg

http://artonym.net/find/duplicates/1-1_500_cr.jpg

http://artonym.net/find/duplicates/1-1_500_f.jpg

http://artonym.net/find/duplicates/1-1_500_inv.jpg negative

http://artonym.net/find/duplicates/1-1_500_l+100.jpg

http://artonym.net/find/duplicates/1-1_500_left.jpg

http://artonym.net/find/duplicates/1-1_500_sh-100.jpg

http://artonym.net/find/duplicates/1-1_500_wb.jpg negative

http://artonym.net/find/duplicates/1-1_500_wl.jpg
