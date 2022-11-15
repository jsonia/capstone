from network import LoRa
import socket
import time
import ubinascii
from time import gmtime



print('hello')
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)

app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('621156E57497EB32F619202C9BDB1BCA')

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
def lora_cb(lora):  
    events = lora.events()
    if events & LoRa.TX_PACKET_EVENT:
        print('Lora packet sent')

print('Joined')
# create a LoRa socket

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, 1)
s.setblocking(False)

s.send(bytes([0x01, 0x02, 0x03]))
obj = time.gmtime()
print('uplink sent', obj)
# try:
#     s.send(bytes([0x01, 0x02, 0x03]))
# except OSError as e:
#     if e.args[0] == 11:
#         print("error occured")


#lora.callback(trigger=(LoRa.TX_PACKET_EVENT), handler=lora_cb)
#time.sleep(5)

while(1):
    data = s.recv(64)
    obj = time.gmtime()
    print(obj)
    print(data)

    time.sleep(10);



