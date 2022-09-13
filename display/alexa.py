import socket
import threading
import logging
import time

from zeroconf import ServiceInfo, Zeroconf
from http.server import HTTPServer

localHTTP = None
zeroconf = None
info = None

LOCAL_HOST = "alexa.local"
LOCAL_PORT = 3000
BASE_URL = "http://" + LOCAL_HOST + ":" + str(LOCAL_PORT) + "/"


def get_local_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("www.amazon.com", 80))
    res = s.getsockname()[0]
    s.close()
    return res


def start():
    global localHTTP, zeroconf, info, httpthread
    ip = get_local_address()
    logging.info("Local IP is " + ip)
    host_ip = socket.gethostbyname(socket.gethostname())
    socket.inet_aton(host_ip)

    desc = {'version': '0.1'}
    info = ServiceInfo(type_="_WebCaster._tcp.local.",
                       name="Alexa Device._WebCaster._tcp.local.",
                       addresses=[socket.inet_aton(ip)],
                       port=LOCAL_PORT,
                       properties=desc,
                       server=LOCAL_HOST + ".")
    zeroconf = Zeroconf()
    zeroconf.register_service(info)
    logging.info("Local mDNS is started, domain is " + LOCAL_HOST)
    # localHTTP = HTTPServer(("", LOCAL_PORT), alexa_http_config.AlexaConfig)
    # httpthread = threading.Thread(target=localHTTP.serve_forever)
    # httpthread.start()
    logging.info("Local HTTP is " + BASE_URL)
    # alexa_control.start()
    while True:
        time.sleep(30)

start()
