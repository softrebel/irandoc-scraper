import json
from irandoc.clean import clean_pattern_for_regex

f = open('nogorani_cleaned.json', 'r', encoding='utf-8')
content = json.loads(f.read())
tag_freq_dict = {}
for item in content:
    for tag in item['tags']:
        # caption = clean_pattern_for_regex(tag['title_fa'])
        caption = tag['title_fa']

        tag_freq_dict[caption] = tag_freq_dict.get(caption, 0) + 1

# with open('nogorani_tags.txt','w',encoding='utf-8') as f:
#     for key,value in tag_freq_dict.items():
#         f.write(f'{key},{value}\n')
# with open('nogorani_nodes.csv','w',encoding='utf-8') as f:
#     for key,value in tag_freq_dict.items():
#         f.write(f'{key},')
with open('nogorani_edges.csv', 'w', encoding='utf-8') as f:
    from igraph import *

    g = Graph()
    tag_keys = list(tag_freq_dict.keys())
    g.add_vertices(tag_keys)
    for item in content:
        tags_in_parseh = [tag['title_fa'] for tag in item['tags']]
        for tag_in_parseh in tags_in_parseh:
            for another_tag_in_parseh in tags_in_parseh:
                if another_tag_in_parseh != tag_in_parseh:
                    # n1 = tag_keys.index(tag_in_parseh)
                    # n2 = tag_keys.index(another_tag_in_parseh)
                    # g.add_edge(n1 , n2 )
                    g.add_edge(another_tag_in_parseh , tag_in_parseh )
    g.write_graphml("tags.graphml ")

    # f.write(f'{key},')
# print(content[-1]['facet_tags'])
