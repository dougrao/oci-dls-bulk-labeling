import datetime
import sys
import re
sys.path.append("..")
from config import *
import dls_create_annotation

def re_search(word):
    for l in labels:
        if re.search(l, word.lower()):
            return l 

def main(name, record_id):
    label = re_search(word=name)
    if label:
        dls_create_annotation.main(label=label, record_id=record_id)
    else:
        print("current time: " + str(datetime.datetime.now()))
        print("No label match for record " + str(n))
        print("with id: " + str(ids[count_records_in_batch]))
        print()