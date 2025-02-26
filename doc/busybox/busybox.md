# Busybox测试样例

## 题目描述

BusyBox 是一个提供多种 Unix 工具的轻量级软件包，它将常见的 Unix 工具（如 `ls`、`cp`、`mv`、`sh`、`cat` 等）合并到一个可执行文件中。它旨在为嵌入式系统或资源受限环境提供简洁、高效的替代方案。通过这种方式，BusyBox 在占用少量存储空间的同时，能够提供丰富的功能，特别适合嵌入式设备、Linux 系统的救援模式或容器化环境中使用。对于轻量级内核来说，支持 busybox 就可以拥有了一个简单的交互终端功能。



本测试用例会将编译好的 busybox 文件作为输入的可执行文件，并为其传递一系列的参数，从而执行一系列功能，判断待测内核对 busybox 功能的支持情况。



## 编译方法

- 源码地址：https://github.com/oscomp/testsuits-for-oskernel/tree/pre-2025/busybox
- 编译 busybox 方式：参考 https://github.com/oscomp/testsuits-for-oskernel/tree/pre-2025 下的 README.md 对完整测例进行编译，在项目根目录下生成的 sdcard 目录下，会找到 busybox 目录，其即为编译生成的测例。
- 单独编译：请修改 [编译目标](https://github.com/oscomp/testsuits-for-oskernel/blob/pre-2025/Makefile.sub#L14) ，仅保留 busybox 目标。之后按照 README 操作进行，即可单独编译 busybox 测例到 sdcard 目录下。



## 样例输出


测试 busybox musl 版本的输出可能如下所示：
```
#### OS COMP TEST GROUP START busybox-musl ####
#### independent command test
testcase busybox echo "#### independent command test" success
testcase busybox ash -c exit success
testcase busybox sh -c exit success
bbb
testcase busybox basename /aaa/bbb success
   February 2025
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28
                     
testcase busybox cal success

。。。
testcase busybox echo "ccccccc" >> test.txt success
testcase busybox echo "bbbbbbb" >> test.txt success
testcase busybox echo "aaaaaaa" >> test.txt success
testcase busybox echo "2222222" >> test.txt success
testcase busybox echo "1111111" >> test.txt success
testcase busybox echo "bbbbbbb" >> test.txt success
testcase busybox sort test.txt | ./busybox uniq success
  File: test.txt
  Size: 60        	Blocks: 8          IO Block: 4096   regular file
Device: 10304h/66308d	Inode: 101061027   Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1010/     zyj)   Gid: ( 1010/     zyj)
Access: 2025-02-26 15:30:12.000000000
Modify: 2025-02-26 15:30:12.000000000
Change: 2025-02-26 15:30:12.000000000

testcase busybox stat test.txt success
hello world
ccccccc
bbbbbbb
aaaaaaa
2222222
1111111
bbbbbbb
testcase busybox strings test.txt success
        7         8        60 test.txt
testcase busybox wc test.txt success
testcase busybox [ -f test.txt ] success
hello world
ccccccc
bbbbbbb
aaaaaaa
2222222
1111111
bbbbbbb
testcase busybox more test.txt success
testcase busybox rm test.txt success
testcase busybox mkdir test_dir success
testcase busybox mv test_dir test success
testcase busybox rmdir test success
echo "hello world" > test.txt
grep hello busybox_cmd.txt
testcase busybox grep hello busybox_cmd.txt success
testcase busybox cp busybox_cmd.txt busybox_cmd.bak success
testcase busybox rm busybox_cmd.bak success
./busybox_cmd.txt
testcase busybox find -name "busybox_cmd.txt" success
#### OS COMP TEST GROUP END busybox-musl ####
```

用户可以将sdcard 中的 busybox_testcode.sh 文件中提到的 `./busybox` 字段修改为`busybox`字段，使用本机自带的 busybox 程序执行 `busybox sh busybox_testcode.sh`，也可得到如上输出。

观察 `busybox_testcode.sh`可以了解到，上述输出是`busybox_cmd.txt`中每一条指令的执行结果。待测脚本读取了 `busybox_cmd.txt` 的每一行，执行 `eval ./busybox $line` ，将这条指令进行执行，并依照返回值进行判断。

- 假设原有的语句中不包含 `false` 字段，则认为这条指令是一条应当成功执行的语句。此时若返回值不为 0 ，则认为执行失败，则这条指令不得分，输出`testbase xx fail`
- 其他情况下均认为得分。如`rm busybox_cmd.bak`是其中的一条指令，若输出了`testcase busybox rm busybox_cmd.bak success`说明该指令得分。

```shell
#!/busybox sh

./busybox echo "#### OS COMP TEST GROUP START busybox-glibc ####"
# RST=result.txt
# if [ -f $RST ];then
# 	rm $RST
# fi
# touch $RST

# echo "If the CMD runs incorrectly, return value will put in $RST" > $RST
# echo -e "Else nothing will put in $RST\n" >> $RST
# echo "TEST START" >> $RST

./busybox cat ./busybox_cmd.txt | while read line
do
	eval "./busybox $line"
	RTN=$?
	if [[ $RTN -ne 0 && $line != "false" ]] ;then
		echo "testcase busybox $line fail"
		# echo "return: $RTN, cmd: $line" >> $RST
	else
		echo "testcase busybox $line success"
	fi
done

# echo "TEST END" >> $RST
./busybox echo "#### OS COMP TEST GROUP END busybox-glibc ####"
```

## 评分依据

每一条指令占一分，若输出了`testbase xx success`（xx为指令内容）则得一分，否则不得分。