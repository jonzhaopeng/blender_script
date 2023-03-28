import subprocess
import sys
import os
PYTHONVERSION="python3.10"
PIPLIST="scipy numpy pandas sympy"

pythonbin = os.path.join(sys.prefix, 'bin', PYTHONVERSION)
print("升级pip包管理器")
subprocess.call([pythonbin, '-m', 'pip', 'install', '--upgrade', 'pip']) 
print("安装科学计算包")
subprocess.call([pythonbin, '-m', 'pip', 'install', '--upgrade', PIPLIST, '--user'])

print('环境安装完成')
