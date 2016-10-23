import alexa
import dns.resolver
from python_hosts import Hosts, HostsEntry

ALEXA_TOP_COUNT = 1000
HOST_FILE_PATH = 'hosts_test'

hosts = Hosts(path = HOST_FILE_PATH)
for domain in alexa.top_list(ALEXA_TOP_COUNT):
        try:
                answers = dns.resolver.query(domain[1],'A')
                for rdata in answers:
                        hosts.add([HostsEntry(entry_type='ipv4', address=str(rdata), names=[domain[1]])])
                        hosts.write()
        except:
                pass
