#!/usr/bin/env python3
'''
Python implementation of quicksort algorithm on a random list
'''
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', help='Length of list to sort',
                    type=int, default=10)
parser.add_argument('-s', '--start', help='Start number of random range',
                    type=int, default=1)
parser.add_argument('-e', '--end', help='End number of random range',
                    type=int, default=100)

args = parser.parse_args()


random_list = [random.randint(args.start, args.end)
               for i in range(args.length)]


def sort(lst):
    less = []
    equal = []
    greater = []
    if len(lst) > 1:
        pivot = lst[0]
        for i in lst:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                equal.append(i)
        return sort(less) + equal + sort(greater)
    else:
        return lst


if __name__ == '__main__':
    print('Before sort: {}'.format(random_list))
    print('After sort: {}'.format(sort(random_list)))
