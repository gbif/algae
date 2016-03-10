#!/usr/bin/python
import csv

# hash of old id to new id
ids = {}
# kingdom ids
kidx = 1
# phylum ids
pidx = 100
# class ids
cidx = 1000
# other ids
oidx = 10000

def mapId(id, rank):
    global ids,kidx,pidx,cidx,oidx
    if id == None or id == "":
        return ""
    if ids.has_key(id):
        return ids.get(id)
    if rank == "kingdom":
        id2 = kidx
        kidx += 1
    elif rank == "phylum":
        id2 = pidx
        pidx += 1
    elif rank == "class":
        id2 = cidx
        cidx += 1
    else:
        id2 = oidx
        oidx += 1
    ids[id]=id2
    return id2


with open("algae.txt") as tsv, open("algae2.txt", "w") as out:
    writer = csv.writer(out, delimiter="\t")
    for line in csv.reader(tsv, delimiter="\t"):
        if len(line)>4:
            rank = line[3].lower()
            line[0]=mapId(line[0], rank)
            line[1]=mapId(line[1], rank)
            line[2]=mapId(line[2], rank)
            writer.writerow(line)
        else:            
            writer.writerow([])


