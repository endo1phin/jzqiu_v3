import os
import json 
import codecs 
import markdown



# Markdown metadata: 
# ---
# title:   My Document
# summary: A brief description of my document.
# id: c-01
# ---

# index.json:
# {
#     "c-01": {
#         "title": "My Document",
#         "summary": "A brief description of my document.",
#         "last_modified": "2020-2-20",
#         "category": "Career",
#     }
# }


HTML_OUTPUT_DIR = '../app/templates/notes_html/'

# translate category letter to readable cateogory names
ID_CAT = {
    'a': 'Algorithm',
    'b': 'CS Basics',
    'c': 'Career',
    'd': 'Application',
    'e': 'Others',
    'x': 'Test'
}


# add info to Markdown object meta dictionary for server readability
def dict_from_meta(md_meta, os_last_modified): 
    d = {}
    d['title'] = meta['title'][0]
    d['summary'] = meta['summary'][0]
    d['id'] = md_meta['id'][0]

    cat = d['id'].split('-')[0]
    d['category'] = ID_CAT[cat]
    d['last_modified'] = os_last_modified
    return d


if __name__ == "__main__":
    list_of_mds = ['notes/'+d for d in os.listdir('notes')]
    
    index = []    

    # initiate an instance of parer, with meta extension
    md = markdown.Markdown(extensions=['meta'])

    for md_dir in list_of_mds:
        # print('...writing ' + md_dir)
        file = codecs.open(md_dir, mode="r", encoding="utf-8")
        text = file.read()
        html = md.convert(text)
        
        meta = md.Meta
        last_modified = os.path.getmtime(md_dir)
        meta_d = dict_from_meta(meta, last_modified)
        index.append(meta_d)
        
        # overwrites html
        with open(HTML_OUTPUT_DIR+meta_d['id']+'.html', 'w+') as html_f:
            html_f.write(html)
            
        md.reset()
    # print(index)

    index = sorted(index, key=lambda d: d['last_modified'], reverse=True)
    
    # overwrites index json
    with open('index.json', 'w') as index_f:
        json.dump(index, index_f)

    # print('Done.')
    
        

        