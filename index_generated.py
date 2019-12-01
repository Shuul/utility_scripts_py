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
        xml_data = '<entry name="%s" value="extensions\VRO\\assets\props\WeaponSystems\missile\macros\%s"/>\n' % (row['macro'], row['macro'])
        xml_data_final += xml_data
        row_n += 1

print(xml_data_final)
xml_file = 'index_wares.xml'
F = open(xml_file, 'w')
F.write(xml_data_final)
F.close
