import builtins
import collections

key = 'list'
mappings = collections.ChainMap(globals(), locals(), vars(builtins))
value = mappings[key]
print(value)
