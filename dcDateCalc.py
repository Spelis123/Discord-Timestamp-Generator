import datetime
from pyperclip import copy

print("separate by space, leave blank for current time, format: YYYY MM DD HH MM SS")

def main():
    dt = input(">>>")

    if dt == "":
        dt = datetime.datetime.now()
        dt = str(dt).split("-")
        dt = " ".join(dt)
        dt = dt.split(":")[:2]
        dt = " ".join(dt)
        dt = dt.split(" ")
        d = []
        for i in dt:
            d.append(i.lstrip("0"))
    else:
        dt = dt.split(" ")
        d = []
        for i in dt:
            d.append(i.lstrip("0"))
    
    x = eval("int(datetime.datetime(" + ",".join(d) + ").timestamp())")
    y = input("Input Type. https://discord.com/developers/docs/reference#message-formatting-timestamp-styles\n>>>")
    copy("<t:" + str(x) + ":" + str(y) + ">")
    if input("Press enter to continue. Or enter X to exit.").lower() == "x":
        from sys import exit
        exit("User Exited.")

while 1:
    try:
        main()
    except Exception as e:
        print(e)
        if input("Press Enter to exit. Or input C and then Enter to continue") != "C":
            pass
        else:
            main()
