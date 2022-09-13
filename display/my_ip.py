import netifaces as ni

#ni.ifaddresses('eth0')
#ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlp0s20f3')[ni.AF_INET][0]['addr']
print(ip)  # should print "192.168.100.37"

