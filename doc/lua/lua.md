# Lua 测试用例

## 题目描述

Lua 是一种轻量级的、快速的脚本语言，常用于嵌入式编程和扩展应用程序。它的设计目标是简单、灵活并且易于嵌入其他应用程序中。本测试用例会将编译好的 lua 解释器作为输入的可执行文件，并且传入一系列的 lua 脚本文件，要求你运行这些脚本文件并输出结果，判断待测内核是否支持 lua 脚本的解释执行。


## 编译方法

- 源码地址：https://github.com/oscomp/testsuits-for-oskernel/tree/pre-2025/lua
- 编译 lua 方式：参考 https://github.com/oscomp/testsuits-for-oskernel/tree/pre-2025 下的 README.md 对完整测例进行编译，在项目根目录下生成的 sdcard 目录下，会找到 lua 目录，其即为编译生成的测例。
- 单独编译：请修改 [编译目标](https://github.com/oscomp/testsuits-for-oskernel/blob/pre-2025/Makefile.sub#L14) ，仅保留 lua 目标。之后按照 README 操作进行，即可单独编译 lua 测例到 sdcard 目录下。



## 样例输出

测试 lua musl 的输出可能如下所示：
```
#### OS COMP TEST GROUP START lua-musl ####
testcase lua date.lua success
testcase lua file_io.lua success
testcase lua max_min.lua success
testcase lua random.lua success
testcase lua remove.lua success
testcase lua round_num.lua success
testcase lua sin30.lua success
testcase lua sort.lua success
testcase lua strings.lua success
#### OS COMP TEST GROUP END lua-musl ####
```

`lua_testcode.sh` 指定了测试所用到的各种 lua 脚本文件。`lua_testcode.sh` 将脚本文件作为参数传递给 `test.sh`，`test.sh` 会将脚本文件作为输入传递给 lua 解释器，并判断执行结束之后的返回值是否为 0。若为 0，则输出 `success`，否则输出 `fail`。


## 评分依据

参考[评分脚本](../../judge/judge_lua.py)可知，每一个测试用例占 1 分。当输出了 `success` 时，得 1 分；否则得 0 分。