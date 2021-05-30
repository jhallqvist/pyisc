# Used to generate a target table for the different parsed files.
import pathlib
import inspect
from pyisc import dhcpd

file_array = [
    'data/dhcpd_ref-conf.conf',
    'data/dhcpd_ref-options.conf'
]
parser = dhcpd.parsing.DhcpdParser()

for file in file_array:
    reference_file = pathlib.Path(file)
    with reference_file.open() as infile:
        conf = infile.read()
        table_file = reference_file.with_suffix('.md')
    test = conf.splitlines()
    reference_head = inspect.cleandoc('''# DHCPd statements

    | Original statement | Key | Value | Optional/Parameter |
    | :----------------- | :-- | :---- | :----------------- |
    ''') + '\n'
    with table_file.open("w") as f:
        f.write(reference_head)
    for row in test:
        if not row.startswith('#'):
            node = parser.build_tree(row).children[0]
            joined_str = "|".join(
                [str(x) for x in [node.type, node.value, node.parameters]])
            final_string = "|" + "|".join((row, joined_str)) + "|" + '\n'
            with table_file.open("a") as f:
                f.write(final_string)
