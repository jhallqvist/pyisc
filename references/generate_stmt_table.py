output_file = 'test.md'

files = ['dhcpd-parameters.conf']

concatenated_string = None

for file in files:
    with open(file, 'r') as input_file:
        isc_conf = input_file.read()
    concatenated_string = '\n'.join(filter(None, (concatenated_string, isc_conf)))

isc_list = concatenated_string.splitlines()

reference_head = '''# DHCPd statements

| Original statement | Key | Value | Optional parameter |
| :----------------- | :-- | :---- | :----------------- |
'''


def generate_table(input_list: list) -> str:
    return_string = ''
    for line in input_list:
        line = line.replace('|', '\\|').replace(' ;', ';')
        if line.startswith('server-duid'):
            key, value, optional = line.split(None, 2)
        elif 'authoritative' in line:
            key, value, optional = [line] + [None, None]
        elif any(['hardware' in line, 'host-identifier' in line]):
            key, value, optional = line.rsplit(None, 1) + [None]
        else:
            key, value, optional = line.split(None, 1) + [None]
        return_string += f'|{line}|{key}|{value}|{optional}|\n'
    return return_string


def generate_final():
    return reference_head + generate_table(isc_list)


with open(output_file, 'w') as output:
    output.write(generate_final())
