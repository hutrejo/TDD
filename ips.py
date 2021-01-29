import re
import itertools
import sys

with open('sh_run.txt') as f:
	lines= tuple(f)
	for i, line in enumerate(lines):
		if "interface G" in line:
			print(lines[i])
			print(lines[i+1])
