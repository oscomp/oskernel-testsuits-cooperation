# cyclictest 测试用例

## 题目描述

cyclictest 是 rt-tests 中的一个高精度测试程序，通过测量任务被唤醒的延迟时间来测试内核的实时性。

本测例还会用到同属于 rt-tests 的 hackbench 程序，和 cyclictest 同时运行来进行压力测试。

### [测试脚本](https://github.com/oscomp/testsuits-for-oskernel/blob/pre-2025/scripts/cyclictest/cyclictest_testcode.sh)

```sh
./busybox echo "#### OS COMP TEST GROUP START cyclictest ####"

run_cyclictest() {
    echo "====== cyclictest $1 begin ======"
    ./cyclictest $2
    if [ $? == 0 ]; then
	    ans="success"
    else
	    ans="fail"
    fi
  echo "====== cyclictest $1 end: $ans ======"
}

run_cyclictest NO_STRESS_P1 "-a -i 1000 -t1  -p99 -D 1s -q"
run_cyclictest NO_STRESS_P8 "-a -i 1000 -t8  -p99 -D 1s -q"

echo "====== start hackbench ======"
./hackbench -l 100000000 &
hackbench_pid=$!

sleep 1

run_cyclictest STRESS_P1 "-a -i 1000 -t1  -p99 -D 1s -q"
run_cyclictest STRESS_P8 "-a -i 1000 -t8  -p99 -D 1s -q"

# Kill children in the parent process's interrupt processing, 
# so SIGINT is used instead of SIGKILL
kill -2 $hackbench_pid
if [ $? == 0 ]; then
    ans="success"
else
    ans="fail, ignore STRESS result"
fi
sleep 1
echo "====== kill hackbench: $ans ======"


./busybox echo "#### OS COMP TEST GROUP END cyclictest ####"
```

运行参数说明：
- `-a` 绑定测试线程到所有 CPU。
- `-i 1000` 设置基准间隔为 1000 微秒
- `-t1`/`-t8` 运行 1/8 个测试线程
- `-p99` 设置线程优先级为 99
- `-D 1s` 指定测试时长为 1s
- `-q` 安静模式，只在退出时输出摘要信息

## 编译方法

请参考[赛题仓库](https://github.com/oscomp/testsuits-for-oskernel/tree/pre-2025)中的 `rt-tests-2.7` 目录和 `Makefile.sub` 中的 `cyclictest` 目标。

## 样例输出

```
#### OS COMP TEST GROUP START cyclictest ####
====== cyclictest NO_STRESS_P1 begin ======
# /dev/cpu_dma_latency set to 0us
T: 0 (11312) P:99 I:1000 C:   1000 Min:      1 Act:    1 Avg:    1 Max:       8
====== cyclictest NO_STRESS_P1 end: success ======
====== cyclictest NO_STRESS_P8 begin ======
# /dev/cpu_dma_latency set to 0us
T: 0 (11315) P:99 I:1000 C:   1000 Min:      1 Act:    1 Avg:    1 Max:       8
T: 1 (11316) P:99 I:1500 C:    667 Min:      1 Act:    1 Avg:    1 Max:       1
T: 2 (11317) P:99 I:2000 C:    500 Min:      1 Act:    1 Avg:    1 Max:       2
T: 3 (11318) P:99 I:2500 C:    400 Min:      1 Act:    1 Avg:    1 Max:       3
T: 4 (11319) P:99 I:3000 C:    334 Min:      1 Act:    1 Avg:    1 Max:      49
T: 5 (11320) P:99 I:3500 C:    286 Min:      1 Act:    1 Avg:    1 Max:       2
T: 6 (11321) P:99 I:4000 C:    250 Min:      1 Act:    1 Avg:    1 Max:       2
T: 7 (11322) P:99 I:4500 C:    223 Min:      1 Act:    1 Avg:    1 Max:       2
====== cyclictest NO_STRESS_P8 end: success ======
====== start hackbench ======
Running in process mode with 10 groups using 40 file descriptors each (== 400 tasks)
Each sender will pass 100000000 messages of 100 bytes
====== cyclictest STRESS_P1 begin ======
# /dev/cpu_dma_latency set to 0us
T: 0 (11726) P:99 I:1000 C:   1000 Min:      2 Act:    2 Avg:    2 Max:      14
====== cyclictest STRESS_P1 end: success ======
====== cyclictest STRESS_P8 begin ======
# /dev/cpu_dma_latency set to 0us
T: 0 (11729) P:99 I:1000 C:   1000 Min:      1 Act:    2 Avg:    2 Max:      23
T: 1 (11730) P:99 I:1500 C:    667 Min:      1 Act:    2 Avg:    2 Max:       7
T: 2 (11731) P:99 I:2000 C:    500 Min:      1 Act:    2 Avg:    2 Max:       9
T: 3 (11732) P:99 I:2500 C:    400 Min:      2 Act:    2 Avg:    2 Max:       5
T: 4 (11733) P:99 I:3000 C:    334 Min:      1 Act:    2 Avg:    2 Max:       6
T: 5 (11734) P:99 I:3500 C:    286 Min:      1 Act:    2 Avg:    2 Max:      16
T: 6 (11735) P:99 I:4000 C:    250 Min:      2 Act:    3 Avg:    2 Max:       9
T: 7 (11736) P:99 I:4500 C:    223 Min:      1 Act:    2 Avg:    2 Max:       7
====== cyclictest STRESS_P8 end: success ======
Signal 2 caught, longjmp'ing out!
longjmp'ed out, reaping children
sending SIGTERM to all child processes
signaling 400 worker threads to terminate
SENDER: write (error: Connection reset by peer)
SENDER: write (error: Connection reset by peer)
SENDER: write (error: Connection reset by peer)
SENDER: write (error: Broken pipe)
SENDER: write (error: Broken pipe)
SENDER: write (error: Connection reset by peer)
Time: 3.102
====== kill hackbench: success ======
#### OS COMP TEST GROUP END cyclictest ####
```

与 BusyBox 测例类似地，可以通过修改测试脚本中的程序路径，在本机上执行此脚本得到以上输出，不过需要注意运行 `cyclictest` 需要 root 权限或加入 `realtime` 用户组。

## 评分依据

成功运行一次 cyclictest 应当输出形如 `cyclictest * end: success` 的内容，一共应当有 `NO_STRESS_P1` `NO_STRESS_P8` `STRESS_P1` `STRESS_P8` 四次输出。且如果没有输出 `kill hackbench: success`，对应 `STRESS_P1` `STRESS_P8` 的两个结果将会被舍弃。

根据 cyclictest 的输出，对内核的实时性也做一定的评分。
