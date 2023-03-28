import subprocess
import sys
import os

proj_dir = os.path.abspath('.')
print("当前项目工作目录",proj_dir)

print("安装pip包管理器")
subprocess.call([sys.executable,'-m','ensurepip'])
print("升级pip包管理器")
subprocess.call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip']) 
print("安装科学计算包")
subprocess.call([sys.executable, '-m', 'pip', 'install', '-r', "{}/requirements.txt".format(proj_dir), '--user'])

print('环境安装完成')
