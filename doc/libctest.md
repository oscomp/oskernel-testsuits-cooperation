# Libctest测试样例

## 题目描述

libc-test 是一个用于测试 C 标准库（libc）功能和兼容性的测试套件。C 标准库是 C 语言程序开发中不可或缺的一部分，它提供了诸如输入输出、内存管理、字符串处理等基本功能。libc-test 通过一系列精心设计的测试用例，对 C 标准库的各个功能模块进行全面而细致的测试，以确保其在不同环境下的正确性和稳定性。
本测试用例会将编译好的 libc-test 可执行文件作为输入，运行其中的各种测试用例，包括静态测试和动态测试。通过执行这些测试用例并检查输出结果，来判断待测内核是否能够正确支持 C 标准库的各项功能，从而验证内核与 C 标准库之间的兼容性和稳定性。



## 编译方法

- 源码地址：https://github.com/oscomp/testsuits-for-oskernel/tree/pre-2025/libc-test
- 编译 libctest 方式：参考 https://github.com/oscomp/testsuits-for-oskernel/tree/pre-2025 下的 README.md 对完整测例进行编译，在项目根目录下生成的 sdcard 目录下，会找到 libctest 目录，其即为编译生成的测例。
- 单独编译：请修改 [编译目标](https://github.com/oscomp/testsuits-for-oskernel/blob/pre-2025/Makefile.sub#L14) ，仅保留 libctest 目标。之后按照 README 操作进行，即可单独编译 libctest 测例到 sdcard 目录下。



## 样例输出


测试 libctest 的输出可能如下所示：
```
#### OS COMP TEST GROUP START libctest ####
========== START entry-static.exe argv ==========
Pass!
========== END entry-static.exe argv ==========
========== START entry-static.exe basename ==========
Pass!
========== END entry-static.exe basename ==========
···
#### OS COMP TEST GROUP END libctest ####
```

首先由libctest_testcode.sh输出`#### OS COMP TEST GROUP START libctest ####`，随后运行./run-static.sh以及./run-dynamic.sh脚本进行测试，脚本中执行`./runtest.exe -w entry-static.exe argv`等指令以运行如上例中的argv、basename等测例并输出`Pass!`，最后再由libctest_testcode.sh输出对应的`#### OS COMP TEST GROUP END libctest ####`。



## 评分依据

每一个测例占一分，若输出了`Pass!`则得一分，否则不得分。