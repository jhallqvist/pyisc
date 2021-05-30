# DHCPd statements

| Original statement | Key | Value | Optional/Parameter |
| :----------------- | :-- | :---- | :----------------- |
|option all-subnets-local true;|option all-subnets-local|true|None|
|option arp-cache-timeout 3600;|option arp-cache-timeout|3600|None|
|option associated-ip ip-address [, ip-address... ];|option associated-ip|ip-address [, ip-address... ]|None|
|option bcms-controller-address ip-address [, ip-address... ];|option bcms-controller-address|ip-address [, ip-address... ]|None|
|option bcms-controller-names domain-list;|option bcms-controller-names|domain-list|None|
|option bootfile-name text;|option bootfile-name|text|None|
|option boot-size uint16;|option boot-size|uint16|None|
|option broadcast-address ip-address;|option broadcast-address|ip-address|None|
|option capwap-ac-v4 ip-address [, ip-address ... ];|option capwap-ac-v4|ip-address [, ip-address ... ]|None|
|option client-last-transaction-time uint32;|option client-last-transaction-time|uint32|None|
|option cookie-servers ip-address [, ip-address... ];|option cookie-servers|ip-address [, ip-address... ]|None|
|option default-ip-ttl uint8;|option default-ip-ttl|uint8|None|
|option default-tcp-ttl uint8;|option default-tcp-ttl|uint8|None|
|option default-url string;|option default-url|string|None|
|option dhcp-client-identifier string;|option dhcp-client-identifier|string|None|
|option dhcp-lease-time uint32;|option dhcp-lease-time|uint32|None|
|option dhcp-max-message-size uint16;|option dhcp-max-message-size|uint16|None|
|option dhcp-message text;|option dhcp-message|text|None|
|option dhcp-message-type uint8;|option dhcp-message-type|uint8|None|
|option dhcp-option-overload uint8;|option dhcp-option-overload|uint8|None|
|option dhcp-parameter-request-list uint8 [, uint8... ];|option dhcp-parameter-request-list|uint8 [, uint8... ]|None|
|option dhcp-rebinding-time uint32;|option dhcp-rebinding-time|uint32|None|
|option dhcp-renewal-time uint32;|option dhcp-renewal-time|uint32|None|
|option dhcp-requested-address ip-address;|option dhcp-requested-address|ip-address|None|
|option dhcp-server-identifier ip-address;|option dhcp-server-identifier|ip-address|None|
|option domain-name text;|option domain-name|text|None|
|option domain-name-servers ip-address [, ip-address... ];|option domain-name-servers|ip-address [, ip-address... ]|None|
|option domain-search domain-list;|option domain-search|domain-list|None|
|option extensions-path text;|option extensions-path|text|None|
|option finger-server ip-address [, ip-address... ];|option finger-server|ip-address [, ip-address... ]|None|
|option font-servers ip-address [, ip-address... ];|option font-servers|ip-address [, ip-address... ]|None|
|option geoconf-civic string;|option geoconf-civic|string|None|
|option host-name string;|option host-name|string|None|
|option ieee802-3-encapsulation flag;|option ieee802-3-encapsulation|flag|None|
|option ien116-name-servers ip-address [, ip-address... ];|option ien116-name-servers|ip-address [, ip-address... ]|None|
|option impress-servers ip-address [, ip-address... ];|option impress-servers|ip-address [, ip-address... ]|None|
|option interface-mtu uint16;|option interface-mtu|uint16|None|
|option ip-forwarding flag;|option ip-forwarding|flag|None|
|option irc-server ip-address [, ip-address... ];|option irc-server|ip-address [, ip-address... ]|None|
|option loader-configfile text;|option loader-configfile|text|None|
|option loader-pathprefix text;|option loader-pathprefix|text|None|
|option loader-reboottime uint32;|option loader-reboottime|uint32|None|
|option log-servers ip-address [, ip-address... ];|option log-servers|ip-address [, ip-address... ]|None|
|option lpr-servers ip-address [, ip-address... ];|option lpr-servers|ip-address [, ip-address... ]|None|
|option mask-supplier flag;|option mask-supplier|flag|None|
|option max-dgram-reassembly uint16;|option max-dgram-reassembly|uint16|None|
|option merit-dump text;|option merit-dump|text|None|
|option mobile-ip-home-agent ip-address [, ip-address... ];|option mobile-ip-home-agent|ip-address [, ip-address... ]|None|
|option name-service-search uint16 [, uint6... ];|option name-service-search|uint16 [, uint6... ]|None|
|option nds-context string;|option nds-context|string|None|
|option nds-servers ip-address [, ip-address... ];|option nds-servers|ip-address [, ip-address... ]|None|
|option nds-tree-name string;|option nds-tree-name|string|None|
|option netbios-dd-server ip-address [, ip-address... ];|option netbios-dd-server|ip-address [, ip-address... ]|None|
|option netbios-name-servers ip-address [, ip-address...];|option netbios-name-servers|ip-address [, ip-address...]|None|
|option netbios-node-type uint8;|option netbios-node-type|uint8|None|
|option netbios-scope string;|option netbios-scope|string|None|
|option netinfo-server-address ip-address [, ip-address... ];|option netinfo-server-address|ip-address [, ip-address... ]|None|
|option netinfo-server-tag text;|option netinfo-server-tag|text|None|
|option nis-domain text;|option nis-domain|text|None|
|option nis-servers ip-address [, ip-address... ];|option nis-servers|ip-address [, ip-address... ]|None|
|option nisplus-domain text;|option nisplus-domain|text|None|
|option nisplus-servers ip-address [, ip-address... ];|option nisplus-servers|ip-address [, ip-address... ]|None|
|option nntp-server ip-address [, ip-address... ];|option nntp-server|ip-address [, ip-address... ]|None|
|option non-local-source-routing flag;|option non-local-source-routing|flag|None|
|option ntp-servers ip-address [, ip-address... ];|option ntp-servers|ip-address [, ip-address... ]|None|
|option nwip-domain string;|option nwip-domain|string|None|
|option nwip-suboptions string;|option nwip-suboptions|string|None|
|option pxe-system-type uint16 [, uint16 ... ];|option pxe-system-type|uint16 [, uint16 ... ]|None|
|option pxe-interface-id uint8 uint8 uint8;|option pxe-interface-id|uint8 uint8 uint8|None|
|option pxe-client-id uint8 string;|option pxe-client-id|uint8 string|None|
|option option-6rd uint8 uint8 ip6-address ip-address [, ip-address ...];|option option-6rd|uint8 uint8 ip6-address ip-address [, ip-address ...]|None|
|option pana-agent ip-address [, ip-address ... ];|option pana-agent|ip-address [, ip-address ... ]|None|
|option path-mtu-aging-timeout uint32;|option path-mtu-aging-timeout|uint32|None|
|option path-mtu-plateau-table uint16 [, uint16... ];|option path-mtu-plateau-table|uint16 [, uint16... ]|None|
|option pcode text;|option pcode|text|None|
|option perform-mask-discovery flag;|option perform-mask-discovery|flag|None|
|option policy-filter ip-address ip-address [, ip-address ip-address...];|option policy-filter|ip-address ip-address [, ip-address ip-address...]|None|
|option pop-server ip-address [, ip-address... ];|option pop-server|ip-address [, ip-address... ]|None|
|option rdnss-selection uint8 ip-address ip-address domain-name;|option rdnss-selection|uint8 ip-address ip-address domain-name|None|
|option resource-location-servers ip-address [, ip-address...];|option resource-location-servers|ip-address [, ip-address...]|None|
|option root-path text;|option root-path|text|None|
|option router-discovery flag;|option router-discovery|flag|None|
|option router-solicitation-address ip-address;|option router-solicitation-address|ip-address|None|
|option routers ip-address [, ip-address... ];|option routers|ip-address [, ip-address... ]|None|
|option slp-directory-agent boolean ip-address [, ip-address... ];|option slp-directory-agent|boolean ip-address [, ip-address... ]|None|
|option slp-service-scope boolean text;|option slp-service-scope|boolean text|None|
|option smtp-server ip-address [, ip-address... ];|option smtp-server|ip-address [, ip-address... ]|None|
|option static-routes ip-address ip-address [, ip-address ip-address...];|option static-routes|ip-address ip-address [, ip-address ip-address...]|None|
|option streettalk-directory-assistance-server ip-address [, ip-address...];|option streettalk-directory-assistance-server|ip-address [, ip-address...]|None|
|option streettalk-server ip-address [, ip-address... ];|option streettalk-server|ip-address [, ip-address... ]|None|
|option subnet-mask ip-address;|option subnet-mask|ip-address|None|
|option subnet-selection ip-address;|option subnet-selection|ip-address|None|
|option swap-server ip-address;|option swap-server|ip-address|None|
|option tftp-server-address ip-address [, ip-address... ];|option tftp-server-address|ip-address [, ip-address... ]|None|
|option tcp-keepalive-garbage flag;|option tcp-keepalive-garbage|flag|None|
|option tcp-keepalive-interval uint32;|option tcp-keepalive-interval|uint32|None|
|option tcode text;|option tcode|text|None|
|option tftp-server-name text;|option tftp-server-name|text|None|
|option time-offset int32;|option time-offset|int32|None|
|option time-servers ip-address [, ip-address... ];|option time-servers|ip-address [, ip-address... ]|None|
|option trailer-encapsulation flag;|option trailer-encapsulation|flag|None|
|option uap-servers text;|option uap-servers|text|None|
|option user-class string;|option user-class|string|None|
|option v4-access-domain domain-name;|option v4-access-domain|domain-name|None|
|option v4-lost domain-name;|option v4-lost|domain-name|None|
|option vendor-class-identifier string;|option vendor-class-identifier|string|None|
|option vendor-encapsulated-options string;|option vendor-encapsulated-options|string|None|
|option vivso string;|option vivso|string|None|
|option www-server ip-address [, ip-address... ];|option www-server|ip-address [, ip-address... ]|None|
|option x-display-manager ip-address [, ip-address... ];|option x-display-manager|ip-address [, ip-address... ]|None|
|option agent.circuit-id string;|option agent.circuit-id|string|None|
|option agent.remote-id string;|option agent.remote-id|string|None|
|option agent.DOCSIS-device-class uint32;|option agent.DOCSIS-device-class|uint32|None|
|option agent.link-selection ip-address;|option agent.link-selection|ip-address|None|
|option fqdn.no-client-update flag;|option fqdn.no-client-update|flag|None|
|option fqdn.server-update flag;|option fqdn.server-update|flag|None|
|option fqdn.encoded flag;|option fqdn.encoded|flag|None|
|option fqdn.rcode1 flag;|option fqdn.rcode1|flag|None|
|option fqdn.rcode2 flag;|option fqdn.rcode2|flag|None|
|option fqdn.fqdn text;|option fqdn.fqdn|text|None|
|option fqdn.hostname --never set--;|option fqdn.hostname|--never set--|None|
|option fqdn.domainname --never set--;|option fqdn.domainname|--never set--|None|
|option nwip.nsq-broadcast flag;|option nwip.nsq-broadcast|flag|None|
|option nwip.preferred-dss ip-address [, ip-address... ];|option nwip.preferred-dss|ip-address [, ip-address... ]|None|
|option nwip.nearest-nwip-server ip-address [, ip-address...];|option nwip.nearest-nwip-server|ip-address [, ip-address...]|None|
|option nwip.autoretries uint8;|option nwip.autoretries|uint8|None|
|option nwip.autoretry-secs uint8;|option nwip.autoretry-secs|uint8|None|
|option nwip.nwip-1-1 uint8;|option nwip.nwip-1-1|uint8|None|
|option nwip.primary-dss ip-address;|option nwip.primary-dss|ip-address|None|
|option dhcp6.client-id string;|option dhcp6.client-id|string|None|
|option dhcp6.server-id string;|option dhcp6.server-id|string|None|
|option dhcp6.ia-na string;|option dhcp6.ia-na|string|None|
|option dhcp6.ia-ta string;|option dhcp6.ia-ta|string|None|
|option dhcp6.ia-addr string;|option dhcp6.ia-addr|string|None|
|option dhcp6.oro uint16 [ , uint16, ... ];|option dhcp6.oro|uint16 [ , uint16, ... ]|None|
|option dhcp6.preference uint8;|option dhcp6.preference|uint8|None|
|option dhcp6.elapsed-time uint16;|option dhcp6.elapsed-time|uint16|None|
|option dhcp6.relay-msg string;|option dhcp6.relay-msg|string|None|
|option dhcp6.unicast ip6-address;|option dhcp6.unicast|ip6-address|None|
|option dhcp6.status-code status-code [ string ];|option dhcp6.status-code|status-code [ string ]|None|
|option dhcp6.rapid-commit;|option dhcp6.rapid-commit||None|
|option dhcp6.vendor-opts string;|option dhcp6.vendor-opts|string|None|
|option dhcp6.interface-id string;|option dhcp6.interface-id|string|None|
|option dhcp6.reconf-msg dhcpv6-message;|option dhcp6.reconf-msg|dhcpv6-message|None|
|option dhcp6.reconf-accept;|option dhcp6.reconf-accept||None|
|option dhcp6.sip-servers-names domain-list;|option dhcp6.sip-servers-names|domain-list|None|
|option dhcp6.sip-servers-addresses ip6-address [, ip6-address ... ];|option dhcp6.sip-servers-addresses|ip6-address [, ip6-address ... ]|None|
|option dhcp6.name-servers ip6-address [, ip6-address ... ];|option dhcp6.name-servers|ip6-address [, ip6-address ... ]|None|
|option dhcp6.domain-search domain-list;|option dhcp6.domain-search|domain-list|None|
|option dhcp6.ia-pd string;|option dhcp6.ia-pd|string|None|
|option dhcp6.ia-prefix string;|option dhcp6.ia-prefix|string|None|
|option dhcp6.nis-servers ip6-address [, ip6-address ... ];|option dhcp6.nis-servers|ip6-address [, ip6-address ... ]|None|
|option dhcp6.nisp-servers ip6-address [, ip6-address ... ];|option dhcp6.nisp-servers|ip6-address [, ip6-address ... ]|None|
|option nis-domain-name domain-list;|option nis-domain-name|domain-list|None|
|option dhcp6.nis-domain-name domain-name;|option dhcp6.nis-domain-name|domain-name|None|
|option nisp-domain-name domain-list;|option nisp-domain-name|domain-list|None|
|option dhcp6.nisp-domain-name domain-name;|option dhcp6.nisp-domain-name|domain-name|None|
|option dhcp6.sntp-servers ip6-address [, ip6-address ... ];|option dhcp6.sntp-servers|ip6-address [, ip6-address ... ]|None|
|option dhcp6.info-refresh-time uint32;|option dhcp6.info-refresh-time|uint32|None|
|option dhcp6.bcms-server-d domain-list;|option dhcp6.bcms-server-d|domain-list|None|
|option dhcp6.bcms-server-a ip6-address [, ip6-address ... ];|option dhcp6.bcms-server-a|ip6-address [, ip6-address ... ]|None|
|option dhcp6.geoconf-civic string;|option dhcp6.geoconf-civic|string|None|
|option dhcp6.remote-id string;|option dhcp6.remote-id|string|None|
|option dhcp6.subscriber-id string;|option dhcp6.subscriber-id|string|None|
|option dhcp6.fqdn string;|option dhcp6.fqdn|string|None|
|option dhcp6.pana-agent ip6-address [, ip6-address ... ];|option dhcp6.pana-agent|ip6-address [, ip6-address ... ]|None|
|option dhcp6.new-posix-timezone text;|option dhcp6.new-posix-timezone|text|None|
|option dhcp6.new-tzdb-timezone text;|option dhcp6.new-tzdb-timezone|text|None|
|option dhcp6.ero uint16 [, uint16 ... ];|option dhcp6.ero|uint16 [, uint16 ... ]|None|
|option dhcp6.lq-query string;|option dhcp6.lq-query|string|None|
|option dhcp6.client-data string;|option dhcp6.client-data|string|None|
|option dhcp6.clt-time uint32;|option dhcp6.clt-time|uint32|None|
|option dhcp6.lq-relay-data ip6-address string;|option dhcp6.lq-relay-data|ip6-address string|None|
|option dhcp6.lq-client-link ip6-address [, ip6-address ... ];|option dhcp6.lq-client-link|ip6-address [, ip6-address ... ]|None|
|option dhcp6.v6-lost domain-name;|option dhcp6.v6-lost|domain-name|None|
|option dhcp6.capwap-ac-v6 ip6-address [, ip6-address ... ];|option dhcp6.capwap-ac-v6|ip6-address [, ip6-address ... ]|None|
|option dhcp6.relay-id string;|option dhcp6.relay-id|string|None|
|option dhcp6.v6-access-domain domain-name;|option dhcp6.v6-access-domain|domain-name|None|
|option dhcp6.sip-ua-cs-list domain-list;|option dhcp6.sip-ua-cs-list|domain-list|None|
|option dhcp6.bootfile-url text;|option dhcp6.bootfile-url|text|None|
|option dhcp6.bootfile-param string;|option dhcp6.bootfile-param|string|None|
|option dhcp6.client-arch-type uint16 [, uint16 ... ];|option dhcp6.client-arch-type|uint16 [, uint16 ... ]|None|
|option dhcp6.nii uint8 uint8 uint8;|option dhcp6.nii|uint8 uint8 uint8|None|
|option dhcp6.aftr-name domain-name;|option dhcp6.aftr-name|domain-name|None|
|option dhcp6.erp-local-domain-name domain-name;|option dhcp6.erp-local-domain-name|domain-name|None|
|option dhcp6.rdnss-selection ip6-address uint8 domain-name;|option dhcp6.rdnss-selection|ip6-address uint8 domain-name|None|
|option dhcp6.client-linklayer-addr string;|option dhcp6.client-linklayer-addr|string|None|
|option dhcp6.link-address ip6-address;|option dhcp6.link-address|ip6-address|None|
|option dhcp6.solmax-rt uint32;|option dhcp6.solmax-rt|uint32|None|
|option dhcp6.inf-max-rt uint32;|option dhcp6.inf-max-rt|uint32|None|
|v6relay(1, option dhcp6.subscriber-id) = "client_1";|v6relay(1, option dhcp6.subscriber-id)|"client_1"|None|
|option new-name code new-code = definition;|option new-name code new-code|definition|None|
|option new-name code new-code = boolean;|option new-name code new-code|boolean|None|
|option new-name code new-code = sign integer width;|option new-name code new-code|sign integer width|None|
|option new-name code new-code = ip-address;|option new-name code new-code|ip-address|None|
|option new-name code new-code = ip6-address;|option new-name code new-code|ip6-address|None|
|option new-name code new-code = text;|option new-name code new-code|text|None|
|option new-name code new-code = string;|option new-name code new-code|string|None|
|option new-name code new-code = domain-list [compressed];|option new-name code new-code|domain-list [compressed]|None|
|option new-name code new-code = encapsulate identifier;|option new-name code new-code|encapsulate identifier|None|
|option kerberos-servers code 200 = array of ip-address;|option kerberos-servers code 200|array of ip-address|None|
|option contrived-001 code 201 = { boolean, integer 32, text };|option contrived-001 code 201|{ boolean, integer 32, text }|None|
|option space name [ [ code width number ] [ length width number ] [ hash size number ] ];|option space|name [ [ code width number ] [ length width number ] [ hash size number ] ]|None|
