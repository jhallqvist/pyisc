"""TEMP."""
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from pyisc import utils

output_file = 'dhcpd-reference.md'

"""
files = [
    'dhcpd-allow_deny.conf',
    'dhcpd-classes.conf',
    'dhcpd-declarations.conf',
    'dhcpd-dns.conf',
    'dhcpd-failover.conf',
    'dhcpd-parameters.conf']
"""
files = ['dhcpd-dns.conf']

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
    """TEMP."""
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
            # Bool split and default split can be the same. I.e. remove bool split thinking
            line = line.replace('|', '\\|').replace(';', '').strip()
            if line.startswith(split_two_first):
                line_split = line.split(None, 2)
            # elif line.startswith(bool_keys):
            elif any(x == line for x in bool_keys):
                line_split = line.split()
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
            line = line.replace('{', '').strip()
            if line.startswith(split_two_first):
                line_split = line.split(None, 2)
            elif line.startswith(optional_last_parameter):
                line_split = utils.split_from(line, ' ', 2)
            elif any(x == line for x in bool_keys):
                line_split = [line]
            else:
                line_split = line.split()
        else:
            print(f'{line}: NOT PROCESSED')
            continue
        while 4 > len(line_split):
            line_split.append(None)
        key, value, optional, *_ = line_split
        return_string += f'|{original_line.strip()}|{key}|{value}|{optional}|\n'
    return return_string


def generate_final():
    """TEMP."""
    return reference_head + generate_table(isc_list)


with open(output_file, 'w') as output:
    output.write(generate_final())

"""
parameter needs X patterns -    split on only the second space - nth_split,
                                split on the first space - split(None, 1),
                                split on the first two spaces - split(None, 2),
                                split on last space - rsplit(None, 1)
parameter_option, parameter_general, parameter_multi_value, paramater_multi_key
parameter_option regex: 
    (?:option\s)[\w]+\s*?[^\n]*?;
split_first:
    (?:(?:allow|deny|ignore|match|spawn|range|fixed-address|fixed-prefix6)\s)[\w]+\s*?[^\n]*?;
split_first_two:
    (?:server-duid )[\w]+\s*?[^\n]*?;
split_on_last:
    (?:(?:hardware|host-identifier|load|lease|peer|my state|peer state)\s)[\w]+\s*?[^\n]*?;
parameter_general regex: (?:[\w\/:"-]+\s?)+?;   OR   [\w]+\s*?[^\n]*?;
section needs two regex patterns -  one for failover and one for all others 
                                    that splits on the first two occurences of 
                                    space
                                    failover: (?:failover\s)[\w]+\s*?[^\n]*?{
                                    general: [\w]+\s*?[^\n]*?{
"""