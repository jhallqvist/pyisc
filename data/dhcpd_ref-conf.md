# DHCPd statements

| Original statement | Key | Value | Optional/Parameter |
| :----------------- | :-- | :---- | :----------------- |
|pool {}|pool|None|None|
|pool6 {}|pool6|None|None|
|failover peer "name" state {}|failover peer|"name"|state|
|my state partner-down;|my state|partner-down|None|
|peer state state at date;|peer state state at|date|None|
|failover peer "name" {}|failover peer|"name"|None|
|primary;|primary|None|None|
|secondary;|secondary|None|None|
|address failover-partner.example.org;|address|failover-partner.example.org|None|
|address 10.10.10.56;|address|10.10.10.56|None|
|port 647;|port|647|None|
|peer address failover-partner.example.org;|peer address|failover-partner.example.org|None|
|peer address 10.10.10.56;|peer address|10.10.10.56|None|
|peer port 647;|peer port|647|None|
|max-response-delay 60;|max-response-delay|60|None|
|max-unacked-updates 10;|max-unacked-updates|10|None|
|mclt 3600;|mclt|3600|None|
|split 128;|split|128|None|
|load balance max 5;|load balance max|5|None|
|auto-partner-down 5;|auto-partner-down|5|None|
|max-lease-misbalance 25;|max-lease-misbalance|25|None|
|max-lease-ownership 25;|max-lease-ownership|25|None|
|min-balance 2789;|min-balance|2789|None|
|max-balance 3654;|max-balance|3654|None|
|class "ras-clients" {}|class|"ras-clients"|None|
|match if substring (option dhcp-client-identifier, 1, 3) = "RAS";|match|if substring (option dhcp-client-identifier, 1, 3) = "RAS"|None|
|class "allocation-class-1" {}|class|"allocation-class-1"|None|
|match pick-first-value (option dhcp-client-identifier, hardware);|match|pick-first-value (option dhcp-client-identifier, hardware)|None|
|class "allocation-class-2" {}|class|"allocation-class-2"|None|
|match pick-first-value (option dhcp-client-identifier, hardware);|match|pick-first-value (option dhcp-client-identifier, hardware)|None|
|class "customer" {}|class|"customer"|None|
|spawn with option agent.circuit-id;|spawn|with option agent.circuit-id|None|
|lease limit 4;|lease limit|4|None|
|subclass "allocation-class-1" 1:8:0:2b:4c:39:ad;|subclass|"allocation-class-1"|1:8:0:2b:4c:39:ad|
|subclass "allocation-class-2" 1:08:00:2b:a1:11:31 {}|subclass|"allocation-class-2"|1:08:00:2b:a1:11:31|
|zone EXAMPLE.ORG. {}|zone|EXAMPLE.ORG.|None|
|primary 127.0.0.1;|primary|127.0.0.1|None|
|primary6 0000:0000:0000:0000:0000:0000:0000:0001;|primary6|0000:0000:0000:0000:0000:0000:0000:0001|None|
|secondary 127.0.0.2;|secondary|127.0.0.2|None|
|secondary6 0000:0000:0000:0000:0000:0000:0000:0002;|secondary6|0000:0000:0000:0000:0000:0000:0000:0002|None|
|key DHCP_UPDATER;|key|DHCP_UPDATER|None|
|zone 17.127.10.in-addr.arpa. {}|zone|17.127.10.in-addr.arpa.|None|
|primary 127.0.0.1;|primary|127.0.0.1|None|
|key DHCP_UPDATER;|key|DHCP_UPDATER|None|
|on commit {}|on|commit|None|
|set ClientIP = binary-to-ascii(10, 8, ".", leased-address);|set|ClientIP = binary-to-ascii(10, 8, ".", leased-address)|None|
|set ClientMac = binary-to-ascii(16, 8, ":", substring(hardware, 1, 6));|set|ClientMac = binary-to-ascii(16, 8, ":", substring(hardware, 1, 6))|None|
|log(concat("Commit: IP: ", ClientIP, " Mac: ", ClientMac));|log|(concat("Commit: IP: ", ClientIP, " Mac: ", ClientMac))|None|
|execute("/usr/sbin/my_script_here", "commit", ClientIP, ClientMac);|execute|("/usr/sbin/my_script_here", "commit", ClientIP, ClientMac)|None|
|on expiry {}|on|expiry|None|
|on release {}|on|release|None|
|include "/etc/rndc.key";|include|"/etc/rndc.key"|None|
|shared-network "supertest" {}|shared-network|"supertest"|None|
|subnet 10.0.0.0 netmask 255.255.255.0 {}|subnet|10.0.0.0|netmask 255.255.255.0|
|subnet6 2001:db8:0:1::/64 {}|subnet6|2001:db8:0:1::/64|None|
|range dynamic-bootp 10.5.5.10 10.5.5.100;|range|dynamic-bootp 10.5.5.10 10.5.5.100|None|
|range 10.5.5.10 10.5.5.100;|range|10.5.5.10 10.5.5.100|None|
|range6 2001:db8:0:1::129 2001:db8:0:1::254;|range6|2001:db8:0:1::129 2001:db8:0:1::254|None|
|range6 2001:db8:0:1::/64;|range6|2001:db8:0:1::/64|None|
|range6 2001:db8:0:1::/64 temporary;|range6|2001:db8:0:1::/64|temporary|
|range6 2001:db8:0:1::129 temporary;|range6|2001:db8:0:1::129|temporary|
|prefix6 2001:db8:0:100:: 2001:db8:0:f00:: /56;|prefix6|2001:db8:0:100:: 2001:db8:0:f00:: /56|None|
|host "cookiemonster" {}|host|"cookiemonster"|None|
|group {}|group|None|None|
|allow unknown-clients;|allow|unknown-clients|None|
|deny unknown-clients;|deny|unknown-clients|None|
|ignore unknown-clients;|ignore|unknown-clients|None|
|allow bootp;|allow|bootp|None|
|deny bootp;|deny|bootp|None|
|ignore bootp;|ignore|bootp|None|
|allow booting;|allow|booting|None|
|deny booting;|deny|booting|None|
|ignore booting;|ignore|booting|None|
|allow duplicates;|allow|duplicates|None|
|deny duplicates;|deny|duplicates|None|
|allow declines;|allow|declines|None|
|deny declines;|deny|declines|None|
|ignore declines;|ignore|declines|None|
|allow client-updates;|allow|client-updates|None|
|deny client-updates;|deny|client-updates|None|
|allow leasequery;|allow|leasequery|None|
|deny leasequery;|deny|leasequery|None|
|allow known-clients;|allow|known-clients|None|
|deny known-clients;|deny|known-clients|None|
|allow unknown-clients;|allow|unknown-clients|None|
|deny unknown-clients;|deny|unknown-clients|None|
|allow members of "class";|allow|members of "class"|None|
|deny members of "class";|deny|members of "class"|None|
|allow dynamic bootp clients;|allow|dynamic bootp clients|None|
|deny dynamic bootp clients;|deny|dynamic bootp clients|None|
|allow authenticated clients;|allow|authenticated clients|None|
|deny authenticated clients;|deny|authenticated clients|None|
|allow unauthenticated clients;|allow|unauthenticated clients|None|
|deny unauthenticated clients;|deny|unauthenticated clients|None|
|allow all clients;|allow|all clients|None|
|deny all clients;|deny|all clients|None|
|allow after 27031680;|allow|after 27031680|None|
|allow after 4 2007/08/24 09:14:32;|allow|after 4 2007/08/24 09:14:32|None|
|allow after 4 2007/08/24 11:14:32 -7200;|allow|after 4 2007/08/24 11:14:32 -7200|None|
|deny after 27031680;|deny|after 27031680|None|
|deny after 4 2007/08/24 09:14:32;|deny|after 4 2007/08/24 09:14:32|None|
|deny after 4 2007/08/24 11:14:32 -7200;|deny|after 4 2007/08/24 11:14:32 -7200|None|
|abandon-lease-time 86400;|abandon-lease-time|86400|None|
|adaptive-lease-time-threshold 68;|adaptive-lease-time-threshold|68|None|
|always-broadcast on;|always-broadcast|on|None|
|always-reply-rfc1048 yes;|always-reply-rfc1048|yes|None|
|authoritative;|authoritative|None|None|
|not authoritative;|not authoritative|None|None|
|boot-unknown-clients false;|boot-unknown-clients|false|None|
|check-secs-byte-order enabled;|check-secs-byte-order|enabled|None|
|db-time-format local;|db-time-format|local|None|
|ddns-hostname "happylaptop";|ddns-hostname|"happylaptop"|None|
|ddns-domainname "example.org";|ddns-domainname|"example.org"|None|
|ddns-dual-stack-mixed-mode off;|ddns-dual-stack-mixed-mode|off|None|
|ddns-guard-id-must-match on;|ddns-guard-id-must-match|on|None|
|ddns-local-address4 172.16.16.5;|ddns-local-address4|172.16.16.5|None|
|ddns-local-address6 2001:db8:0:1::129;|ddns-local-address6|2001:db8:0:1::129|None|
|ddns-other-guard-is-dynamic off;|ddns-other-guard-is-dynamic|off|None|
|ddns-rev-domainname "in-addr.arpa";|ddns-rev-domainname|"in-addr.arpa"|None|
|ddns-update-style none;|ddns-update-style|none|None|
|ddns-updates on;|ddns-updates|on|None|
|default-lease-time 43200;|default-lease-time|43200|None|
|delayed-ack 0;|delayed-ack|0|None|
|max-ack-delay 250000;|max-ack-delay|250000|None|
|dhcp-cache-threshold 25;|dhcp-cache-threshold|25|None|
|do-forward-updates on;|do-forward-updates|on|None|
|dont-use-fsync yes;|dont-use-fsync|yes|None|
|dynamic-bootp-lease-cutoff 3 2021/10/24 13:05:55;|dynamic-bootp-lease-cutoff|3 2021/10/24 13:05:55|None|
|dynamic-bootp-lease-length 456;|dynamic-bootp-lease-length|456|None|
|echo-client-id off;|echo-client-id|off|None|
|filename "/tftpboot/netbsd.alphapc-diskless";|filename|"/tftpboot/netbsd.alphapc-diskless"|None|
|fixed-address 192.168.0.10;|fixed-address|192.168.0.10|None|
|fixed-address 192.168.0.10, 172.16.32.88;|fixed-address|192.168.0.10, 172.16.32.88|None|
|fixed-address "rover.example.org";|fixed-address|"rover.example.org"|None|
|fixed-address6 2001:db8:0:1::129;|fixed-address6|2001:db8:0:1::129|None|
|fixed-prefix6 2001:0db8:3000::/48;|fixed-prefix6|2001:0db8:3000::/48|None|
|get-lease-hostnames false;|get-lease-hostnames|false|None|
|hardware ethernet 00:00:00:00:00:00;|hardware ethernet|00:00:00:00:00:00|None|
|hardware token-ring 00:00:00:00:00:00;|hardware token-ring|00:00:00:00:00:00|None|
|host-identifier option dhcp6.client-id 00:01:00:01:4a:1f:ba:e3:60:b9:1f:01:23:45;|host-identifier option dhcp6.client-id|00:01:00:01:4a:1f:ba:e3:60:b9:1f:01:23:45|None|
|host-identifier v6relopt 33 dhcp6.subscriber-id 00:00:5e:00:53:12;|host-identifier v6relopt 33 dhcp6.subscriber-id|00:00:5e:00:53:12|None|
|ignore-client-uids true;|ignore-client-uids|true|None|
|infinite-is-reserved off;|infinite-is-reserved|off|None|
|lease-file-name "DBDIR/dhcpd.leases";|lease-file-name|"DBDIR/dhcpd.leases"|None|
|dhcpv6-lease-file-name "DBDIR/dhcpd6.leases";|dhcpv6-lease-file-name|"DBDIR/dhcpd6.leases"|None|
|lease-id-format octal;|lease-id-format|octal|None|
|limit-addrs-per-ia 1;|limit-addrs-per-ia|1|None|
|local-port 67;|local-port|67|None|
|local-address 10.10.10.10;|local-address|10.10.10.10|None|
|local-address6 2001:db8:0:1::129;|local-address6|2001:db8:0:1::129|None|
|bind-local-address6 disabled;|bind-local-address6|disabled|None|
|log-facility local7;|log-facility|local7|None|
|log-threshold-high 13;|log-threshold-high|13|None|
|log-threshold-low 34;|log-threshold-low|34|None|
|max-lease-time 86400;|max-lease-time|86400|None|
|min-lease-time 300;|min-lease-time|300|None|
|min-secs 255;|min-secs|255|None|
|next-server 192.168.1.5;|next-server|192.168.1.5|None|
|next-server "homie.example.org";|next-server|"homie.example.org"|None|
|omapi-port 7911;|omapi-port|7911|None|
|one-lease-per-client true;|one-lease-per-client|true|None|
|persist-eui-64-leases true;|persist-eui-64-leases|true|None|
|pid-file-name "/var/run/dhcpd.pid";|pid-file-name|"/var/run/dhcpd.pid"|None|
|dhcpv6-pid-file-name "DBDIR/dhcpd.pid";|dhcpv6-pid-file-name|"DBDIR/dhcpd.pid"|None|
|ping-check false;|ping-check|false|None|
|ping-cltt-secs 60;|ping-cltt-secs|60|None|
|ping-timeout 1;|ping-timeout|1|None|
|ping-timeout-ms 0;|ping-timeout-ms|0|None|
|preferred-lifetime 45;|preferred-lifetime|45|None|
|prefix-length-mode prefer;|prefix-length-mode|prefer|None|
|release-on-roam off;|release-on-roam|off|None|
|remote-port 68;|remote-port|68|None|
|server-identifier 10.10.10.58;|server-identifier|10.10.10.58|None|
|server-id-check on;|server-id-check|on|None|
|server-duid LLT [ hardware-type timestamp hardware-address ];|server-duid LLT|[ hardware-type timestamp hardware-address ]|None|
|server-duid EN enterprise-number enterprise-identifier;|server-duid EN|enterprise-number enterprise-identifier|None|
|server-duid LL [ hardware-type hardware-address ];|server-duid LL|[ hardware-type hardware-address ]|None|
|server-name "toccata.fugue.com";|server-name|"toccata.fugue.com"|None|
|dhcpv6-set-tee-times true;|dhcpv6-set-tee-times|true|None|
|site-option-space "pxelinux";|site-option-space|"pxelinux"|None|
|stash-agent-options true;|stash-agent-options|true|None|
|update-conflict-detection true;|update-conflict-detection|true|None|
|update-optimization false;|update-optimization|false|None|
|update-static-leases off;|update-static-leases|off|None|
|use-eui-64 true;|use-eui-64|true|None|
|use-host-decl-names on;|use-host-decl-names|on|None|
|use-lease-addr-for-default-route true;|use-lease-addr-for-default-route|true|None|
|vendor-option-space SUNW;|vendor-option-space|SUNW|None|
