import datetime
print '-'*20
now = datetime.datetime.now()
print now
print now.year
print now.month
print '100 days ago, the date was ', now-datetime.timedelta(days=100)
birthday = datetime.datetime(2013,5,10)
print 'number of days to birthday ', birthday - now
print '10 days from now, month will be ',(now + datetime.timedelta(days=10)).day
print '-'*20
