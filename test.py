from pyisc.dhcpd.nodes import Key, Failover, Pool4, Range4, Subnet4, Option, SharedNetwork, Global, ServerDuid
test = Failover(name='"test"')
test.mclt = 1
test.role ='primary'
test.address = '10.10.10.10'
test.peer_address = '10.10.10.11'
test.peer_port = 56
test.max_response_delay = 88
test.max_unacked_updates = 55
test.split = 128
test.hba = '00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00'
test.load_balance_max_seconds = 5


kaka = Pool4()
kaka.all_clients = 'allow'
kaka.allow_after = '2017/07/15 14:55:45'
kaka.allow_members_of = ['apa', 'test']
kaka.authenticated_clients = 'allow'
kaka.deny_members_of = ['njet', 'nopez']
kaka.dynamic_bootp_clients = 'deny'
kaka.failover_peer = test
kaka.known_clients = 'allow'
kaka.unauthenticated_clients = 'deny'
kaka.unknown_clients = 'deny'
kaka.add_range(Range4(start='10.10.10.10', end='10.10.10.20'))

apa = Subnet4('10.10.10.0/24')
apa.add_pool(kaka)
apa.add_range(Range4(start='10.10.10.10', end='10.10.10.20', flag='dynamic-bootp'))
apa.add_option(Option(name='domain-name', value='"example.org"'))

mongo = SharedNetwork('"224-01"')
mongo.add_subnet(apa)
mongo.add_option(Option(name='domain-name-servers', value='ns1.example.org, ns2.example.org'))
mongo.add_pool(Pool4(deny_members_of=['njet']))

haha = Key(name='DHCPD_UPDATER', secret='123', algorithm='SHA-512')

hoho = Global()
hoho.add_key(haha)
hoho.failover = test
hoho.add_shared_network(mongo)