import json
import re
import sys

cmds = """
echo "#### independent command test"
ash -c exit
sh -c exit
basename /aaa/bbb
cal
clear
date
df
dirname /aaa/bbb
dmesg
du
expr 1 + 1
false
true
which ls
uname
uptime
ps
pwd
free
hwclock
kill 10
ls
sleep 1
echo "#### file opration test"
touch test.txt
echo "hello world" > test.txt
cat test.txt
cut -c 3 test.txt
od test.txt
head test.txt
tail test.txt
hexdump -C test.txt
md5sum test.txt
echo "ccccccc" >> test.txt
echo "bbbbbbb" >> test.txt
echo "aaaaaaa" >> test.txt
echo "2222222" >> test.txt
echo "1111111" >> test.txt
echo "bbbbbbb" >> test.txt
sort test.txt | ./busybox uniq
stat test.txt
strings test.txt
wc test.txt
[ -f test.txt ]
more test.txt
rm test.txt
mkdir test_dir
mv test_dir test
rmdir test
grep hello busybox_cmd.txt
cp busybox_cmd.txt busybox_cmd.bak
rm busybox_cmd.bak
find -name "busybox_cmd.txt"
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
    if f"busybox {line}" not in results.keys():
        results[f"busybox {line}"] = False

results = [{
    "name": k,
    "pass": 1 if v else 0,
    "all": 1,
    "score": 1 if v else 0,
}
    for k, v in results.items()
]

print(json.dumps(results))