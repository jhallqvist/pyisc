from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyisc.dhcpd.nodes import (
        Subnet4, Pool4, Range4, Option4, Class, 
        Group, Host, SharedNetwork, SubClass, Zone, Key, Include)

# Methods to be inherited by objects in order to reduce duplicate code.
# All add methods currently expects a object instance.
class SubnetMixin:
    """add, delete, get, modify, search in list of subnets."""
    def add_subnet(self, subnet: 'Subnet4'):
        self.subnets.append(subnet)
    def find_subnet(self, network):
        for subnet in self.subnets:
            if subnet.network == network:
                return subnet
    def delete_subnet(self, network):
        found_subnet = self.find_subnet(network)
        self.subnets.remove(found_subnet)


class RangeMixin:
    def add_range(self, range: 'Range4'):
        self.ranges.append(range)
    def find_range():
        pass
    def delete_range():
        pass

class PoolMixin:
    def add_pool(self, pool: 'Pool4'):
        self.pools.append(pool)
    def find_pool():
        pass # How to find an object whose uniqeness is defined by its attributes?
    def delete_pool(self, pool):
        # use find pool
        # use self.pool.remove(found_pool)
        pass

class OptionMixin:
    def add_option(self, option: 'Option4'):
        self.options.append(option)
    def find_option(self, option):
        pass
    def delete_option(self, option):
        pass

class HostMixin:
    def add_host(self, host: 'Host'):
        self.hosts.append(host)
    def find_host(self, host):
        pass
    def delete_host(self, host):
        pass

class GroupMixin:
    def add_group(self, group: 'Group'):
        self.groups.append(group)
    def find_group(self, group):
        pass
    def delete_group(self, group):
        pass

class ClassMixin:
    def add_class(self, class_obj: 'Class'):
        self.classes.append(class_obj)
    def find_class(self, class_obj):
        pass
    def delete_class(self, class_obj):
        pass

class SubClassMixin:
    def add_subclass(self, subclass: 'SubClass'):
        self.subclasss.append(subclass)
    def find_subclass(self, subclass):
        pass
    def delete_subclass(self, subclass):
        pass

class SharedNetworkMixin:
    def add_shared_network(self, shared_network: 'SharedNetwork'):
        self.shared_networks.append(shared_network)
    def find_shared_network(self, shared_network):
        pass
    def delete_shared_network(self, shared_network):
        pass

class ZoneMixin:
    def add_zone(self, zone: 'Zone'):
        self.zones.append(zone)
    def find_zone(self, zone):
        pass
    def delete_zone(self, zone):
        pass

class KeyMixin:
    def add_key(self, key: 'Key'):
        self.keys.append(key)
    def find_key(self, key):
        pass
    def delete_key(self, key):
        pass

class IncludeMixin:
    def add_include(self, include: 'Include'):
        self.includes.append(include)
    def find_include(self, include):
        pass
    def delete_include(self, include):
        pass

class Parameters:
    def __init__(
        self,
        # abandon_lease_time=None,
        adaptive_lease_time_threshold=None,
        # always_broadcast=None,
        always_reply_rfc1048=None,
        # authoritative=None,
        boot_unknown_clients=None,
        check_secs_byte_order=None,
        # db_time_format=None,
        ddns_hostname=None,
        ddns_domainname=None,
        # ddns_dual_stack_mixed_mode=None,
        # ddns_guard_id_must_match=None,
        ddns_local_address4=None,
        ddns_local_address6=None,
        # ddns_other_guard_is_dynamic=None,
        ddns_rev_domainname=None,
        ddns_update_style=None,
        ddns_updates=None,
        default_lease_time=None,
        delayed_ack=None,
        max_ack_delay=None,
        dhcp_cache_threshold=None,
        do_forward_updates=None,
        dont_use_fsync=None,
        dynamic_bootp_lease_cutoff=None,
        dynamic_bootp_lease_length=None,
        echo_client_id=None,
        filename=None,
        fixed_address=None,
        fixed_address6=None,
        fixed_prefix6=None,
        get_lease_hostnames=None,
        hardware_type=None,
        hardware_address=None,
        ignore_client_uids=None,
        infinite_is_reserved=None,
        # lease_file_name=None,
        # dhcpv6_lease_file_name=None,
        lease_id_format=None,
        limit_addrs_per_ia=None,
        # local_port=None,
        # local_address=None,
        # local_address6=None,
        # bind_local_address6=None,
        # log_facility=None,
        log_threshold_high=None,
        log_threshold_low=None,
        max_lease_time=None,
        min_lease_time=None,
        min_secs=None,
        next_server=None,
        # omapi_port=None,
        one_lease_per_client=None,
        # persist_eui_64_leases=None,
        # pid_file_name=None,
        # dhcpv6_pid_file_name=None,
        ping_check=None,
        ping_cltt_secs=None,
        ping_timeout=None,
        ping_timeout_ms=None,
        preferred_lifetime=None,
        prefix_length_mode=None,
        # release_on_roam=None,
        # remote_port=None,
        server_identifier=None,
        # server_id_check=None,
        server_name=None,
        dhcpv6_set_tee_times=None,
        site_option_space=None,
        stash_agent_options=None,
        # update_conflict_detection=None,
        update_optimization=None,
        update_static_leases=None,
        # use_eui_64=None,
        use_host_decl_names=None,
        use_lease_addr_for_default_route=None,
        vendor_option_space=None,

    ) -> object:
        # self.abandon_lease_time = abandon_lease_time
        self.adaptive_lease_time_threshold = adaptive_lease_time_threshold
        # self.always_broadcast = always_broadcast
        self.always_reply_rfc1048 = always_reply_rfc1048
        # self.authoritative = authoritative
        self.boot_unknown_clients = boot_unknown_clients
        self.check_secs_byte_order = check_secs_byte_order
        # self.db_time_format = db_time_format
        self.ddns_hostname = ddns_hostname
        self.ddns_domainname = ddns_domainname
        # self.ddns_dual_stack_mixed_mode = ddns_dual_stack_mixed_mode
        # self.ddns_guard_id_must_match = ddns_guard_id_must_match
        self.ddns_local_address4 = ddns_local_address4
        self.ddns_local_address6 = ddns_local_address6
        # self.ddns_other_guard_is_dynamic = ddns_other_guard_is_dynamic
        self.ddns_rev_domainname = ddns_rev_domainname
        self.ddns_update_style = ddns_update_style
        self.ddns_updates = ddns_updates
        self.default_lease_time = default_lease_time
        self.delayed_ack = delayed_ack
        self.max_ack_delay = max_ack_delay
        self.dhcp_cache_threshold = dhcp_cache_threshold
        self.do_forward_updates = do_forward_updates
        self.dont_use_fsync = dont_use_fsync
        self.dynamic_bootp_lease_cutoff = dynamic_bootp_lease_cutoff
        self.dynamic_bootp_lease_length = dynamic_bootp_lease_length
        self.echo_client_id = echo_client_id
        self.filename = filename
        self.fixed_address = fixed_address
        self.fixed_address6 = fixed_address6
        self.fixed_prefix6 = fixed_prefix6
        self.get_lease_hostnames = get_lease_hostnames
        self.hardware_type = hardware_type
        self.hardware_address = hardware_address
        self.ignore_client_uids = ignore_client_uids
        self.infinite_is_reserved = infinite_is_reserved
        # self.lease_file_name = lease_file_name
        # self.dhcpv6_lease_file_name = dhcpv6_lease_file_name
        self.lease_id_format = lease_id_format
        self.limit_addrs_per_ia = limit_addrs_per_ia
        # self.local_port = local_port
        # self.local_address = local_address
        # self.local_address6 = local_address6
        # self.bind_local_address6 = bind_local_address6
        # self.log_facility = log_facility
        self.log_threshold_high = log_threshold_high
        self.log_threshold_low = log_threshold_low
        self.max_lease_time = max_lease_time
        self.min_lease_time = min_lease_time
        self.min_secs = min_secs
        self.next_server = next_server
        # self.omapi_port = omapi_port
        self.one_lease_per_client = one_lease_per_client
        # self.persist_eui_64_leases = persist_eui_64_leases
        # self.pid_file_name = pid_file_name
        # self.dhcpv6_pid_file_name = dhcpv6_pid_file_name
        self.ping_check = ping_check
        self.ping_cltt_secs = ping_cltt_secs
        self.ping_timeout = ping_timeout
        self.ping_timeout_ms = ping_timeout_ms
        self.preferred_lifetime = preferred_lifetime
        self.prefix_length_mode = prefix_length_mode
        # self.release_on_roam = release_on_roam
        # self.remote_port = remote_port
        self.server_identifier = server_identifier
        # self.server_id_check = server_id_check
        self.server_name = server_name
        self.dhcpv6_set_tee_times = dhcpv6_set_tee_times
        self.site_option_space = site_option_space
        self.stash_agent_options = stash_agent_options
        # self.update_conflict_detection = update_conflict_detection
        self.update_optimization = update_optimization
        self.update_static_leases = update_static_leases
        # self.use_eui_64 = use_eui_64
        self.use_host_decl_names = use_host_decl_names
        self.use_lease_addr_for_default_route = use_lease_addr_for_default_route
        self.vendor_option_space = vendor_option_space