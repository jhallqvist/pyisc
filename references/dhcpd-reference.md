# DHCPd statements

| Original statement | Key | Value | Optional parameter |
| :----------------- | :-- | :---- | :----------------- |
|abandon-lease-time time;|abandon-lease-time|time;|None|
|adaptive-lease-time-threshold percentage;|adaptive-lease-time-threshold|percentage;|None|
|always-broadcast flag;|always-broadcast|flag;|None|
|always-reply-rfc1048 flag;|always-reply-rfc1048|flag;|None|
|authoritative;|authoritative;|None|None|
|not authoritative;|not authoritative;|None|None|
|boot-unknown-clients flag;|boot-unknown-clients|flag;|None|
|check-secs-byte-order flag;|check-secs-byte-order|flag;|None|
|db-time-format [ default \| local ];|db-time-format|[ default \| local ];|None|
|ddns-hostname name;|ddns-hostname|name;|None|
|ddns-domainname name;|ddns-domainname|name;|None|
|ddns-dual-stack-mixed-mode flag;|ddns-dual-stack-mixed-mode|flag;|None|
|ddns-guard-id-must-match flag;|ddns-guard-id-must-match|flag;|None|
|ddns-local-address4 address;|ddns-local-address4|address;|None|
|ddns-local-address6 address;|ddns-local-address6|address;|None|
|ddns-other-guard-is-dynamic flag;|ddns-other-guard-is-dynamic|flag;|None|
|ddns-rev-domainname name;|ddns-rev-domainname|name;|None|
|ddns-update-style style;|ddns-update-style|style;|None|
|ddns-updates flag;|ddns-updates|flag;|None|
|default-lease-time time;|default-lease-time|time;|None|
|delayed-ack count;|delayed-ack|count;|None|
|max-ack-delay microseconds;|max-ack-delay|microseconds;|None|
|dhcp-cache-threshold percentage;|dhcp-cache-threshold|percentage;|None|
|do-forward-updates flag;|do-forward-updates|flag;|None|
|dont-use-fsync flag;|dont-use-fsync|flag;|None|
|dynamic-bootp-lease-cutoff W YYYY/MM/DD HH:MM:SS;|dynamic-bootp-lease-cutoff|W YYYY/MM/DD HH:MM:SS;|None|
|dynamic-bootp-lease-length length;|dynamic-bootp-lease-length|length;|None|
|echo-client-id flag;|echo-client-id|flag;|None|
|filename "filename";|filename|"filename";|None|
|fixed-address address [, address ... ];|fixed-address|address [, address ... ];|None|
|fixed-address6 ip6-address;|fixed-address6|ip6-address;|None|
|fixed-prefix6 low-address / bits;|fixed-prefix6|low-address / bits;|None|
|get-lease-hostnames flag;|get-lease-hostnames|flag;|None|
|hardware hardware-type hardware-address;|hardware hardware-type|hardware-address;|None|
|host-identifier option option-name option-data;|host-identifier option option-name|option-data;|None|
|host-identifier v6relopt number option-name option-data;|host-identifier v6relopt number option-name|option-data;|None|
|ignore-client-uids flag;|ignore-client-uids|flag;|None|
|infinite-is-reserved flag;|infinite-is-reserved|flag;|None|
|lease-file-name name;|lease-file-name|name;|None|
|dhcpv6-lease-file-name name;|dhcpv6-lease-file-name|name;|None|
|lease-id-format format;|lease-id-format|format;|None|
|limit-addrs-per-ia number;|limit-addrs-per-ia|number;|None|
|local-port port;|local-port|port;|None|
|local-address address;|local-address|address;|None|
|local-address6 address;|local-address6|address;|None|
|bind-local-address6 flag;|bind-local-address6|flag;|None|
|log-facility facility;|log-facility|facility;|None|
|log-threshold-high percentage;|log-threshold-high|percentage;|None|
|log-threshold-low percentage;|log-threshold-low|percentage;|None|
|max-lease-time time;|max-lease-time|time;|None|
|min-lease-time time;|min-lease-time|time;|None|
|min-secs seconds;|min-secs|seconds;|None|
|next-server server-name;|next-server|server-name;|None|
|omapi-port port;|omapi-port|port;|None|
|one-lease-per-client flag;|one-lease-per-client|flag;|None|
|persist-eui-64-leases flag;|persist-eui-64-leases|flag;|None|
|pid-file-name name;|pid-file-name|name;|None|
|dhcpv6-pid-file-name name;|dhcpv6-pid-file-name|name;|None|
|ping-check flag;|ping-check|flag;|None|
|ping-cltt-secs seconds;|ping-cltt-secs|seconds;|None|
|ping-timeout seconds;|ping-timeout|seconds;|None|
|ping-timeout-ms milliseconds;|ping-timeout-ms|milliseconds;|None|
|preferred-lifetime seconds;|preferred-lifetime|seconds;|None|
|prefix-length-mode mode;|prefix-length-mode|mode;|None|
|release-on-roam flag;|release-on-roam|flag;|None|
|remote-port port;|remote-port|port;|None|
|server-identifier hostname;|server-identifier|hostname;|None|
|server-id-check flag;|server-id-check|flag;|None|
|server-duid LLT [ hardware-type timestamp hardware-address ];|server-duid|LLT|[ hardware-type timestamp hardware-address ];|
|server-duid EN enterprise-number enterprise-identifier;|server-duid|EN|enterprise-number enterprise-identifier;|
|server-duid LL [ hardware-type hardware-address ];|server-duid|LL|[ hardware-type hardware-address ];|
|server-name name;|server-name|name;|None|
|dhcpv6-set-tee-times flag;|dhcpv6-set-tee-times|flag;|None|
|site-option-space name;|site-option-space|name;|None|
|stash-agent-options flag;|stash-agent-options|flag;|None|
|update-conflict-detection flag;|update-conflict-detection|flag;|None|
|update-optimization flag;|update-optimization|flag;|None|
|update-static-leases flag;|update-static-leases|flag;|None|
|use-eui-64 flag;|use-eui-64|flag;|None|
|use-host-decl-names flag;|use-host-decl-names|flag;|None|
|use-lease-addr-for-default-route flag;|use-lease-addr-for-default-route|flag;|None|
|vendor-option-space string;|vendor-option-space|string;|None|
