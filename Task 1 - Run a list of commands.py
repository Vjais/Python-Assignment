#Importing libraries
from subprocess import Popen
import time
import numpy as np

#sleep => delay for a specified amount of time
#ls -l => list directory contents( use a long listing format)
#find / => search for files in a directory hierarchy
# date =>print or set the system date and time
#uptime => Tell how long the system has been running

commands = ['sleep 3','ls -l /','find /','sleep 4','find /usr','date','sleep 5','uptime']
count = 0
processes = []
start = time.time()  #start time to calculate total elapse time
list_time_s=[]       #List to get start time of each command
for com in commands:
    print("running")
    # Start time of each command
    start_p = time.time()
    # append start time in list
    list_time_s.append(start_p)

    #process each command using popen()
    processes.append(Popen(com, shell=True))
    count += 1
    print ("Command " + str(count) + " begining to execute")
else:
    print("Finish..")

#List to get end time of each command
list_time_e=[]
#poll() to finish and terminate commands
for i, process in enumerate(processes):
    poll = process.poll()
    #end time of each command
    end_p = time.time()
    print ("Command #{} finished".format(i))
    #append end time in list
    list_time_e.append([end_p])
#endtime to calculate total elapse time
end = time.time()
#list for elapsed time of each command
lapse_time_p=[]
for a1,b1 in zip(np.asarray(list_time_e),np.asarray(list_time_s)):
    lapse_time_p.append(a1-b1)
print("kabootar")

#total elapsed time
elapsed = end - start
print("elapsed time is:",elapsed)

#maximum time of all commands
max_time=max(lapse_time_p)
print("maximum time is:",max_time)

#minimum time of all commands
min_time=min(lapse_time_p)
print("minimum time is:",min_time)

#average execution time of all commands
avg_time=sum(lapse_time_p)/len(lapse_time_p)
print("average time is:",avg_time)







