
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



def test(a,b):
    """

    >>> test(4,3)
    7

    >>> test(10,2)
    122

    """

    return a + b

if __name__ == '__main__':
    test(4,3)