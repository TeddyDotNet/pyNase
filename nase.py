#--------------------------
# NASE parser in Python 
# Autor: Christopher Uldack
#--------------------------

import sys
import naseLexer 
import naseParser



def compile(code, outfile):
    naseLexer.lexTheCode(code)
    ast = naseParser.parseCode(code)
    print ast
    return 0

# Starting point of nase parser. Read command line input, load file, begin compiling 
def main():

    # check parameter length and file ending
    if len(sys.argv) < 2:
        print "Error: No file to parse!"
        print "Usage: nase.py <Source-Datei>"
        sys.exit(1)

    naseFilename = sys.argv[1]

    destFilename = naseFilename[:-5] + '.s' # <datei>.nase -> <datei>.s  

    print "---------------------"
    print "CREATING FILE: %s" %(destFilename.upper())
    print "---------------------"

    # read NASE source file
    source = open(naseFilename, 'r')
    code = source.read()
    source.close()

    # create destination file
    dest = open(destFilename, 'w')

    print "---------------------"
    print "READING INPUT:"
    print "---------------------"
    print code

    # start compilation
    success = compile(code, dest) 

    # close destination file
    dest.close

    sys.exit(success)

if __name__ == '__main__':
    main()
