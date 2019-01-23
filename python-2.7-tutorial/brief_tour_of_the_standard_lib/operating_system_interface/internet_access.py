import urllib2
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'EST' in line or 'EDT' in line:
        print line
#neend a mailserver running on localhost
# import smtplib
# server=smtplib.SMTP('localhost')
# server.sendmail('seehunter@163.com','seehunter@163.com')
# server.quit()