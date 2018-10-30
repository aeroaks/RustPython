1 + 2

a = 1
b = 2
c = 3
assert a < b
assert not b < a
assert a <= b
assert a <= c

assert b > a
assert not a > b
assert not a > c
assert b >= a
assert c >= a
assert not a >= b