#!/usr/bin/python

from SOAPpy import WSDL
import re
import sys

WoRMS = WSDL.Proxy('http://www.marinespecies.org/aphia.php?p=soap&wsdl=1')

#id, parentid, acceptedid, rank, name,   extinct, marine, terrestrial, freshwater
def openFile(name):
    f=open('worms-'+name+'.txt', 'w')
    f.write("taxonID\tparentNameUsageID\tacceptedNameUsageID\ttaxonRank\tscientificName\tisExtinct\tisMarine\tisTerrestrial\tisFreshwater\n")
    return f

def printTax(f, t, accid, pid):
    print "%s %s %s" % (t.AphiaID, t.rank, t.scientificname)
    f.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (t.AphiaID, accid, pid, t.rank, t.scientificname, t.isExtinct, t.isMarine, t.isTerrestrial, t.isFreshwater))

def showObj(obj):
    for attr in vars(obj):
        if not attr.startswith("_"):
            print( "  %s: %s" % (attr, getattr(obj, attr)))

def showTax(tax, indent):
    space = "".join('  ' for i in xrange(indent))
    print "%s %s %s" % (space, tax.scientificname, tax.rank)

def get(id):
    return WoRMS.getAphiaRecordByID(id)

def walkTree(f, tax):
    syns = WoRMS.getAphiaSynonymsByID(id)
    if not syns == None:
        for s in syns:
            printTax(f, s, tax.AphiaID, "")
    #verns = WoRMS.getAphiaVernacularsByID(id)
    childs = WoRMS.getAphiaChildrenByID(tax.AphiaID)
    if not childs == None:
        for child in childs:
            if child.rank not in ["Family","Subfamily","Tribe","Genus"]:
                printTax(f, child, "", tax.AphiaID)
                walkTree(f, child)

def search(name):
    print 'search for: ', name
    repl = WoRMS.getAphiaRecords(name, like='true', fuzzy='false', marine_only='false', offset=0)
    if repl != None:
        for t in repl:
            print t


if len(sys.argv) == 1:
    print '  USAGE: ./worms.py taxon_name OR AphiaID'
    print '  EXAMPLE: ./worms.py Mytilus\ edulis'
    print '  KINGDOMS: 2=Animalia, 3=Plantae, 4=Fungi, 5=Protozoa, 6=Bacteria, 7=Chromista, 8=Archaea, 10=Viruses'

target_names = sys.argv[1:]
for n in target_names:
    try:
        id = int(n)
        f=openFile(n)
        root = get(id)
        printTax(f, root, "", "")
        walkTree(f, root)
        f.close()
    except ValueError:
        search(n)
    print '\n'