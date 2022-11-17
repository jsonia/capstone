from network import LoRa
import socket
import time
import ubinascii
from time import gmtime
import utime
from machine import RTC

rtc = RTC()
rtc.init((2022, 11, 15, 2, 21, 0, 0, 0))
print(rtc.now())


print('hello')
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)

app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('621156E57497EB32F619202C9BDB1BCA')

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')     

print('Joined')

def lora_cb(lora):  
    events = lora.events()
    if events & LoRa.TX_FAILED_EVENT:
        t = time.gmtime()
        print('Lora packet not sent', t)
    if events & LoRa.TX_PACKET_EVENT:
        t = time.gmtime()
        print('Lora packet sent', t)
    if events & LoRa.RX_PACKET_EVENT:
        t = time.gmtime()
        print('Lora packet received', t)     

lora.callback(trigger=(LoRa.RX_PACKET_EVENT | LoRa.TX_PACKET_EVENT | LoRa.TX_FAILED_EVENT), handler=lora_cb)
    
# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, 1)
s.setblocking(False)

s.send(bytes([0x01, 0x02, 0x03]))

t = time.gmtime()
print(t)

while(1):   
    data = s.recv(64)
    #lora.callback(LoRa.RX_PACKET_EVENT, handler=lora_cb)
    print(data)
    
    t = time.gmtime()
    print(t)
    #print('downlink received', t.tm_hour, ' ', t.tm_min, ' ', t.tm_sec)
    
    time.sleep(1);
