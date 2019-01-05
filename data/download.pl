#!/usr/bin/env perl
use strict;
use warnings;

foreach my $y (1993..2018){
    my $x = $y + 1; 
    my $season = substr($y, 2) . substr($x, 2); 
    print "mkdir -p $y && cd $y\n"; 
    foreach my $div (0..4){ 
        print "wget http://www.football-data.co.uk/mmz4281/$season/E$div.csv\n";
    }
    print "cd ../\n";
}

