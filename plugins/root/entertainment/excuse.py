# This plugin posts a random BOFH excuse
# source: http://pages.cs.wisc.edu/~ballard/bofh/excuses

def main(data):
    if 'excuse' in data['recv']:
        import random, linecache
        args = argv('!excuse', data['recv'])
        # hardcoded number of lines in excuse file
        excuse = linecache.getline('bofh.txt', random.randint(0, 465))
        return say(args['channel'], excuse)
