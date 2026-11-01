import platform
import os

print("Hello Fedora Linux!")
print("当前系统用户:", os.getlogin())
print("系统内核版本:", platform.release())