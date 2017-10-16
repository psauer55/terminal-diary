#!/usr/bin/env python2.7
#Organize a list of words that has be used as keywords and ignore certain keywords in exclude_keywords
import sys
import pandas as pd
import numpy as np
import os
import glob

home = os.path.expanduser("~")
datapath = os.environ.get("TERMINAL_NOTES_DIR", "{}/terminal-notes".format(home))

if not os.path.exists(datapath):
    os.makedirs(datapath)
os.chdir(datapath)

def main(args=None):
    date = ""
    time=""
    tag1=""
    tag2=""
    content=""
    year = '2016'
    mega_content  = []
    content = ""
    FIRST=True
    keyword="word"
    for filename in glob.glob("daily/{}_*.md".format(year)):
        f = open(filename)
        for line in f.readlines():
            if (line[:4]==year):
                if (FIRST):
                    line = line.split()
                    date = line[0]
                    time = line[1]
                    tags = line[2].split(",")
                    tag1 = tags[0]
                    try:
                        tag2 = tags[1]
                    except (IndexError):
                        tag2=""
                    content =""
                    FIRST=False
                else:
                    mega_content.append([date,time,tag1,tag2,content])
                    line = line.split()
                    date = line[0]
                    time = line[1]
                    tags = line[2].split(",")
                    tag1 = tags[0]
                    try:
                        tag2 = tags[1]
                    except (IndexError):
                        tag2=""
                    content =""
            else:
                content+=line
    mega_content.append([date,time,tag1,tag2,content])
    df = pd.DataFrame(mega_content, columns=['date', 'time', 'tag1','tag2','content'])
    if not os.path.exists("org_md"):
        os.makedirs("org_md")
    f = open("org_md/{}.md".format(keyword),'w')
    for index, row in df.iterrows():
        if row['tag1']==keyword or  row['tag2']==keyword:
            f.write(row['content'])
    f.close()
    if not os.path.exists("exclude_keywords"):
        f= open("exclude_keywords",'w') 
        f.close()
        exclude=[]
    else:
        exclude = open("exclude_keywords",'r').readlines()
    f = open("org_md/word.md",'w')
    for i in np.unique(df['tag1']):
        if (i+"\n" not in exclude):
            f.write(i+"\n")
    f.close()
    os.system("cat org_md/{}.md".format(keyword))
