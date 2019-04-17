#! /usr/bin/env python3

# this script returns the fibonacci number at a specified position in the fibonacci sequence

import argparse

def get_args():

    #create an argument parser object 
    parser = argparse.ArgumentParser(description = 'this script returns the fibonacci number at a specified position')


    # add positional arguments, i.e., the required input
    #parser.add_argument( "-number", "--num", help="the fibonacci number you wish to calculate", type=int)

    # add positional arguments, i.e., the required input
    parser.add_argument("num", help="the fibonacci number you wish to calculate", type=int)

    # add optional arguments
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="print verbose output")
    group.add_argument("-s", "--simple", action="store_true", help="print simple output (default)")

    #action="store_true" makes the default false?

    # parse the command line arguments
    return parser.parse_args()


def fib(n):
    # calculate the fibonacci number
    a, b = 0, 1

    for i in range(n):
        a,b = b, a+b

    return(a)

def print_output(position, fib_num):
        #print the desired output
    if args.verbose:
        #verbose output
        print("for position", position, str(args.num), "the fibonacci numer is", fib_num)
    else:
        #simple output
        print(str(args.num), fib_num)

def main(): 
    fib_num = fib(args.num)
    print_output(args.num, fib_num)
    
# get the arguments before calling main
args = get_args()

# execute the program by calling main
if __name__== "__main__":
    main()


#functions for: 
#parsing fasta
#parsing gff
#function for gc content?
# function for reverse complement of a sequence
    # test for (+) or (-)?
        #will use the seqIO