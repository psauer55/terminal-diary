import sys
import os
import time
import datetime
today = str(datetime.date.today()).replace("-",'_')
timestamp =  str(datetime.datetime.now()).split(".")[0]

home = os.path.expanduser("~")
datapath = os.environ.get("TERMINAL_NOTES_DIR", "{}/terminal-notes".format(home)).join("diary.noindex")

if not os.path.exists(datapath):
    os.makedirs(datapath)
os.chdir(datapath)

def main(args=None):
    try:
        score = sys.argv[1]
        print ("Starting new diary file for {}".format(today) )
        f = open('{}.txt'.format(today), 'a')
        f.write(timestamp)
        f.write("    "+score+"\n")
        f.close()
        os.system("open .")
        os.system("vim "+'{}.txt'.format(today))
    except (IndexError):
        print ('''
        --------------------------------------------------
        || WARNING: Don't forget enter a daily score !! ||
        --------------------------------------------------
        ''')
        print ('''
        ``diary`` : record a daily diary with a daily mood score 

        >    diary     <daily-score>  

        Ex) diary 8

        ''')
