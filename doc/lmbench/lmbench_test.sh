#!/bin/bash

if ! command -v lmbench_all &> /dev/null; then
    echo "lmbench_all 命令未找到"
    lmbench_all=""
    have_lmbench=""
else
    echo "lmbench_all 命令已找到，开始执行测试。"
    have_lmbench="yes"
fi
# 比较实际结果与预期结果的函数，返回得分
compare_results() {
    local test_name=$1     # 测试名称
    local actual_result=$2  # 实际结果
    local expected_result=$3 # 预期结果
    local max_score=$4      # 该测试的满分

    # 如果没有获取到实际结果，返回0分
    if [ -z "$actual_result" ]; then
        echo "0"
        return 0
    fi

    # 如果实际结果包含预期结果，则认为通过，给满分
    if [[ "$actual_result" == *"$expected_result"* ]]; then
        echo $max_score
        return $max_score  # 返回满分
    else
        # 如果实际结果不包含预期结果，得分为0
	echo "0"
        return 0
    fi
}

# 初始化总分
total_score=0

# 定义每个测试的权重（总和应该为100）
declare -A test_weights=(
    ["lat_syscall_null"]=5
    ["lat_syscall_read"]=5
    ["lat_syscall_write"]=5
    ["lat_syscall_stat"]=5
    ["lat_syscall_fstat"]=5
    ["lat_syscall_open"]=5
    ["lat_select"]=5
    ["lat_sig_install"]=5
    ["lat_sig_catch"]=5
    ["lat_sig_prot"]=5
    ["lat_pipe"]=5
    ["lat_proc_fork"]=5
    ["lat_proc_exec"]=5
    ["lat_proc_shell"]=5
    ["lat_fs"]=5
    ["write_bandwidth"]=5
    ["lat_pagefault"]=5
    ["lat_mmap"]=5
    ["bw_file_rd"]=2
    ["lat_ctx"]=1
    ["bw_pipe"]=2
    ["bw_mmap_rd"]=1
)

# 运行并比较每个测试的结果
# 测试1：syscall（null）延迟, 测试空系统调用
echo "测试1：syscall（null）延迟"
if [ -z "$have_lmbench" ]; then
    result=$(./lat_syscall -P 1 null 2>&1)
else
    result=$(lmbench_all ./lat_syscall -P 1 null 2>&1)
fi

expected_result="Simple syscall"
score=$(compare_results "lat_syscall null" "$result" "$expected_result" ${test_weights["lat_syscall_null"]})
total_score=$((total_score + score))
echo "测试1：syscall（null）得分 $score"
echo $total_score

# 测试2：syscall（read）延迟，测试读系统调用
echo "测试2：syscall（read）延迟"
if [ -z "$have_lmbench" ]; then
    result=$(./lat_syscall -P 1 read  2>&1)
else
    result=$(lmbench_all lat_syscall -P 1 read  2>&1)
fi

expected_result="Simple read"
score=$(compare_results "lat_syscall read" "$result" "$expected_result" ${test_weights["lat_syscall_read"]})
total_score=$((total_score + score))
echo "测试2：syscall（read）得分 $score"
echo $total_score

# 测试3：syscall（write）延迟，测试写系统调用
if [ -z "$have_lmbench" ]; then
    result=$(./lat_syscall -P 1 write  2>&1)
else
    result=$(lmbench_all lat_syscall -P 1 write  2>&1)
fi

expected_result="Simple write"
score=$(compare_results "lat_syscall write" "$result" "$expected_result" ${test_weights["lat_syscall_write"]})
total_score=$((total_score + score))
echo "测试3：syscall（wrie）得分 $score"
echo $total_score

busybox touch /var/tmp/lmbench

# 测试4：文件stat延迟，测试stat系统调用
if [ -z "$have_lmbench" ]; then
    result=$(./lat_syscall -P 1 stat /var/tmp/lmbench 2>&1)
else
    result=$(lmbench_all lat_syscall -P 1 stat /var/tmp/lmbench  2>&1)
fi

expected_result="Simple stat"
score=$(compare_results "lat_syscall stat" "$result" "$expected_result" ${test_weights["lat_syscall_stat"]})
total_score=$((total_score + score))
echo "测试4：syscall（stat）得分 $score"
echo $total_score


# 测试5：文件fstat延迟，测试stat系统调用
if [ -z "$have_lmbench" ]; then
    result=$(./lat_syscall -P 1 fstat /var/tmp/lmbench 2>&1)
else
    result=$(lmbench_all lat_syscall -P 1 fstat /var/tmp/lmbench  2>&1)
fi

expected_result="Simple fstat"
score=$(compare_results "lat_syscall fstat" "$result" "$expected_result" ${test_weights["lat_syscall_fstat"]})
total_score=$((total_score + score))
echo "测试5：syscall（fstat）得分 $score"
echo $total_score


# 测试6：文件打开延迟，测试open系统调用
if [ -z "$have_lmbench" ]; then
    result=$(./lat_syscall -P 1 open /var/tmp/lmbench 2>&1)
else
    result=$(lmbench_all lat_syscall -P 1 open /var/tmp/lmbench  2>&1)
fi

expected_result="Simple open"
score=$(compare_results "lat_syscall open" "$result" "$expected_result" ${test_weights["lat_syscall_open"]})
total_score=$((total_score + score))
echo "测试6：syscall（open）得分 $score"
echo $total_score

# 测试7：select延迟，测试select系统调用
if [ -z "$have_lmbench" ]; then
    result=$(./lat_select -n 100 -P 1 file 2>&1)
else
    result=$(lmbench_all lat_select -n 100 -P 1 file  2>&1)
fi

expected_result="Select on"
score=$(compare_results "lat_select" "$result" "$expected_result" ${test_weights["lat_select"]})
total_score=$((total_score + score))
echo "测试7：syscall（select）得分 $score"
echo $total_score


# 测试8：信号安装延迟，测试信号安装系统调用
if [ -z "$have_lmbench" ]; then
    result=$(./lat_sig -P 1 install 2>&1)
else
    result=$(lmbench_all lat_sig -P 1 install  2>&1)
fi


expected_result="Signal handler installation"
score=$(compare_results "lat_sig install" "$result" "$expected_result" ${test_weights["lat_sig_install"]})
total_score=$((total_score + score))
echo "测试8：sig install得分 $score"
echo $total_score


# 测试9：信号捕获延迟，测试信号捕获
if [ -z "$have_lmbench" ]; then
    result=$(./lat_sig -P 1 catch 2>&1)
else
    result=$(lmbench_all lat_sig -P 1 install  2>&1)
fi

expected_result="Signal handler overhead"
score=$(compare_results "lat_sig catch" "$result" "$expected_result" ${test_weights["lat_sig_catch"]})
total_score=$((total_score + score))
echo "测试9：sig catch得分 $score"
echo $total_score

# 测试10：信号保护延迟，测试信号保护
if [ -z "$have_lmbench" ]; then
    result=$(./lat_sig -P 1 prot lat_sig 2>&1)
else
    result=$(lmbench_all lat_sig -P 1 prot lat_sig 2>&1)
fi

expected_result="Protection fault"
score=$(compare_results "lat_sig prot" "$result" "$expected_result" ${test_weights["lat_sig_prot"]})
total_score=$((total_score + score))
echo "测试10：sig prot得分 $score"
echo $total_score


# 测试11：管道延迟，测试管道实现
if [ -z "$have_lmbench" ]; then
    result=$(./lat_pipe -P 1 2>&1)
else
    result=$(lmbench_all lat_pipe -P 1 2>&1)
fi

expected_result="Pipe latency"
score=$(compare_results "lat_pipe" "$result" "$expected_result" ${test_weights["lat_pipe"]})
total_score=$((total_score + score))
echo "测试11：lat_pipe得分 $score"
echo $total_score


# 测试12：fork延迟，测试fork实现
if [ -z "$have_lmbench" ]; then
    result=$(./lat_proc -P 1 fork 2>&1)
else
    result=$(lmbench_all lat_proc -P 1 fork 2>&1)
fi

expected_result="Process fork+exit"
score=$(compare_results "lat_proc fork" "$result" "$expected_result" ${test_weights["lat_proc_fork"]})
total_score=$((total_score + score))
echo "测试12：fork得分 $score"
echo $total_score


# 测试13：exec延迟，测试exec实现
if [ -z "$have_lmbench" ]; then
    result=$(./lat_proc -P 1 exec 2>&1)
else
    result=$(lmbench_all lat_proc -P 1 exec 2>&1)
fi

expected_result="Process fork+execve"
score=$(compare_results "lat_proc exec" "$result" "$expected_result" ${test_weights["lat_proc_exec"]})
total_score=$((total_score + score))
echo "测试13：exec得分 $score"
echo $total_score


# 测试14：shell延迟
if [ -z "$have_lmbench" ]; then
    result=$(./lat_proc -P 1 shell 2>&1)
else
    result=$(lmbench_all lat_proc -P 1 shell 2>&1)
fi


expected_result="Process fork+/bin/sh"
score=$(compare_results "lat_proc shell" "$result" "$expected_result" ${test_weights["lat_proc_shell"]})
total_score=$((total_score + score))
echo "测试14：shell得分 $score"
echo $total_score


# 测试15：文件写带宽，测试文件写实现
if [ -z "$have_lmbench" ]; then
    result=$(./lmdd label="File /var/tmp/XXX write bandwidth:" of=/var/tmp/XXX move=1m fsync=1 print=3 2>&1)
else
    result=$(lmbench_all lmdd label="File /var/tmp/XXX write bandwidth:" of=/var/tmp/XXX move=1m fsync=1 print=3 2>&1)
fi


expected_result="File /var/tmp/XXX write bandwidth"
score=$(compare_results "write bandwidth" "$result" "$expected_result" ${test_weights["write_bandwidth"]})
total_score=$((total_score + score))
echo "测试15：write bandwidth得分 $score"
echo $total_score

# 测试16：页面错误延迟，测试页面错误处理能力
if [ -z "$have_lmbench" ]; then
    result=$(./lat_pagefault -P 1 /var/tmp/XXX 2>&1)
else
    result=$(lmbench_all lat_pagefault -P 1 /var/tmp/XXX 2>&1)
fi

expected_result="Pagefaults on /var/tmp/XXX"
score=$(compare_results "lat_pagefault" "$result" "$expected_result" ${test_weights["lat_pagefault"]})
total_score=$((total_score + score))
echo "测试16：lat_pagefault得分 $score"
echo $total_score


# 测试17：mmap延迟，测试mmap实现
if [ -z "$have_lmbench" ]; then
    result=$(./lat_mmap -P 1 512k /var/tmp/XXX 2>&1)
else
    result=$(lmbench_all lat_mmap -P 1 512k /var/tmp/XXX 2>&1)
fi


expected_result="." 
score=$(compare_results "lat_mmap" "$result" "$expected_result" ${test_weights["lat_mmap"]})
total_score=$((total_score + score))
echo "测试17：lat_mmap得分 $score"
echo $total_score


# 测试18：管道带宽，测试管道带宽
if [ -z "$have_lmbench" ]; then
    result=$(./bw_pipe -P 1 2>&1)
else
    result=$(lmbench_all bw_pipe -P 1 2>&1)
fi

expected_result="Pipe"
score=$(compare_results "bw_pipe" "$result" "$expected_result" ${test_weights["bw_pipe"]})
total_score=$((total_score + score))
echo "测试18：bw_pipe得分 $score"


# 测试19：文件系统延迟，测试文件系统延迟
if [ -z "$have_lmbench" ]; then
    result=$(./lat_fs /var/tmp 2>&1)
else
    result=$(lmbench_all lat_fs /var/tmp 2>&1)
fi

expected_result="0k"
score=$(compare_results "lat_fs" "$result" "$expected_result" ${test_weights["lat_fs"]})
total_score=$((total_score + score))
echo "测试19：lat_fs得分 $score"

# 测试20：文件读带宽，测试文件读
if [ -z "$have_lmbench" ]; then
    result=$(./bw_file_rd -P 1 512k io_only /var/tmp/XXX 2>&1)
else
    result=$(lmbench_all bw_file_rd -P 1 512k io_only /var/tmp/XXX 2>&1)
fi


expected_result="."  # Any bandwidth values can follow
score=$(compare_results "bw_file_rd" "$result" "$expected_result" ${test_weights["bw_file_rd"]})
total_score=$((total_score + score))
echo "测试20：bw_file_rd io_only 得分 $score"



# 测试21：文件读带宽（open2close）
if [ -z "$have_lmbench" ]; then
    result=$(./bw_file_rd -P 1 512k open2close /var/tmp/XXX 2>&1)
else
    result=$(lmbench_all bw_file_rd -P 1 512k open2close /var/tmp/XXX 2>&1)
fi


expected_result="."
score=$(compare_results "bw_file_rd" "$result" "$expected_result" ${test_weights["bw_file_rd"]})
total_score=$((total_score + score))
echo "测试21：bw_file_rd open2close 得分 $score"
echo "总得分: $total_score"


# 测试22：内存映射读取带宽（mmap_only）
if [ -z "$have_lmbench" ]; then
    result=$(./bw_mmap_rd -P 1 512k mmap_only /var/tmp/XXX 2>&1)
else
    result=$(lmbench_all bw_mmap_rd -P 1 512k mmap_only /var/tmp/XXX 2>&1)
fi

expected_result="."
score=$(compare_results "bw_mmap_rd" "$result" "$expected_result" ${test_weights["bw_mmap_rd"]})
total_score=$((total_score + score))
echo "测试22：bw_mmap_rd mmap_only 得分 $score"
echo "总得分: $total_score"


# 测试23：内存映射读取带宽（open2close）
if [ -z "$have_lmbench" ]; then
    result=$(./bw_mmap_rd -P 1 512k open2close /var/tmp/XXX 2>&1)
else
    result=$(lmbench_all bw_mmap_rd -P 1 512k open2close /var/tmp/XXX 2>&1)
fi

expected_result="."
score=$(compare_results "bw_file_rd" "$result" "$expected_result" ${test_weights["bw_file_rd"]})
total_score=$((total_score + score))
echo "测试23：bw_mmap_rd open2close 得分 $score"



# 测试24：上下文切换延迟（lat_ctx）
if [ -z "$have_lmbench" ]; then
    result=$(./lat_ctx -P 1 -s 32 2 4 8 16 24 32 64 96 2>&1)
else
    result=$(lmbench_all lat_ctx -P 1 -s 32 2 4 8 16 24 32 64 96 2>&1)
fi

expected_result="size=32k"
score=$(compare_results "lat_ctx" "$result" "$expected_result" ${test_weights["lat_ctx"]})
total_score=$((total_score + score))
echo "测试24：lat_ctx 得分 $score"
echo "总得分: $total_score"


