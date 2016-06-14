#!/usr/bin/python

import getopt
from sys import argv
from sys import exit
from os import listdir
from os.path import isfile, join
import numpy as np

def main(argv):
    helpMsg = 'getDistribution.py -i <inputfile> [-o <outputfile>]'
    if len(argv) < 1:
        print('Too few arguments')
        print(helpMsg)
        raise
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["help", "ifile=","ofile="])
    except getopt.GetoptError as e:
        print(helpMsg)
        raise(e)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(helpMsg)
            exit()
        elif opt in ('-i', '--ifile'):
            inputfile = arg
        elif opt in ('-o', '--ofile'):
            outputfile = arg
    if not isfile(inputfile):
        print('invalid input file %s' % inputfile)
        raise
    getDistribution(inputfile, outputfile)

def getDistribution(inputfile, outputfile):
    array = np.loadtxt(inputfile)
    m = array.min()
    M = array.max()
    median = np.median(array)
    miu = array.mean()
    sigma = array.std()
    if outputfile == '':
        print('min: %s, max: %s, median: %s, miu: %s, sigma: %s' % (m, M, median, miu, sigma))
    else:
        with open(outputfile, 'w+') as f:
            f.write('min: %s, max: %s, median: %s, miu: %s, sigma: %s' % (m, M, median, miu, sigma))


if __name__ == '__main__':
    main(argv[1:])