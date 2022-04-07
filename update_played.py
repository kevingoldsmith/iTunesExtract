import json
import xml.etree.ElementTree as ET

tree = ET.parse("data/iTunes Library.xml")
root = tree.getroot()
main_dict=root.findall('dict')
tracks_dict = None
for item in list(main_dict[0]):
    if item.tag=="dict":
        tracks_dict=item
        break
tracklist_xml=list(tracks_dict.findall('dict'))
tracklist_json=[]
for item in tracklist_xml:
    x=list(item)
    i=0
    track={}
    while i < len(x):
        track[x[i].text] = x[i+1].text
        i = i + 2
    tracklist_json.append(track)

with open('tracks.json', 'w') as f:
    f.write(json.dumps(tracklist_json))

