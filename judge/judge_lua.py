import json
import re
import sys

cmds = """
date.lua
file_io.lua
max_min.lua
random.lua
remove.lua
round_num.lua
sin30.lua
sort.lua
strings.lua
"""

serial_out = sys.stdin.read()
result = {}
pattern = re.compile(r"testcase (.+) (\bsuccess\b|\bfail\b)")
results = pattern.findall(serial_out)
results = {x[0].strip(): x[1] == 'success' for x in results}

for line in cmds.split('\n'):
    line = line.strip()
    if not line:
        continue
    if f"lua {line}" not in results.keys():
        results[f"lua {line}"] = False

results = [{
    "name": k,
    "pass": 1 if v else 0,
    "all": 1,
    "score": 1 if v else 0,
}
    for k, v in results.items()
]

print(json.dumps(results))