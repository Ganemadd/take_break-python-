import webbrowser
import time
total_breaks = 3
break_count = 0
print("This program stared on" +time.ctime())
while(break_count<total_breaks):
    time.sleep(2*60*60)
    webbrowser.open("google.com")
    break_count=break_count+1
    print"Take your brake now"

