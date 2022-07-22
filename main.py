# imports
from colorama import Fore, Back, Style
from datetime import datetime

# function
def basiclog(info, text, firstcolor):
    current_time = datetime.now().strftime("%H:%M:%S")
    if firstcolor == "GRN":
        infocolor = Back.GREEN
    else:
        if firstcolor == "YEL":
            infocolor = Back.YELLOW
        else:
            if firstcolor == "RED":
                infocolor = Back.RED
            else:
                if firstcolor == "none":
                    infocolor = ""
                else:
                    print("DEV: Set firstcolor (arg3) to " + Back.GREEN + "GRN" + Style.RESET_ALL + "/" + Back.YELLOW + "YEL" + Style.RESET_ALL + "/" + Back.RED + "RED" + Style.RESET_ALL + "/none. Not exiting")
                    infocolor = ""
    return Style.DIM + current_time + Style.RESET_ALL + " " + infocolor + info + Style.RESET_ALL + " " + text

# log
print(basiclog("sys0", "there log goes, you can there write everything.", "GRN"))
