import dns.resolver
import sys
import pyfiglet
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("DNSEnum")
print(ascii_banner)

target = input(str( "TargetDomain: " ))

#Banner
print("_" * 50)
print("Scanning: " + target )
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)


record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']
try:
    domain = target
except IndexError:
    print('Syntax Error - python 3 DNSEnum.py <domainname>')
    quit()
for records in record_types:
    try:
        answer = dns.resolver.resolve(domain, records)
        print(f'\n{records} Records')
        print ('-'*30)
        for server in answer:
            print(server.to_text())
    except dns.resolver.NoAnswer: 
        print('Uh-oh, no record found. ')
        pass
    except dns.resolver.NXDOMAIN:
        print(f'{domain} does not exsist. ')
        quit()
    except KeyboardInterrupt:
        print('Hey! you interrupted my search, goodbye. ')
        quit()



#Credit @JoeHellethemayor on YouTube.