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
        ware_name = 'missile_' + row['name']
        print(ware_name)
        price_min_f = int(row['price']) - int(row['price'])*0.15
        price_min = int(price_min_f)
        price_max_f = int(row['price']) + int(row['price'])*0.15
        price_max = int(price_max_f)
        tname = '{6699, ' + row['tname'] + '}'
        tbasename = '{6699, ' + row['tbasename'] + '}'
        tdescription = '{6699, ' + row['tdescription'] + '}'

        xml_data = '<ware id="%s" name="%s" description="%s" group="missiles" transport="equipment" volume="1" tags="equipment missile">\n<price min="%s" average="%s" max="%s" />\n<production time="%s" amount="1" method="default" name="{20206,101}">\n<primary>\n<ware ware="energycells" amount="%s" />\n<ware ware="missilecomponents" amount="%s" />]\n<ware ware="smartchips" amount="%s" />\n</primary>\n</production>\n<component ref="%s" amount="1" />\n<container ref="sm_gen_pickup_equipment_01_macro" />\n<use threshold="0"/>\n' % (ware_name, tname, tdescription, price_min, row['price'], price_max, row['prodtime'], row['cells'], row['mcs'], row['sc'], row['macro'])
        if row['race'] == '0':
            xml_data = xml_data + '</ware>\n\n'
            xml_data_final += xml_data
            row_n += 1
        elif row['race'] == 'argon':
            xml_data = xml_data + '<owner faction="antigone"/>\n<owner faction="argon"/>\n</ware>\n\n'
            xml_data_final += xml_data
            row_n += 1
        elif row['race'] == 'paranid':
            xml_data = xml_data + '<owner faction="holyorder"/>\n<owner faction="paranid"/>\n</ware>\n\n'
            xml_data_final += xml_data
            row_n += 1
        elif row['race'] == 'teladi':
            xml_data = xml_data + '<owner faction="teladi"/>\n<owner faction="ministry"/>\n</ware>\n\n'
            xml_data_final += xml_data
            row_n += 1

print(xml_data_final)
xml_file = 'generated_wares.xml'
F = open(xml_file, 'w')
F.write(xml_data_final)
F.close
