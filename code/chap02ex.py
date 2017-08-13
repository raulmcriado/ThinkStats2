"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2
import math
import numpy as np

import nsfg

import thinkplot

def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    max_freq = 0
    for key ,freq in hist.Items():
        if freq> max_freq:
            max_freq = freq
            max_key = key
            
        
    return max_key


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    return sorted(hist.Items(),key=lambda item: item[1],reverse=True)
    
def stats_compare (live,firsts,others):
    """
    
    live: DataFrame of all live births
    firsts: DataFrame of firsts babies
    others: DataFrame of others
    """
    mean1 = live.totalwgt_lb.mean()
    mean2 = firsts.totalwgt_lb.mean()
    mean3 = others.totalwgt_lb.mean()
    
    var2 = firsts.totalwgt_lb.var()
    var3 = others.totalwgt_lb.var()
    
    print('Mean')
    print('First babies', mean2)
    print('Others', mean3)

    print('Variance')
    print('First babies', var2)
    print('Others', var3)

    print('Difference in lbs', mean2 - mean3)


    print('Difference relative to mean (%age points)', 
          (mean2 - mean3) / mean1 * 100)

    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print('Cohen d', d)    
    
    
    

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    
    preg = nsfg.ReadFemPreg()
    

    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]
    
    
    assert len(live) == 9148
    assert len(firsts) == 4413
    assert len(others) == 4735
    
   
    
    stats_compare(live,firsts,others)
       
    hist = thinkstats2.Hist(live.prglngth)
    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert(mode == 39)

    # test AllModes
    modes = AllModes(hist)
    assert(modes[0][1] == 4693)

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
