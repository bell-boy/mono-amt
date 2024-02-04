# extracts the inscripts from the datafile
from lxml import etree
import json
import tqdm
events = ("start", "end")
context = etree.iterparse("data/rism_231219.xml", events=events)

with open("data/transcripts.txt", "w") as output_file:
    cnt = 0
    max_inscripts = 90_000

    state = False # False corresponds to we're not looking at new data, True says we are looking at new data

    with tqdm.tqdm(total=max_inscripts) as pbar:
        for event, element in context:
            if(event == "start" and element.get("tag") == "031"):
                obj = {"clef": "",
                       "keysig": "",
                       "timesig": "",
                       "data": ""}
                state = True
            if(event == "end" and state == True and element.tag == "{http://www.loc.gov/MARC21/slim}datafield"):
                if(obj["clef"] != ""):
                    output_file.write(json.dumps(obj) + "\n")
                    cnt += 1
                    pbar.update(1)
                if(cnt >= max_inscripts):
                    break
                state = False

            if(event == "end"):
                element.clear()

            if(state == False):
                continue

            if(element.get("code") == "g" and event == "start"): # This is the Clef
                obj["clef"] = ''.join(element.itertext())
            if(element.get("code") == "n" and event == "start"): # THis is the Key Sig
                obj["keysig"] = ''.join(element.itertext())
            if(element.get("code") == "o" and event == "start"): # This is the Time sig
                obj["timesig"] = ''.join(element.itertext())
            if(element.get("code") == "p" and event == "start"): # This is the actual data
                obj["data"] = ''.join(element.itertext())
           
        