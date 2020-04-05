# pyUsageApi
Minimal Api to call system infos written in python

The api will run on port 8001
All objects will be returned as json obejcts

#Usage

localhost:5000/cpuinfo

Returns CPU usage in percent


localhost:5000/cpucount

Returns numbers of logical CPU cores


localhost:5000/temp

Returns temperatures


localhost:5000/netstat

Returns netstats


localhost:5000/uptime

Returns current uptime in seconds


localhost:5000/memoryinfo

Returns memory info
