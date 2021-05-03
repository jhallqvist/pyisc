# DHCPd statements

| Original statement | Key | Value | Optional/Parameter |
| :----------------- | :-- | :---- | :----------------- |
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
|allow after time;|allow|after time|None|
|deny after time;|deny|after time|None|
|class "ras-clients" {|class|"ras-clients"|None|
|match if substring (option dhcp-client-identifier, 1, 3) = "RAS";|match|if substring (option dhcp-client-identifier, 1, 3) = "RAS"|None|
|class "allocation-class-1" {|class|"allocation-class-1"|None|
|match pick-first-value (option dhcp-client-identifier, hardware);|match|pick-first-value (option dhcp-client-identifier, hardware)|None|
|class "allocation-class-2" {|class|"allocation-class-2"|None|
|match pick-first-value (option dhcp-client-identifier, hardware);|match|pick-first-value (option dhcp-client-identifier, hardware)|None|
|class "limited-1" {|class|"limited-1"|None|
|lease limit 4;|lease limit|4|None|
|subclass "allocation-class-1" 1:8:0:2b:4c:39:ad;|subclass|"allocation-class-1"|1:8:0:2b:4c:39:ad|
|subclass "allocation-class-2" 1:8:0:2b:a9:cc:e3;|subclass|"allocation-class-2"|1:8:0:2b:a9:cc:e3|
|subclass "allocation-class-1" 1:0:0:c4:aa:29:44;|subclass|"allocation-class-1"|1:0:0:c4:aa:29:44|
|subnet 10.0.0.0 netmask 255.255.255.0 {|subnet|10.0.0.0|netmask 255.255.255.0|
|pool {|pool|None|None|
|allow members of "allocation-class-1";|allow|members of "allocation-class-1"|None|
|range 10.0.0.11 10.0.0.50;|range|10.0.0.11 10.0.0.50|None|
|pool {|pool|None|None|
|allow members of "allocation-class-2";|allow|members of "allocation-class-2"|None|
|range 10.0.0.51 10.0.0.100;|range|10.0.0.51 10.0.0.100|None|
|subclass "allocation-class-2" 1:08:00:2b:a1:11:31 {|subclass|"allocation-class-2"|1:08:00:2b:a1:11:31|
|option root-path "samsara:/var/diskless/alphapc";|option root-path|"samsara:/var/diskless/alphapc"|None|
|filename "/tftpboot/netbsd.alphapc-diskless";|filename|"/tftpboot/netbsd.alphapc-diskless"|None|
|class "customer" {|class|"customer"|None|
|spawn with option agent.circuit-id;|spawn|with option agent.circuit-id|None|
|lease limit 4;|lease limit|4|None|
|class "jr-cable-modems" {|class|"jr-cable-modems"|None|
|match if option dhcp-vendor-identifier = "jrcm";|match|if option dhcp-vendor-identifier = "jrcm"|None|
|spawn with option agent.circuit-id;|spawn|with option agent.circuit-id|None|
|lease limit 4;|lease limit|4|None|
|class "dv-dsl-modems" {|class|"dv-dsl-modems"|None|
|match if option dhcp-vendor-identifier = "dvdsl";|match|if option dhcp-vendor-identifier = "dvdsl"|None|
|spawn with option agent.circuit-id;|spawn|with option agent.circuit-id|None|
|lease limit 16;|lease limit|16|None|
|include "filename";|include|"filename"|None|
|shared-network name {|shared-network|name|None|
|subnet subnet-number netmask netmask-dotted {|subnet|subnet-number|netmask netmask-dotted|
|subnet6 subnet6-number {|subnet6|subnet6-number|None|
|range [ dynamic-bootp ] low-address [ high-address];|range|[ dynamic-bootp ] low-address [ high-address]|None|
|range6 low-address high-address;|range6|low-address high-address|None|
|range6 subnet6-number;|range6|subnet6-number|None|
|range6 subnet6-number temporary;|range6|subnet6-number temporary|None|
|range6 address temporary;|range6|address temporary|None|
|prefix6 low-address high-address / bits;|prefix6|low-address|high-address|
|host hostname {|host|hostname|None|
|group {|group|None|None|
|key DHCP_UPDATER {|key|DHCP_UPDATER|None|
|algorithm HMAC-MD5.SIG-ALG.REG.INT;|algorithm|HMAC-MD5.SIG-ALG.REG.INT|None|
|secret pRP5FapFoJ95JEL06sv4PQ==;|secret|pRP5FapFoJ95JEL06sv4PQ==|None|
|zone EXAMPLE.ORG. {|zone|EXAMPLE.ORG.|None|
|primary 127.0.0.1;|primary|127.0.0.1|None|
|key DHCP_UPDATER;|key|DHCP_UPDATER|None|
|zone 17.127.10.in-addr.arpa. {|zone|17.127.10.in-addr.arpa.|None|
|primary 127.0.0.1;|primary|127.0.0.1|None|
|key DHCP_UPDATER;|key|DHCP_UPDATER|None|
|failover peer "failover" {|failover peer|"failover"|None|
|primary;|primary|None|None|
|address p-dhcp.ipamworldwide.com;|address|p-dhcp.ipamworldwide.com|None|
|port 519;|port|519|None|
|peer address f-dhcp.ipamworldwide.com;|peer address|f-dhcp.ipamworldwide.com|None|
|peer port 520;|peer port|520|None|
|max-response-delay 60;|max-response-delay|60|None|
|max-unacked-updates 10;|max-unacked-updates|10|None|
|mclt 3600;|mclt|3600|None|
|split 128;|split|128|None|
|load balance max 5;|load balance max|5|None|
|auto-partner-down 5;|auto-partner-down|5|None|
|failover peer "failover" {|failover peer|"failover"|None|
|secondary;|secondary|None|None|
|address p-dhcp.ipamworldwide.com;|address|p-dhcp.ipamworldwide.com|None|
|port 519;|port|519|None|
|peer address f-dhcp.ipamworldwide.com;|peer address|f-dhcp.ipamworldwide.com|None|
|peer port 520;|peer port|520|None|
|max-response-delay 60;|max-response-delay|60|None|
|max-unacked-updates 10;|max-unacked-updates|10|None|
|mclt 3600;|mclt|3600|None|
|hba ff:ff:ff:ff:ff:ff:ff:ff:00:00:00:00:00:00:00;|hba|ff:ff:ff:ff:ff:ff:ff:ff:00:00:00:00:00:00:00|None|
|load balance max 5;|load balance max|5|None|
|auto-partner-down 5;|auto-partner-down|5|None|
|failover peer 'name' state {|failover peer|'name'|state|
|my state partner-down;|my state|partner-down|None|
|peer state state at date;|peer state state at|date|None|
|subnet 10.0.2.0 netmask 255.255.254.0 {|subnet|10.0.2.0|netmask 255.255.254.0|
|option broadcast-address 10.0.3.255;|option broadcast-address|10.0.3.255|None|
|option subnet-mask 255.255.254.0;|option subnet-mask|255.255.254.0|None|
|option routers 10.0.3.254;|option routers|10.0.3.254|None|
|pool {|pool|None|None|
|failover peer "dhcp-failover";|failover peer|"dhcp-failover"|None|
|range 10.0.2.1 10.0.3.250;|range|10.0.2.1 10.0.3.250|None|
|max-lease-misbalance percentage;|max-lease-misbalance|percentage|None|
|max-lease-ownership percentage;|max-lease-ownership|percentage|None|
|min-balance seconds;|min-balance|seconds|None|
|max-balance seconds;|max-balance|seconds|None|
|abandon-lease-time time;|abandon-lease-time|time|None|
|adaptive-lease-time-threshold percentage;|adaptive-lease-time-threshold|percentage|None|
|always-broadcast flag;|always-broadcast|flag|None|
|always-reply-rfc1048 flag;|always-reply-rfc1048|flag|None|
|authoritative;|authoritative|None|None|
|not authoritative;|not|authoritative|None|
|boot-unknown-clients flag;|boot-unknown-clients|flag|None|
|check-secs-byte-order flag;|check-secs-byte-order|flag|None|
|db-time-format [ default | local ];|db-time-format|[ default \| local ]|None|
|ddns-hostname name;|ddns-hostname|name|None|
|ddns-domainname name;|ddns-domainname|name|None|
|ddns-dual-stack-mixed-mode flag;|ddns-dual-stack-mixed-mode|flag|None|
|ddns-guard-id-must-match flag;|ddns-guard-id-must-match|flag|None|
|ddns-local-address4 address;|ddns-local-address4|address|None|
|ddns-local-address6 address;|ddns-local-address6|address|None|
|ddns-other-guard-is-dynamic flag;|ddns-other-guard-is-dynamic|flag|None|
|ddns-rev-domainname name;|ddns-rev-domainname|name|None|
|ddns-update-style style;|ddns-update-style|style|None|
|ddns-updates flag;|ddns-updates|flag|None|
|default-lease-time time;|default-lease-time|time|None|
|delayed-ack count;|delayed-ack|count|None|
|max-ack-delay microseconds;|max-ack-delay|microseconds|None|
|dhcp-cache-threshold percentage;|dhcp-cache-threshold|percentage|None|
|do-forward-updates flag;|do-forward-updates|flag|None|
|dont-use-fsync flag;|dont-use-fsync|flag|None|
|dynamic-bootp-lease-cutoff W YYYY/MM/DD HH:MM:SS;|dynamic-bootp-lease-cutoff|W|YYYY/MM/DD|
|dynamic-bootp-lease-length length;|dynamic-bootp-lease-length|length|None|
|echo-client-id flag;|echo-client-id|flag|None|
|filename "filename";|filename|"filename"|None|
|fixed-address address [, address ... ];|fixed-address|address [, address ... ]|None|
|fixed-address6 ip6-address;|fixed-address6|ip6-address|None|
|fixed-prefix6 low-address / bits;|fixed-prefix6|low-address / bits|None|
|get-lease-hostnames flag;|get-lease-hostnames|flag|None|
|hardware hardware-type hardware-address;|hardware hardware-type|hardware-address|None|
|host-identifier option option-name option-data;|host-identifier option option-name|option-data|None|
|host-identifier v6relopt number option-name option-data;|host-identifier v6relopt number option-name|option-data|None|
|ignore-client-uids flag;|ignore-client-uids|flag|None|
|infinite-is-reserved flag;|infinite-is-reserved|flag|None|
|lease-file-name name;|lease-file-name|name|None|
|dhcpv6-lease-file-name name;|dhcpv6-lease-file-name|name|None|
|lease-id-format format;|lease-id-format|format|None|
|limit-addrs-per-ia number;|limit-addrs-per-ia|number|None|
|local-port port;|local-port|port|None|
|local-address address;|local-address|address|None|
|local-address6 address;|local-address6|address|None|
|bind-local-address6 flag;|bind-local-address6|flag|None|
|log-facility facility;|log-facility|facility|None|
|log-threshold-high percentage;|log-threshold-high|percentage|None|
|log-threshold-low percentage;|log-threshold-low|percentage|None|
|max-lease-time time;|max-lease-time|time|None|
|min-lease-time time;|min-lease-time|time|None|
|min-secs seconds;|min-secs|seconds|None|
|next-server server-name;|next-server|server-name|None|
|omapi-port port;|omapi-port|port|None|
|one-lease-per-client flag;|one-lease-per-client|flag|None|
|persist-eui-64-leases flag;|persist-eui-64-leases|flag|None|
|pid-file-name name;|pid-file-name|name|None|
|dhcpv6-pid-file-name name;|dhcpv6-pid-file-name|name|None|
|ping-check flag;|ping-check|flag|None|
|ping-cltt-secs seconds;|ping-cltt-secs|seconds|None|
|ping-timeout seconds;|ping-timeout|seconds|None|
|ping-timeout-ms milliseconds;|ping-timeout-ms|milliseconds|None|
|preferred-lifetime seconds;|preferred-lifetime|seconds|None|
|prefix-length-mode mode;|prefix-length-mode|mode|None|
|release-on-roam flag;|release-on-roam|flag|None|
|remote-port port;|remote-port|port|None|
|server-identifier hostname;|server-identifier|hostname|None|
|server-id-check flag;|server-id-check|flag|None|
|server-duid LLT [ hardware-type timestamp hardware-address ];|server-duid|LLT|[ hardware-type timestamp hardware-address ]|
|server-duid EN enterprise-number enterprise-identifier;|server-duid|EN|enterprise-number enterprise-identifier|
|server-duid LL [ hardware-type hardware-address ];|server-duid|LL|[ hardware-type hardware-address ]|
|server-name name;|server-name|name|None|
|dhcpv6-set-tee-times flag;|dhcpv6-set-tee-times|flag|None|
|site-option-space name;|site-option-space|name|None|
|stash-agent-options flag;|stash-agent-options|flag|None|
|update-conflict-detection flag;|update-conflict-detection|flag|None|
|update-optimization flag;|update-optimization|flag|None|
|update-static-leases flag;|update-static-leases|flag|None|
|use-eui-64 flag;|use-eui-64|flag|None|
|use-host-decl-names flag;|use-host-decl-names|flag|None|
|use-lease-addr-for-default-route flag;|use-lease-addr-for-default-route|flag|None|
|vendor-option-space string;|vendor-option-space|string|None|
