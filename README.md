# pyUsageApi
Minimal Api to call system infos written in python

The api will run on port 8001
All objects will be returned as json obejects

# Install
```
git clone https://github.com/arne-fuchs/pyUsageApi.git
```

```
cd pyUsageApi
```

```
sudo chmod +x install
```

```
./install
```

The program will be started in the background

You may want to add it to crontab with 

@reboot python3 /path/to/script/api.py 

Example for home folder:
```
@reboot python3 ~/pyUsageApi/api.py
```

# Usage

localhost:8001/cpuinfo

Returns CPU usage in percent:
{'cpu_percent': psutil.cpu_percent(interval=None,percpu=False)}

localhost:8001/cpucount

Returns numbers of logical CPU cores:
{'cpu_count':psutil.cpu_count()}

localhost:8001/temp

Returns temperatures:
{'sensors_temperatures':psutil.sensors_temperatures(fahrenheit=False)}

localhost:8001/netstat

Returns netstats:
{'net_stat':psutil.net_io_counters()}

localhost:8001/uptime

Returns current uptime in seconds:
{'uptime':uptime()}

localhost:8001/memoryinfo

Returns memory info:
