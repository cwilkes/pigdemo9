@outputSchema("word:chararray")
def helloworld():  
  return 'Hello, World'
@outputSchema("word:chararray,num:long")
def complex(word):
  return str(word),len(word)

@outputSchemaFunction("squareSchema")
def square(num):
  return ((num)*(num))

@schemaFunction("squareSchema")
def squareSchema(input):
  return input

# No decorator - bytearray
def concat(str):
  return str+str

@outputSchema("y:bag{t:tuple(initial, followup)}")
def find_followup_queries(bag):
	outBag = []
	if len(bag) < 2:
		return outBag
	prev_link = None
	try:
		prev_link = bag[0][3]
	except:
		print >>sys.stderr, "Error with", bag
		return outBag
	for session in bag[1:]:
		outBag.append( (prev_link, session[3]) )
		prev_link = session[3]
	return outBag

@outputSchema("t:tuple(initial, followup)")
def find_followup_queries2(bag):
	if len(bag) < 2:
		return 
	prev_link = None
	try:
		prev_link = bag[0][3]
	except:
		print >>sys.stderr, "Error with", bag
		return
	for session in bag[1:]:
		yield ( prev_link, session[3] )
		prev_link = session[3]
