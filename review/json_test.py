
import json
dictionary={
	'name':'fairy',
	'situation':'wowo'
}

string = json.dumps(dictionary)

print(string)

print(json.loads(string))
