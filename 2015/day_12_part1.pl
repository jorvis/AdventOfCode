#!/usr/bin/env perl

use strict;
use warnings;

open(my $ifh, 'day_12.data') || die "Failed to open input file: $!";

my $sum = 0;

while (my $line = <$ifh>) {
    while ($line =~ /(\-*\d+)/g) {
        $sum += $1;
    }
}

print "The sum is: $sum\n";

