
# Create an object
object = subsets_colex_iterator(7,3)

# Create an iterable from the object
iterator = iter(object)

# Use the iterator in a for loop
for dum in iterator:
    print(dum)

# Try to call next() (this will fail!)
try:
    print(next(iterator))
except StopIteration:
    print('Game over!')
