#encoding:UTF-8

import random
import unittest

from time import sleep
import json
import urllib2

#----------------------------------------------------------------------
def searchForSet(retX, retY, setNum, yr, numPce, origPrc):
    """"""
    #sleep(10)
    myAPIstr = 'get from code.google.com'
    searchURL = 'https://www.googleapis.com/shopping/search/v1/public/products?\
    key=%s&country=US&q=lego+%d&alt=json' %(myAPIstr, setNum)
    request = urllib2.Request(searchURL)
    request.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36')
    print request.get_header('User-agent')
    pg = urllib2.urlopen(request)
    retDict = json.loads(pg.read())
    for i in range(len(retDict['items'])):
        try:
            currItem = retDict['items'][i]
            if currItem['product']['condition'] == 'new':
                newFlag = 1
            else:
                newFlag = 0
            listOfInv = currItem['product']['inventories']
            for item in listOfInv:
                sellingPrice = item['price']
                if sellingPrice > origPrc * 0.5:
                    print '%d\t%d\t%d\t%f\t%f' %\
                          (yr, numPce, newFlag, origPrc, sellingPrice)
                    retX.append([yr, numPce, newFlag, origPrc])
                    retY.append(sellingPrice)
        except:
            print 'problem with item %d' %i
            
#----------------------------------------------------------------------
def setDataCollect(retX, retY):
    """"""
    searchForSet(retX, retY, 8288, 2006, 800, 49.99)
    searchForSet(retX, retY, 10030, 2002, 3096, 269.99)
    searchForSet(retX, retY, 10179, 2007, 5195, 499.99)
    searchForSet(retX, retY, 10181, 2007, 3428, 199.99)
    searchForSet(retX, retY, 10189, 2008, 5922, 299.99)
    searchForSet(retX, retY, 10196, 2009, 3263, 249.99)
    

if __name__ == '__main__':
    lgX = []
    lgY = []
    setDataCollect(lgX, lgY)