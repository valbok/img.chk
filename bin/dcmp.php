#!/usr/bin/env php
<?php
/**
 * @author VaL
 * @copyright Copyright (C) 2013 VaL::bOK
 * @license GNU GPL v2
 * @package img.chk
 */

/**
 * @return int
 */
function getPopCount( $value )
{
    $result = 0;
    while( $value )
    {
        $result += ($value & 1);
        $value = $value >> 1;
    }

    return $result;
}

/**
 * @param string HEX
 * @param string HEX
 * @return int
 */
function getHammingDistance( $hash1, $hash2 )
{
    return getPopCount( hexdec( $hash1 ) ^ hexdec( $hash2 ) );
}

/**
 * @return []
 */
function extractHashes( $path )
{
    $command = 'python dhashes.py ' . $path;
    $output = array();
    $r = 0;

    putenv( "PYTHONPATH=/usr/lib/python2.7/site-packages/" );
    exec( $command, $output, $r );

    $jsn = isset( $output[0] ) ? $output[0] : false;
    if ( !$jsn )
    {
        return array();
    }

    $array = json_decode( $jsn, true );
    $result = array();
    foreach ( $array as $key => $itemList )
    {
        foreach ( $itemList as $hash => $item )
        {
            $result[$key][] = $hash;
        }
    }

    return $result;
}

$fn1 = isset( $_SERVER['argv'][1] ) ? $_SERVER['argv'][1] : false;
if ( !$fn1 )
{
    exit;
}

$fn2 = isset( $_SERVER['argv'][2] ) ? $_SERVER['argv'][2] : false;
if ( !$fn2 )
{
    exit;
}

$hd = 3;
$hs1 = extractHashes( $fn1 );
$hs2 = extractHashes( $fn2 );
if ( !$hs1 or !$hs2 )
{
    exit;
}

$matched = array();
print "[" . count( $hs1['PHash'] ) . "] $fn1\n";
print "[" . count( $hs2['PHash'] ) . "] $fn2\n";
foreach ( $hs1['PHash'] as $h1 )
{
    foreach( $hs2['PHash'] as $h2 )
    {
        $d = getHammingDistance( $h1, $h2 );
        if ( $d <= $hd )
        {
            $matched[] = array( $h1, $h2, $d );
        }
    }
}

var_dump( $matched ) ."\n";
print "Found " . count( $matched ) . " matches using $hd distance.\n";

?>
