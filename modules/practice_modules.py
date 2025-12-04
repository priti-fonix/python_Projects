import json
import math

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y.keys())

# bytes data (UTF-8 encoded JSON)
data_bytes = b'{ "name": "Alice", "age": 25, "city": "Paris" }'

# decode bytes → string → parse JSON
json_str = data_bytes.decode("utf-8")
res = json.loads(json_str)

print(res)
print(res["name"])

# create bytearray from a JSON string
data_bytearray = bytearray(b'{ "brand": "Ford", "model": "Mustang" }')

# convert bytearray → bytes → string → dict
json_str = data_bytearray.decode("utf-8")
result = json.loads(json_str)

print(result)

person = {"name": "Bob", "age": 40}

# convert dict → JSON string → bytes
data_str= json.dumps(person) #-------    to string   -----------
data_bytes  = data_str.encode("utf-8")  #-------    to bytes  -----------
print(data_str)  
print(type(data_str))
print("--------- bytes -------------------")
print(data_bytes)  
print(type(data_bytes))
print("---------any datatype to -------------------")
print("-------------  json  --------------")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print(math.sqrt(6))