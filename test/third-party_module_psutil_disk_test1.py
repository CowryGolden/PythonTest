#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用第三方模块-psutil：psutil模块获取磁盘信息
    # 使用场景：
        使用psutil模块的disk_*相关方法获取磁盘分区、磁盘使用率和磁盘IO信息：

'''
# 使用psutil模块的disk_*相关方法获取磁盘分区、磁盘使用率和磁盘IO信息：
import psutil

print('psutil.disk_partitions() =', psutil.disk_partitions())    # 获取磁盘分区信息

print('psutil.disk_usage(\'/\') =', psutil.disk_usage('/'))    # 获取磁盘使用情况

print('psutil.disk_io_counters() =', psutil.disk_io_counters())    # 磁盘IO

r'''
    #注：输出结果为：
            psutil.disk_partitions() = [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='F:\\', mountpoint='F:\\', fstype='NTFS', opts='rw,fixed')]
            psutil.disk_usage('/') = sdiskusage(total=429497774080, used=10628845568, free=418868928512, percent=2.5)
            psutil.disk_io_counters() = sdiskio(read_count=505233, write_count=1085165, read_bytes=27819159552, write_bytes=26528036864, read_time=3099, write_time=5181)    
        可以看到，磁盘'/'的总容量是429497774080 = 400 GB（当前文件所在分区的根目录），使用了2.5%。文件格式是NTFS，opts中包含rw表示可读写，journaled表示支持日志。    

'''