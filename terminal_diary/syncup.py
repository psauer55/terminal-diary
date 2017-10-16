import sys
import iforgot
import os

def main():

    print "Organizing all your notes. \n This may take a while ...."

    home = os.path.expanduser("~")
    datapath = os.environ.get("TERMINAL_NOTES_DIR", "{}/terminal-notes".format(home)).join("diary.noindex")

    if not os.path.exists(datapath):
        os.makedirs(datapath)
    os.chdir(datapath)

    try:
            pdf = sys.argv[1]
    except(IndexError):
            pdf = ""
    if pdf =="pdf":
            pdf=pdf+"!" #signify to organize.py to supress opening of pdf files
    if not os.path.exists("terminal-notes"):
            os.system("mkdir {}".format("terminal-notes"))
    os.chdir("terminal-notes")


    exclude  = open("exclude_keywords").readlines()
    print "Here are all the notes that I will organize:"
    os.system("iforgot")
    tags  = open("org_md/word.md").readlines()
    for t in tags:
            print "Organizing "+t[:-1]
            if t+'\n' not in exclude:
                    os.system("organize {0} notes {1}".format(t[:-1],pdf))
