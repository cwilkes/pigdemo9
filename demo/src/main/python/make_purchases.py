from avro import schema, datafile, io
import sys

SCHEMA_STR="""{
	  "type": "record", 
	    "name": "Purchase",
		  "namespace": "org.seattlehadoop.pigdemo9.avro",
		    "fields": [
{"name": "itemName", "type": "string"}, 
{"name": "quantity", "type": { "type": "array", "items": "int"} }
]
}"""

SCHEMA = schema.parse(SCHEMA_STR)

def avro_writer(file_name):
	rec_writer = io.DatumWriter(SCHEMA)
	df_writer = datafile.DataFileWriter(
    	open(file_name, 'wb'),
		rec_writer,
		writers_schema = SCHEMA,
		codec = 'deflate'
	)
	return df_writer


def create_record(name, quantity):
	rec1 = {}
	rec1['itemName'] = name
	rec1['quantity'] = []
	for q in quantity:
		rec1['quantity'].append(q)
	return rec1


def create_items(file_name):
	writer = avro_writer(file_name)
	writer.append(create_record('car', [ 10, 11, 12 ]))
	writer.append(create_record('house', [ 20 ]))
	writer.close()


def main(args):
	create_items(args[0])


if __name__ == '__main__':
	main(sys.argv[1:])
