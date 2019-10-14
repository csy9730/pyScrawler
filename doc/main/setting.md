# setting

主要配置包括 
* download
* http
* autothrottle（自动限速）
* mail
* log

## misc
``` python
LOG_LEVEL= 'CRITICAL'# ERROR, WARNING, INFO, DEBUG
LOG_STDOUT = False
LOG_ENABLED = True
LOG_FILE = 'scapy.log'

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

DEPTH_LIMIT = 0
DEPTH_PRIORITY = 0
# request.priority = request.priority - ( depth * DEPTH_PRIORITY )
# Scope: scrapy.spidermiddlewares.depth.DepthMiddleware

TELNETCONSOLE_ENABLED

```


