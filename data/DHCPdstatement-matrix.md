# DHCPd statement matrix

## Configuration Elements

|   Data Type    | Specifies |
| :------------- | :-------- |
| filename       | |
| domain-name    | A quoted ASCII string |
| subnet-number  | An ip-address type or a domain-name type |
| netmask        | An ip-address type or a domain-name type |
| subnet6-number | An IPv6 identifier specified as ip6-address/bits |
| low-address    | subnet-number or subnet6-number |
| high-address   | subnet-number or subnet6-number |
| time           | second since epoch, or a UTC time string e.g. 4 2007/08/24 09:14:32 or a string with time zone offset in seconds e.g. 4 2007/08/24 11:14:32 -7200 |
| boolean        | true or false |

### Failover-State

1. partner-down
2. normal
3. communications-interrupted
4. resolution-interrupted
5. potential-conflict
6. recover
7. recover-done
8. shutdown
9. paused
10. startup
11. recover-wait

### Text

None

### Date

W YYYY/MM/DD HH:MM:SS

### Time

Given in seconds.

## Matrix

| Original statement | Value Format | Default Value | Scopes |
| :--                           | :-- | :-- | :-- |
| pool {}                       | None | - | shared-network, subnet |
| pool6 {}                      | None | - | subnet6 |
| failover peer _name_ state {} | text | - | "Leases file" |
| my state _state_;             | failover-state | - | failover peer state |
| peer state _state_ at _date_; | date | | failover peer state |
| failover peer _name_ {}       | None | text | global, pool | <!-- Declaration is global and usage is can be in pool of subnet (then ending with a semicolon) -->
| primary;                      | None | failover peer _name_ | |
| secondary;                    | None | failover peer _name_ | |
| address _address_;            | ip-address OR domain-name | failover peer _name_ | |
| port _port-number_;           | uint32| | |
| peer address _address_;       | ip-address OR domain-name | | |
| peer address 10.10.10.56;     | | | |
| peer port 647;                | | | |
| max-response-delay 60;        | | | |
| max-unacked-updates 10;       | | | |
| mclt 3600;                    | | | | <!-- Should only be configured on Primary -->
| split 128;                    | | | | <!-- Should only be configured on Primary -->
| load balance max 5;           | | | |
| auto-partner-down 5;          | | | |
| max-lease-misbalance 25;      | | | |
| max-lease-ownership 25;       | | | |
| min-balance 2789;             | | | |
| max-balance 3654;             | | | |
| class "ras-clients" {}        | None | | |
| match if substring (option dhcp-client-identifier, 1, 3) = "RAS"; | | | |
| class "allocation-class-1" {} | None | | |
| match pick-first-value (option dhcp-client-identifier, hardware); | | | |
| class "allocation-class-2" {} | None | | |
| match pick-first-value (option dhcp-client-identifier, hardware); | | | |
| class "customer" {}           | None | | |
| spawn with option agent.circuit-id; | | | |
| lease limit 4;                | | | |
| subclass "allocation-class-1" 1:8:0:2b:4c:39:ad; | | | |
| subclass "allocation-class-2" 1:08:00:2b:a1:11:31 {} | | | |
| zone EXAMPLE.ORG. {} | | | |
| primary 127.0.0.1; | | | |
| primary6 0000:0000:0000:0000:0000:0000:0000:0001; | | | |
| secondary 127.0.0.2; | | | |
| secondary6 0000:0000:0000:0000:0000:0000:0000:0002; | | | |
| key DHCP_UPDATER; | | | |
| zone 17.127.10.in-addr.arpa. {} | | | |
| primary 127.0.0.1; | | | |
| key DHCP_UPDATER; | | | |
| on commit {} | | | |
| set ClientIP = binary-to-ascii(10, 8, ".", leased-address); | | | |
| set ClientMac = binary-to-ascii(16, 8, ":", substring(hardware, 1, 6)); | | | |
| log(concat("Commit: IP: ", ClientIP, " Mac: ", ClientMac)); | | | |
| execute("/usr/sbin/my_script_here", "commit", ClientIP, ClientMac); | | | |
| on expiry {} | | | |
| on release {} | | | |
| include "/etc/rndc.key"; | | | |
| shared-network "supertest" {} | | | |
| subnet 10.0.0.0 netmask 255.255.255.0 {} | | | |
| subnet6 2001:db8:0:1::/64 {} | | | |
| range dynamic-bootp 10.5.5.10 10.5.5.100; | | | subnet, pool |
| range 10.5.5.10 10.5.5.100; | | | subnet, pool  |
| range6 2001:db8:0:1::129 2001:db8:0:1::254; | | | subnet6, pool6 |
| range6 2001:db8:0:1::/64; | | | subnet6, pool6 |
| range6 2001:db8:0:1::/64 temporary; | | | subnet6, pool6 |
| range6 2001:db8:0:1::129 temporary; | | | subnet6, pool6 |
| prefix6 2001:db8:0:100:: 2001:db8:0:f00:: /56; | | | subnet6, pool6 |
| host "cookiemonster" {} | | | global, subnet, subnet6 |
| group {} | | | global |
| allow unknown-clients; | | | | <!-- DEPRECATED and replaced with similar in Pool scope -->
| deny unknown-clients; | | | |
| ignore unknown-clients; | | | |
| allow bootp; | | | global, subnet |
| deny bootp; | | | global, subnet |
| ignore bootp; | | | global, subnet |
| allow booting; | | | host |
| deny booting; | | | host |
| ignore booting; | | | host |
| allow duplicates; | | | |
| deny duplicates; | | | |
| allow declines; | | | |
| deny declines; | | | |
| ignore declines; | | | |
| allow client-updates; | | | |
| deny client-updates; | | | |
| allow leasequery; | | | |
| deny leasequery; | | | |
| allow known-clients; | | | |
| deny known-clients; | | | |
| allow unknown-clients; | | | |
| deny unknown-clients; | | | |
| allow members of "class"; | | | |
| deny members of "class"; | | | |
| allow dynamic bootp clients; | | | |
| deny dynamic bootp clients; | | | |
| allow authenticated clients; | | | |
| deny authenticated clients; | | | |
| allow unauthenticated clients; | | | |
| deny unauthenticated clients; | | | |
| allow all clients; | | | |
| deny all clients; | | | |
| allow after 27031680; | | | |
| allow after 4 2007/08/24 09:14:32; | | | |
| allow after 4 2007/08/24 11:14:32 -7200; | | | |
| deny after 27031680; | | | |
| deny after 4 2007/08/24 09:14:32; | | | |
| deny after 4 2007/08/24 11:14:32 -7200; | | | |
| abandon-lease-time _time_; | time | 86400 | global |
| adaptive-lease-time-threshold 68; | | | |
| always-broadcast _flag_; | boolean | - | conditional statement, class, host |
| always-reply-rfc1048 _flag_; | boolean | - | |
| authoritative; | - | - | global, subnet |
| not authoritative; | - | - | global, subnet |
| boot-unknown-clients false; | | | |
| check-secs-byte-order true; | | | |
| db-time-format local; | | | |
| ddns-hostname "happylaptop"; | | | |
| ddns-domainname "example.org"; | | | |
| ddns-dual-stack-mixed-mode off; | | | |
| ddns-guard-id-must-match on; | | | |
| ddns-local-address4 172.16.16.5; | | | |
| ddns-local-address6 2001:db8:0:1::129; | | | |
| ddns-other-guard-is-dynamic off; | | | |
| ddns-rev-domainname "in-addr.arpa"; | | | |
| ddns-update-style none; | | | |
| ddns-updates on; | | | |
| default-lease-time 43200; | | | |
| delayed-ack 0; | | | |
| max-ack-delay 250000; | | | |
| dhcp-cache-threshold 25; | | | |
| do-forward-updates on; | | | |
| dont-use-fsync true; | | | |
| dynamic-bootp-lease-cutoff 1623676561; | | | |
| dynamic-bootp-lease-length 456; | | | |
| echo-client-id off; | | | |
| filename "/tftpboot/netbsd.alphapc-diskless"; | | | |
| fixed-address 192.168.0.10; | | | |
| fixed-address 192.168.0.10, 172.16.32.88; | | | |
| fixed-address "rover.example.org"; | | | |
| fixed-address6 2001:db8:0:1::129; | | | |
| fixed-prefix6 2001:0db8:3000::/48; | | | |
| get-lease-hostnames false; | | | |
| hardware ethernet 00:00:00:00:00:00; | | | |
| hardware token-ring 00:00:00:00:00:00; | | | |
| host-identifier option dhcp6.client-id 00:01:00:01:4a:1f:ba:e3:60:b9:1f:01:23:45; | | | |
| host-identifier v6relopt 33 dhcp6.subscriber-id 00:00:5e:00:53:12; | | | |
| ignore-client-uids true; | | | |
| infinite-is-reserved off; | | | |
| lease-file-name "DBDIR/dhcpd.leases"; | | | |
| dhcpv6-lease-file-name "DBDIR/dhcpd6.leases"; | | | |
| lease-id-format octal; | | | |
| limit-addrs-per-ia 1; | | | |
| local-port 67; | | | |
| local-address 10.10.10.10; | | | |
| local-address6 2001:db8:0:1::129; | | | |
| bind-local-address6 disabled; | | | |
| log-facility local7; | | | |
| log-threshold-high 13; | | | |
| log-threshold-low 34; | | | |
| max-lease-time 86400; | | | |
| min-lease-time 300; | | | |
| min-secs 255; | | | |
| next-server 192.168.1.5; | | | |
| next-server "homie.example.org"; | | | |
| omapi-port 7911; | | | |
| one-lease-per-client true; | | | |
| persist-eui-64-leases true; | | | |
| pid-file-name "/var/run/dhcpd.pid"; | | | |
| dhcpv6-pid-file-name "DBDIR/dhcpd.pid"; | | | |
| ping-check false; | | | |
| ping-cltt-secs 60; | | | |
| ping-timeout 1; | | | |
| ping-timeout-ms 0; | | | |
| preferred-lifetime 45; | | | |
| prefix-length-mode prefer; | | | |
| release-on-roam off; | | | |
| remote-port 68; | | | |
| server-identifier 10.10.10.58; | | | |
| server-id-check on; | | | |
| server-duid LLT ethernet 1623675835 08:00:27:f8:35:72; | | | |
| server-duid EN 9 "a string"; | | | |
| server-duid LL ethernet 08:00:27:f8:35:72; | | | |
| server-name "toccata.fugue.com"; | | | |
| dhcpv6-set-tee-times true; | | | |
| site-option-space "pxelinux"; | | | |
| stash-agent-options true; | | | |
| update-conflict-detection true; | | | |
| update-optimization false; | | | |
| update-static-leases off; | | | |
| use-eui-64 true; | | | |
| use-host-decl-names on; | | | |
| use-lease-addr-for-default-route true; | | | |
| vendor-option-space SUNW; | | | |
