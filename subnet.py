import sys
class IP(object):
    def __init__(self,ip_address,cdir=24):
        if '/' in ip_address:
            self._address_val, self._cidr = ip_address.split('/')
            self._address = map(int, self._address_val.split('.'))
        else:
            self._address = map(int, ip_address.split('.'))
            self._cidr = cdir
        self.ip_addres = ip_address

    def dec_to_binary(self):
#        print(self._address)
        return map(lambda x: bin(x)[2:].zfill(8), self._address)


def calculate_sub(ip):
    myobj = IP(ip)
    binary = myobj.dec_to_binary()
    print("IP Address: ",binary)

x = input("Enter IP Address:")
calculate_sub(x)
