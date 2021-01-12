from sys import argv

open(argv[2], mode='w').write(open(argv[1]).read())