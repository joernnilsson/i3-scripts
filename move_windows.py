
import i3ipc
import sys

i3 = i3ipc.Connection()

WS1 = '1: Chrome'
WS2 = '2: Terminals'
WS3 = '3: Slack'
WS4 = '4: Code'
WS5 = '5: Code'
WS6 = '6: Git'
WS7 = '7: Evernote'
WS8 = '8: '
WS9 = '9: '
WS0 = '10: '


rules = [
    ('class', "Google-chrome", WS1),
    ('class', "Slack", WS3),
    ('class', "Gnome-terminal", WS2),
    ('class', "VirtualBox.*", WS0),
    ('class', "Spotify", WS8),
    ('class', "Code", WS5),
    ('class', "jetbrains-clion", WS4),
    ('class', "GitKraken", WS6),
    ('class', "openttd", WS9),
    ('title', "Evernote Web$", WS7),
]

def move_class_to(tp, cl, ws):
    cmd = '['+tp+'="'+cl+'"] move container to workspace "'+ws+'"'
    print(cmd)
    i3.command(cmd)

print("Windows:")
for win in i3.get_tree().leaves():
    print(" - '" + win.window_class + "': '"+win.window_title+"'")


for r in rules:
    #print("('class': \""+cl+"\", WS),")
    move_class_to(r[0], r[1], r[2])
