import json
import collections

def tree():
	return collections.defaultdict(tree)

colours = tree()
colours['other']['black'] = 0x000000
colours['other']['white'] = 0xFFFFFF
colours['primary']['red'] = 0xFF0000

print(json.dumps(colours, sort_keys=True, indent=4))
