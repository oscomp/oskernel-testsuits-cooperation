### UnixBench 测试样例说明

---

#### **题目描述**

UnixBench 测试集用于评估操作系统的综合性能，涵盖 CPU 运算、内存管理、进程调度、文件系统等核心功能。测试程序通过系统调用与内核交互，验证 OS 的正确性和效率。每个测试点对应不同场景，需确保系统调用实现完整且性能达标。

---

#### **测试用例代码**

以下是文档中出现的所有测试用例代码文件及其核心功能描述：

| 文件名             | 测试目标             | 关键指标                | 关键系统调用                                               |
| ------------------ | -------------------- | ----------------------- | ---------------------------------------------------------- |
| `arith.c`        | 算术运算速度         | 运算次数/秒 (lps)       | 无（纯CPU计算）                                            |
| `dhry_1/2.c`     | 整数运算性能         | Dhrystone MIPS          | `malloc`, `execv`                                      |
| `pipe.c`         | 进程间通信吞吐量     | 管道操作次数/秒 (lps)   | `pipe`, `read`, `write`                              |
| `syscall.c`      | 系统调用延迟         | 系统调用次数/秒 (lps)   | `getpid`, `exec`, `close`, `dup`等多种基础系统调用 |
| `fstime.c`       | 文件系统I/O速度      | 读写吞吐量 (KBps)       | `creat`, `open`, `read`, `write`, `lseek`        |
| `hanoi.c`        | 递归性能             | 汉诺塔操作次数/秒 (lps) | 无（纯算法计算）                                           |
| `context1.c`     | 上下文切换开销       | 切换次数/秒 (lps)       | `fork`, `pipe`（通过读写同步切换）                     |
| `spawn.c`        | 进程创建效率         | 进程数/秒 (lps)         | `fork`, `wait`                                         |
| `whets.c`        | 浮点运算性能         | MFLOPS                  | 无（依赖数学库函数）                                       |
| `execl.c`        | 程序加载效率         | 加载次数/秒 (lps)       | `execl`, `fork`                                        |
| `time-polling.c` | 多路I/O复用效率      | 事件处理数/秒 (ops)     | `select`, `poll`                                       |
| `looper.c`       | 用户态任务调度公平性 | 循环完成次数/秒 (lps)   | 无（依赖用户态逻辑）                                       |

---

#### **编译方法**

参考 `Makefile` 配置，使用静态链接和优化选项编译：

```
# 编译器配置
CC = riscv64-linux-gcc -static
OPTON = -O3 -ffast-math
CFLAGS = -Wall -pedantic (OPTON) -I (OPTON)−I(SRCDIR) -DTIME
# 编译目标程序（示例：arithoh）(PROGDIR)/arithoh: (PROGDIR)/arithoh:(SRCDIR)/arith.c $(SRCDIR)/timeit.c
	(CC) -o (CC)−o@ (CFLAGS) (CFLAGS)<< $(LDFLAGS)
```

执行编译：

```
make -f Makefile.sub all
```

---

#### **样例输出**

一个可能的运行输出示例：

```
#### OS COMP TEST GROUP START unixbench ####
========== START test_arith ==========
COUNT|987654|1|lps
========== END test_arith ==========
========== START test_dhrystone ==========
Dhrystone Test: 10.0 MIPS
========== END test_dhrystone ==========
========== START test_pipe ==========
Pipe Throughput: 5000 ops/sec
========== END test_pipe ==========
========== START test_fstime ==========
File Read: 200 MB/s, Write: 150 MB/s
========== END test_fstime ==========
#### OS COMP TEST GROUP END unixbench ####
```

**解释** ：

* **`test_dhrystone`** 显示每秒 1000 万次 Dhrystone 操作（MIPS）。
* **`COUNT|987654|1|lps`**：表示在测试持续时间内完成了 987,654 次循环迭代（每秒循环数）。
* **`test_pipe`** 显示每秒处理 5000 次管道操作。
* **`test_fstime`** 显示文件读写速度。

---

#### **评分依据**

脚本中无评分依据，实现正确的情况下性能越高越好。
