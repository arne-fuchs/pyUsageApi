# pyUsageApi
Minimal Api to call system infos written in python

The api will run on port 5000

#Usage

localhost:5000/cpuinfo
Returns string with CPU usage in percent

localhost:5000/cpucount
Returns string with numbers of logical CPU cores

localhost:5000/temp
Return string with temperatures (Doesnt work yet)

localhost:5000/netstat
Returns string with netstats

localhost:5000/uptime
Returns string with the current uptime in seconds

localhost:5000/memoryinfo
Retruns json object with memory info
