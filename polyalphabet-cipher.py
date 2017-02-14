# coding=utf-8
import sys, getopt
from string import ascii_lowercase
from collections import Counter

##----TODO-------
#
#
#
#encriptar pasando por parámetro el keyword
#
##--------------

def decrypt(keyword,inputfile,outputfile):
    if outputfile != 'none':
        archivo = open (output,"w")
    
    with open(inputfile) as mensaje
        for line in mensaje:
            key = 0
            for c in line:
                diferencia = (ord(c) - ord(keyword[key]))
                if diferencia == 0:
                    chLetra = 'z'
                elif diferencia > 0:
                    chLetra = chr(96 + diferencia)
                else:
                    chLetra = chr(122 + diferencia)
                if key == 5:
                    key = 0
                else:
                    key = key + 1
                if outputfile != 'none':
                    archivo.write(chLetra)
                else:
                    print chLetra,
    if outputfile != 'none':
        archivo.close()
        print 'Status : COMPLETED'

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hk:i:o:cd", ["keyword","ifile=","ofile="])
    except getopt.GetoptError:
        print 'polyalphabetic-cipher.py -<metodo> -k <keyword> -i <inputfile> -o <outputfile OR "none">'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'polyalphabet-cipher.py -<metodo> -k <keyword> -i <inputfile> -o <outputfile OR "none">'
            sys.exit()
        elif opt == "-c":
            metodo = 'crypt'
        elif opt == "-d":
            metodo = 'decrypt'
        elif opt in ("-w", "--keyword"):
            keyword = arg
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if metodo == 'decrypt':
        decrypt(keyword,inputfile,outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])

#def main(argv):
#    llave = 'd,a,g,g,e,r'
    #llave = 'c,r,u,c,i,f,i,x'
    #llave = 'c,r,o,s,s'
    #llave = 'c,h,r,i,s,t'
    
#    llave = llave.split(',')
#    puerta = 'puerta.txt'
    
#    letranueva = ''
#    with open(puerta) as puertafile:
#        for line in puertafile:
#            key = 0
#            for c in line:
#                diferencia = (ord(c) - ord(llave[key]))
#                if diferencia == 0:
#                    chLetra = 'z'
#                elif diferencia > 0:
#                    chLetra = chr(96 + diferencia)
#                else:
#                    chLetra = chr(122 + diferencia)
#                if key == 5:
#                    key = 0
#                else:
#                    key = key + 1
#                print chLetra,


#if __name__ == "__main__":
#    main(sys.argv[1:])
