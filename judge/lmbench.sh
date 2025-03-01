#!/bin/bash

if ! command -v lmbench_all &> /dev/null; then
    lmbench_all=""
    have_lmbench=""
else
    have_lmbench="yes"
fi


run_test() {
    local test_name=$1

    if [ -z "$have_lmbench" ]; then
	local command="./$2"
	result=$($command 2>&1 | tail -n 1)
    else
	local command=$2
	result=$($command 2>&1 | tail -n 1)
    fi
    number=$(echo "$result" | grep -oP '\d+\.\d+')

    if [[ "$2" == *lat_fs* ]]; then
	# Assuming the output is stored in a variable or command result
	output="10k 581 105675 191452"
    
	# Extract the two numbers (105675 and 191452)
	num1=$(echo $result | awk '{print $3}')
	num2=$(echo $result | awk '{print $4}')
    
	# Perform the addition
	number=$((num1 + num2))
    fi

    if [[ "$2" == *lat_mmap* || "$2" == *bw_file_rd*
	|| "$2" == *bw_mmap_rd* ]]; then
	number=$(echo "$result" | awk '{print $1}')
    fi
    if [ -z "$number" ]; then
	number=$(echo "$result" | awk '{print $1}')
    fi
    echo "$test_name:$number"
}


run_test "1:syscall null latency (micro second)" "lat_syscall -P 1 null"
run_test "2:syscall read latency (micro second)" "lat_syscall -P 1 read"
run_test "3:syscall write latency (micro second)" "lat_syscall -P 1 write"
run_test "4:syscall stat latency (micro second)" "lat_syscall -P 1 stat"
run_test "5:syscall fstat latency (micro second)" "lat_syscall -P 1 fstat"
run_test "6:syscall open latency (micro second)" "lat_syscall -P 1 open"
run_test "7:select latency (micro second)" "lat_select -n 100 -P 1 file"
run_test "8:sig install latency (micro second)" "lat_sig -P 1 install"
run_test "9:sig catch latency (micro second)" "lat_sig -P 1 catch"
run_test "10:sig prot latency (micro second)" "lat_sig -P 1 prot lat_sig"
run_test "11:pipe latency (micro second)" "lat_pipe -P 1"
run_test "12:proc fork latency (micro second)" "lat_proc -P 1 fork"
run_test "13:proc exec latency (micro second)" "lat_proc -P 1 exec"
run_test "14:proc shell latency (micro second)" "lat_proc -P 1 shell"
run_test "15:fs write bandwidth (KB/sec)" "lmdd of=/var/tmp/XXX move=1m fsync=1 print=3"
run_test "16:pagefault latency (micro second)" "lat_pagefault -P 1 /var/tmp/XXX"
run_test "17:mmap latency (micro second)" "lat_mmap -P 1 512k /var/tmp/XXX"
run_test "18:pipe bandwidth (KB/sec)" "bw_pipe -P 1"
run_test "19:file system latency (creations+deletes per second)" "lat_fs /var/tmp"
run_test "20:512k file read ioonly (megabytes per second)" "bw_file_rd -P 1 512k io_only /var/tmp/XXX"
run_test "21:512k file read open2close (megabytes per second)" "bw_file_rd -P 1 512k open2close /var/tmp/XXX"
run_test "22:512k mmap read mmaponly (megabytes per second)" "bw_mmap_rd -P 1 512k mmap_only /var/tmp/XXX"
run_test "23:512k mmap read mmaponly (megabytes per second)" "bw_mmap_rd -P 1 512k open2close /var/tmp/XXX"
run_test "24:context switch latency (micro second when there are 96 processes)" "lat_ctx -P 1 -s 32 2 4 8 16 24 32 64 96" 
