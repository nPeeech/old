import json
import sys

args = sys.argv[1]

#open
jso = open(args,'r')
json = json.load(jso) # >dict

class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'

for i in range(len(json['cells'])):
    
    #in
    print("") #Invalidation \n
    print(pycolor.BLUE + '_'*80 + pycolor.END) #print line
    print(pycolor.BLUE + "In [" + str(json['cells'][i]['execution_count']) + "]:" + pycolor.END) #print count
    
    for s in range(len(json['cells'][i]['source'])):
        print(pycolor.BLUE + "|" + pycolor.END + json['cells'][i]['source'][s],end='') #print [in]
    print("") #Invalidation \n
    print(pycolor.BLUE + '~'*80 + pycolor.END) #print line

    
    #result
    try:
        for o in range(len(json['cells'][i]['outputs'][0]['text'])):
            print("  " + json['cells'][i]['outputs'][0]['text'][o],end='') #print result
    except IndexError:
        pass
    except KeyError:
        pass

    #out
    try:
        for out in range(len(json['cells'][i]['outputs'][0]['data']['text/plain'])):
            print(pycolor.RED + "  " + json['cells'][i]['outputs'][0]['data']['text/plain'][out] + pycolor.END) #print out
    except IndexError:
        pass
    except KeyError:
        pass
jso.close()
