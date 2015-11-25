#!/usr/bin/python

from datetime import timedelta

with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime_minutes = uptime_seconds 

   # uptime_string = str(timedelta(seconds = uptime_seconds))


if uptime_minutes > warning_max_time:
        print "OK - your system has more than two days of uptime "
        sys.exit(0)
elif uptime_minutes":
        print "WARNING - %s of disk space used." % used_space
        sys.exit(1)
elif uptime_minutes :
        print "CRITICAL - %s of disk space used." % used_space
        sys.exit(2)
else:
        print "UKNOWN - problem running thi script"
        sys.exit(3)
