
from collections import OrderedDict


od = OrderedDict([
	('a',123),
	('b',777)
	])


regd = dict(
	{'a':111,
	'b':222}
	)

for i,(k,v) in enumerate(od.items()):
	print(i,k,v)
print(180*'*')

for k,v in regd.items():
	print(k,v)