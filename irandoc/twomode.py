import json
import scipy.sparse as sp
import numpy as np
from igraph import *
f = open('nogorani_cleaned.json', 'r', encoding='utf-8')
content = json.loads(f.read())
tag_freq_dict = {}
item_tags = []
for item in content:
    # uuids.append(item['uuid'])
    item_tags.append([tag['title_fa'] for tag in item['tags']])
    for tag in item['tags']:
        caption = tag['title_fa']
        tag_freq_dict[caption] = tag_freq_dict.get(caption, 0) + 1

tags = list(tag_freq_dict.keys())
# row=np.arange(len(item_tags))
# col=np.arange(len(tags))
data = []
row = []
col = []
for i in range(len(item_tags)):
    for j in range(len(tags)):
        item = item_tags[i]
        tag = tags[j]
        if tag in item:
            row.append(i)
            col.append(j)
            data.append(1)

p = np.array(data, dtype=int)
nprow = np.array(row)
npcol = np.array(col)
csr = sp.csc_matrix((p, (nprow, npcol)), dtype=np.int32)
csrT = csr.transpose()
Parsehs=np.matmul(csr.toarray(),csrT.toarray())
Tags=np.matmul(csrT.toarray(),csr.toarray())



'''
build graph manual 


data2 = Tags.data
rows2 = Tags.nonzero()[0]
cols2 = Tags.nonzero()[1]
g = Graph()
g.add_vertices(len(data))
g.vs['name'] = tags
for i in range(len(rows2)):
    if rows2[i] != cols2[i]:
    #len(rows2)=len(cols2)
        g.add_edge(rows2[i],cols2[i])
'''

'''
build graph with Adjacency
'''
g=Graph.Adjacency(Tags,mode='undirected')
# g.vs['name'] = tags
g.vs['label'] = tags
g.write_graphml("tags_mode2_with_adjacency.graphml")