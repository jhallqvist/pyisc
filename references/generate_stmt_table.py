"""TEMP."""
from pyisc import utils

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

output_file = 'dhcpd-reference.md'

files = [
    'dhcpd-allow_deny.conf',
    'dhcpd-classes.conf',
    'dhcpd-declarations.conf',
    'dhcpd-dns.conf',
    'dhcpd-failover.conf',
    'dhcpd-parameters.conf']

concatenated_string = None

for file in files:
    with open(file, 'r') as input_file:
        isc_conf = input_file.read()
    concatenated_string = '\n'.join(
        filter(None, (concatenated_string, isc_conf)))

isc_list = concatenated_string.splitlines()

reference_head = '''# DHCPd statements

| Original statement | Key | Value | Optional/Parameter |
| :----------------- | :-- | :---- | :----------------- |
'''


def generate_table(input_list: list) -> str:
    return_string = ''
    bool_keys = ('authoritative', 'not authoritative', 'primary', 'secondary',
                'group', 'pool')  # Primary currently not working for DNS Conf
    optional_last_parameter = ('failover')
    split_on_first = ('allow', 'deny', 'ignore', 'match', 'spawn', 'range',
                     'db-time-format', 'fixed-address', 'fixed-prefix6')
    split_on_last = ('hardware', 'host-identifier', 'load', 'lease', 'peer',
                    'my state', 'peer state')
    split_on_second = ('option')
    split_two_first = ('server-duid', 'subnet ')
    for line in input_list:
        original_line = line
        if line.endswith(';'):
            line = line.replace('|', '\\|').replace(';', '').strip()
            if line.startswith(split_two_first):
                line_split = line.split(None, 2)
            elif line.startswith(bool_keys):
                line_split = [line]
            elif line.startswith(split_on_second):
                line_split = utils.nth_split(line, ' ', 2)
            elif line.startswith(split_on_first):
                line_split = line.split(None, 1)
            elif line.startswith(optional_last_parameter):
                line_split = utils.split_from(line, ' ', 2)
            elif line.startswith(split_on_last):
                line_split = line.rsplit(None, 1)
            else:
                line_split = line.split()
        elif line.endswith('{'):
            line = line.replace(' {', '').strip()
            if line.startswith(split_two_first):
                line_split = line.split(None, 2)
            elif line.startswith(optional_last_parameter):
                line_split = utils.split_from(line, ' ', 2)
            elif line.startswith(bool_keys):
                line_split = [line]
            else:
                line_split = line.split()
        else:
            # print(f'{line}: NOT PROCESSED')
            continue
        while 4 > len(line_split):
            line_split.append(None)
        key, value, optional, *_ = line_split
        return_string += f'|{original_line.strip()}|{key}|{value}|{optional}|\n'
    return return_string


def generate_final():
    return reference_head + generate_table(isc_list)


with open(output_file, 'w') as output:
    output.write(generate_final())
