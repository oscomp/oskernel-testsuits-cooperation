
## 题目描述

libc-bench 是一个用于测试和比较不同 C/POSIX 标准库函数实现的时间和内存效率的测试工具集。它由 Eta Labs 开发，主要用于评估标准库函数（如 malloc、字符串操作、线程创建等）的性能。
主要功能:
- 内存分配性能测试：测量 malloc 在不同线程竞争条件下的吞吐量和开销，以及释放内存返回给操作系统的效率。
- 字符串和正则表达式搜索：测试标准库中字符串操作和正则表达式匹配的性能。
- 线程创建和销毁性能：评估线程创建和销毁的吞吐量。
- UTF-8 解码性能：测试 UTF-8 编码的解码效率。
- 标准 I/O 测试：测量标准输入输出缓冲读写性能。


## 编译方法

- 源码地址：https://github.com/oscomp/testsuits-for-oskernel/tree/pre-2025/busybox
- 编译 libcbench 方式：参考 https://github.com/oscomp/testsuits-for-oskernel/tree/pre-2025 下的 README.md 对完整测例进行编译，在项目根目录下生成的 sdcard 目录下，会找到 busybox 目录，其即为编译生成的测例。
- 单独编译：请修改 [编译目标](https://github.com/oscomp/testsuits-for-oskernel/blob/pre-2025/Makefile.sub#L14) ，仅保留 libcbench 目标。之后按照 README 操作进行，即可单独编译 busybox 测例到 sdcard 目录下。

## 样例输出

```shell
b_malloc_sparse (0)
  time: 0.044845625, virt: 39376, res: 0, dirty: 0

b_malloc_bubble (0)
  time: 0.035995583, virt: 39376, res: 0, dirty: 0

b_malloc_tiny1 (0)
  time: 0.007387947, virt: 628, res: 0, dirty: 0

b_malloc_tiny2 (0)
  time: 0.004802770, virt: 628, res: 0, dirty: 0

b_malloc_big1 (0)
  time: 0.010567392, virt: 80080, res: 0, dirty: 0

b_malloc_big2 (0)
  time: 0.007766442, virt: 80080, res: 0, dirty: 0

b_malloc_thread_stress (0)
  time: 0.091500541, virt: 72, res: 0, dirty: 0

b_malloc_thread_local (0)
  time: 0.087201559, virt: 84, res: 0, dirty: 0

b_string_strstr ("abcdefghijklmnopqrstuvwxyz")
  time: 0.018217474, virt: 0, res: 0, dirty: 0

b_string_strstr ("azbycxdwevfugthsirjqkplomn")
  time: 0.025178139, virt: 0, res: 0, dirty: 0

b_string_strstr ("aaaaaaaaaaaaaacccccccccccc")
  time: 0.017301663, virt: 0, res: 0, dirty: 0

b_string_strstr ("aaaaaaaaaaaaaaaaaaaaaaaaac")
  time: 0.017933191, virt: 0, res: 0, dirty: 0

b_string_strstr ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac")
  time: 0.020625649, virt: 0, res: 0, dirty: 0

b_string_memset (0)
  time: 0.008373490, virt: 0, res: 0, dirty: 0

b_string_strchr (0)
  time: 0.019126830, virt: 0, res: 0, dirty: 0

b_string_strlen (0)
  time: 0.015457260, virt: 0, res: 0, dirty: 0

b_pthread_createjoin_serial1 (0)
  time: 1.021888869, virt: 0, res: 0, dirty: 0

b_pthread_createjoin_serial2 (0)
  time: 0.971511952, virt: 0, res: 0, dirty: 0

b_pthread_create_serial1 (0)
  time: 0.937488568, virt: 50000, res: 0, dirty: 0

b_pthread_uselesslock (0)
  time: 0.109982275, virt: 0, res: 0, dirty: 0

b_utf8_bigbuf (0)
  time: 0.048280698, virt: 0, res: 0, dirty: 0

b_utf8_onebyone (0)
  time: 0.183226514, virt: 0, res: 0, dirty: 0

b_stdio_putcgetc (0)
  time: 0.369177917, virt: 4, res: 0, dirty: 0

b_stdio_putcgetc_unlocked (0)
  time: 0.368543852, virt: 4, res: 0, dirty: 0

b_regex_compile ("(a|b|c)*d*b")
  time: 0.085520989, virt: 20, res: 0, dirty: 0

b_regex_search ("(a|b|c)*d*b")
  time: 0.097498578, virt: 20, res: 0, dirty: 0

b_regex_search ("a{25}b")
  time: 0.296807894, virt: 20, res: 0, dirty: 0
```

## 评分依据

- time: 执行时间。执行时间越短，表示性能越好。
- virt: 虚拟内存占用情况。通常，较低的内存占用表示更好的内存管理效率
- res: 常驻内存占用情况。通常，较低的内存占用表示更好的内存管理效率
- dirty: 脏页数量。较低的脏页数量通常意味着更少的磁盘 I/O 操作，从而提高性能。



