# Basic基本测试样例

## 题目描述

这里给出的测试题目会通过系统调用访问内核实现组开发的OS，得到正确可靠的服务。系统调用基于部分比较基础的Linux syscalls。

测试用例代码可见[syscalls测试用例](https://github.com/oscomp/testsuits-for-oskernel/tree/pre-2025/basic)。从测试用例可以看出，自己开发的OS只需实现Linux syscalls的功能子集即可。

具体的Syscall说明可见[syscalls说明](oscomp_syscalls.md)。

## 编译方法

请参考[赛题仓库](https://github.com/oscomp/testsuits-for-oskernel/tree/pre-2025)中的basic目录和Makefile.sub中的basic目标。

## 样例输出

一次运行正确的输出可能如下所示：
```
#### OS COMP TEST GROUP START basic-musl ####
========== START test_brk ==========
Before alloc,heap pos: 0
After alloc,heap pos: 64
Alloc again,heap pos: 128
========== END test_brk ==========
========== START test_chdir ==========
chdir ret: 0
  current working dir : /test_chdir/
========== END test_chdir ==========
#### OS COMP TEST GROUP END basic-musl ####
```

首先由basic_testcode.sh输出`#### OS COMP TEST GROUP START basic-musl ####`，随后运行了brk和chdir两个测试程序，最后再由basic_testcode.sh输出对应的`#### OS COMP TEST GROUP END basic-musl ####`。

在brk测试点中，进行了两次分配内存操作，每次分配64字节，分别打印出了分配前和两次分配后的堆指针位置。在chdir测试点中，首先调用mkdir创建了/test_chdir目录，并使用chdir进入，检查了chdir调用的返回值为0，最后使用getpwd调用验证当前位置是否在/test_chidr中。

## 评分依据

brk样例成功运行得1分，第一次brk分配结束堆指针在正确位置得1分，第二次分配结束堆指针在正确位置得1分，因此上述输出共得3分。
chdir样例成功运行得1分，chdir调用返回值为0得1分，使用getpwd验证当前目录在/test_chdir中得1分，因此上述输出共得3分。

其余所有测试点的详细评分依据可参考[评分脚本](../../judge/judge_basic.py)