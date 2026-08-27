import hashmap

provinces = hashmap.new()
# Dutch provinces; key is province name, value is its largest city
hashmap.set(provinces, 'North Holland', 'Amsterdam')
hashmap.set(provinces, 'South Holland', 'Rotterdam')
hashmap.set(provinces, 'Utrecht', 'Utrecht')
hashmap.set(provinces, 'Zeeland', 'Middelburg')
hashmap.set(provinces, 'Groningen', 'Groningen')
hashmap.set(provinces, 'Limburg', 'Maastricht')
hashmap.set(provinces, 'Flevoland', 'Almere')
hashmap.set(provinces, 'North Brabant', 'Den Bosch')
hashmap.set(provinces, 'Friesland', 'Leeuwarden')
hashmap.set(provinces, 'Drenthe', 'Assen')
hashmap.set(provinces, 'Gelderland', 'Nijmegen')
hashmap.set(provinces, 'Overijssel', 'Enschede')

hashmap.list(provinces)
print '-' * 10
print hashmap.get(provinces, 'Drenthe')