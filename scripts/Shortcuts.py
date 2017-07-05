import csv

qute = ""
rang = ""
bash = ""
zshrc = ""

with open("/home/wilvin/.config/qutebrowser/keys.conf.base") as qb:
    qute+=qb.read()
with open("/home/wilvin/.config/ranger/rc.conf.base") as rg:
    rang+=rg.read()
with open("/home/wilvin/.dotfiles/scripts/bashrc") as bsh:
    bash+=bsh.read()
with open("/home/wilvin/.dotfiles/scripts/zshrc") as zsh: 
    zshrc+=zsh.read()

rang+=("\n# Autogenrated hotkeys\n")
bash+=("\n# AUTOGENERATED HOTKEYS AND ALIASES BEGIN HERE\n")
zshrc+=("\n# AUTOGENERATED HOTKEYS AND ALIASES BEGIN HERE\n")

with open("/home/wilvin/.dotfiles/scripts/folders") as fold:
    for line in csv.reader(fold, dialect="excel-tab"):
        qute+="set storage download-directory "+line[1]+" ;; hint links download\n\t;"+line[0]+"\n"
        rang+=("map g"+line[0]+" cd "+line[1]+"\n")
        rang+=("map t"+line[0]+" tab_new "+line[1]+"\n")
        rang+=("map m"+line[0]+" shell mv %s "+line[1]+"\n")
        rang+=("map Y"+line[0]+" shell cp %s "+line[1]+"\n")
        bash+=("alias "+line[0]+"=\"cd "+line[1]+" && ls -a\"\n")
        zshrc+=("alias "+line[0]+"=\"cd "+line[1]+" && ls -a\"\n")

with open("/home/wilvin/.dotfiles/scripts/configs") as conf:
    for line in csv.reader(conf, dialect="excel-tab"):
        bash+=("alias "+line[0]+"=\"nvim "+line[1]+"\"\n")
        zshrc+=("alias "+line[0]+"=\"nvim "+line[1]+"\"\n")
        rang+=("map "+line[0]+" shell nvim "+line[1]+"\n")

with open("/home/wilvin/.config/ranger/rc.conf", "w") as outrang:
    outrang.write(rang)
with open("/home/wilvin/.config/qutebrowser/keys.conf", "w") as outqb:
    outqb.write(qute)
with open("/home/wilvin/.bashrc", "w") as outbashrc:
    outbashrc.write(bash)
with open("/home/wilvin/.zshrc", "w") as outzshrc:
    outzshrc.write(zshrc)