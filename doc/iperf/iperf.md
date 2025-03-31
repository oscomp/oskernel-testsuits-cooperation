## 测试题目说明

### 1. 题目描述

`iperf3` 是一个用于测量 TCP、UDP 和 SCTP 网络带宽的工具。它支持各种参数的调节，如时序、协议和缓冲区设置，并能够报告网络吞吐量、数据丢失等性能指标。本题将要求学生编译并使用 `iperf3` 工具进行网络带宽的测试，理解其如何配置和使用，以及如何通过命令行选项来调整性能参数。

### 2. 编译方法

要编译 `iperf3`，首先确保系统上没有任何先决条件要求。然后，按照以下步骤进行：

```bash
# 获取源代码并进入目录
git clone https://github.com/esnet/iperf.git
cd iperf

# 运行配置脚本、编译并安装
./configure
make
sudo make install
```

如果在运行 `./configure` 时遇到问题，可以尝试先运行 `./bootstrap.sh` 来重新生成配置文件。

### 3. 样例输出

运行 `iperf3` 的命令行示例如下：

```bash
# 启动服务器端（通常在一台机器上运行）
iperf3 -s

# 启动客户端进行带宽测试（另一台机器上运行）
iperf3 -c <server_ip_address> -t 60 -i 10
```

**输出示例：**

```
Connecting to host 192.168.1.1, port 5201
[  5] local 192.168.1.2 port 54321 connected to 192.168.1.1 port 5201
[ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
[  5]   0.0-10.0 sec   1.23 GBytes   1.05 Gbits/sec   0   1.02 MBytes
[  5]  10.0-20.0 sec   1.21 GBytes   1.04 Gbits/sec   0   1.02 MBytes
```

### 4. 评分依据

评分将根据以下几个方面进行：

- **正确性**：程序是否能够成功编译并执行。
- **理解度**：是否能正确使用 `iperf3` 测量网络带宽，配置命令行选项进行带宽测试。
- **性能测试**：是否能使用 `iperf3` 测试不同的网络带宽配置，并理解其报告结果。
- **命令行选项使用**：是否能够利用 `iperf3` 的高级功能（如 `-Z` 选项启用零拷贝，或 `-A` 设置 CPU 亲和性）进行优化测试。

