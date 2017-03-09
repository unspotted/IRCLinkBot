# This plugin posts a random BOFH excuse
# source: http://pages.cs.wisc.edu/~ballard/bofh/excuses

import random, linecache
def main(data):
    if 'excuse' in data['recv']:
        args = argv('!excuse', data['recv'])
        lines = sum(1 for line in open('bofh.txt'))
        excuse = linecache.getline('bofh.txt', random.randint(0, lines - 1))
        return say(args['channel'], excuse)
