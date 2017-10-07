import nmap
print (nmap.__file__)

ns = nmap.PortScanner()
print(ns.nmap_version())
#ns.scan('127.0.0.1', '1-1000', '-v')
ns.scan('34.228.19.131', '22-445', '-sV')
#print(ns.scaninfo())
#print(ns.csv())
#ns.all_hosts()
print(ns.scanstats())
print(ns['34.228.19.131'].state())
print(ns['34.228.19.131'].all_protocols())
print(ns['34.228.19.131']['tcp'].keys())
print(ns['34.228.19.131'].has_tcp(22))



'''for host in nm.all_hosts():
    print('Host: %s (%s)' % (host, nm[host].hostname()))
    print('State: %s' % nm[host].state())
'''
