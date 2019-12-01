import csv

csv_file = 'VROMISSILES.csv'
xml_data_final = ''
csv_data = csv.DictReader(open(csv_file), fieldnames=['name', 'macro', 'tags', 'info', 'race', 'damage', 'reload', 'amount', 'barrel', 'dps', 'alpha', 'lifetime', 'thrust', 'speed', 'travel', 'firerange', 'guided', 'retarget', 'swarm', 'locktime', 'lockrange', 'hull', 'weapon', 'resiliense', 'mass', 'inertia', 'dforward', 'dhv', 'dman', 'explosioneffect', 'launcheffect', 'engine', 'component', 'price', 'cells', 'mcs', 'sc', 'prodtime', 'tname', 'tbasename', 'tdescription'])

row_n = 0
for row in csv_data:
    if row_n == 0:
        print('row' + str(row_n) + ' is not printing')
        row_n += 1
    else:
        xml_data = '<t id="%s">%s</t>\n<t id="%s">%s</t>\n<t id="%s">%s</t>\n' % (row['tname'], row['name'], row['tbasename'], row['name'], row['tdescription'], row['name'])
        xml_data_final += xml_data
        print(xml_data)
        row_n += 1

print(xml_data_final)
xml_file = 'tfile_generated.xml'
F = open(xml_file, 'w')
F.write(xml_data_final)
F.close
