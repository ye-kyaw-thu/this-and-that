#!/usr/bin/perl

# Shannon Entropy calculation for a given sentence
# Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Last Updated: 12 June 2022
# e.g. $ cat input.txt | perl ./calc-entropy.pl

# Reference: 
# https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
# https://codereview.stackexchange.com/questions/868/calculating-entropy-of-a-string
# https://math.stackexchange.com/questions/1573537/entropy-of-a-character-in-a-string
# https://rosettacode.org/wiki/Entropy
# shannonentropy.netmark.pl/calculate

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

# log2 calculation subroutine
sub log2 
{
   my $n = shift;
   return log($n) / log(2);
}

sub calc_entropy {
   my %freq; my $entropy=0; my $input_string = shift;
   my @chars = split(//, $input_string);
   $freq{$_}++ for @chars;

   foreach my $char (sort keys %freq)
   {
       my $p = $freq{$char}/@chars;
       print ("p for $char: $p\n");
       $entropy -= $p * log2($p);
   }
   return ($entropy);
}

foreach my $line (<>)
{
   chomp($line);
   print ("Entropy: ", calc_entropy($line), "\n\n");
}

