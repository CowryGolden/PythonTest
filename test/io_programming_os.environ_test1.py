#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-操作文件和目录：os模块的使用；os.environ的使用
    # 使用场景：
        如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
        如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
        我们来看看如何使用os模块的基本功能：
        在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
'''
# 使用os模块的os.environ

import os

print('os.environ :')
print('----------------')
print(os.environ)


'''
    #注：执行结果
os.environ :
----------------
environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Golden Cowry\\AppData\\Roaming', 'AWE_DIR': 'D:\\Program Files\\Khrona LLC\\Awesomium SDK\\1.6.6\\', 'CLASSPATH': '.;D:\\ProgramFiles\\Java\\jdk1.8.0_131\\lib;D:\\ProgramFiles\\Java\\jdk1.8.0_131\\lib\\tools.jar', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-EGNQ5KJ', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Golden Cowry', 'JAVA_HOME': 'D:\\ProgramFiles\\Java\\jdk1.8.0_131', 'LANG': 'en_US.UTF-8', 'LOCALAPPDATA': 'C:\\Users\\Golden Cowry\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-EGNQ5KJ', 'MAVEN_HOME': 'E:\\MavenProject\\plug-in\\maven3.5.2', 'MYSQL_HOME': 'D:\\ProgramFiles\\mysql-5.7.16', 'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\Users\\Golden Cowry\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'D:\\ProgramFiles\\Python364\\Scripts\\;D:\\ProgramFiles\\Python364\\;D:\\ProgramFiles\\Java\\jdk1.8.0_131\\bin;D:\\ProgramFiles\\Java\\jdk1.8.0_131\\jre\\bin;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;D:\\ProgramFiles\\mysql-5.7.16\\bin;D:\\Program Files\\Git\\cmd;D:\\Program Files\\VanDyke Software\\Clients\\;E:\\MavenProject\\plug-in\\maven3.5.2\\bin;D:\\ProgramFiles\\Anaconda3;D:\\ProgramFiles\\Anaconda3\\Scripts;C:\\Users\\Golden Cowry\\AppData\\Local\\GitHubDesktop\\bin;C:\\Program Files\\Microsoft VS Code\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW;.CPL', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 60 Stepping 3, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '3c03', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Users\\Golden Cowry\\Documents\\WindowsPowerShell\\Modules;C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'PUBLIC': 'C:\\Users\\Public', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\GOLDEN~1\\AppData\\Local\\Temp', 'TERM_PROGRAM': 'vscode', 'TERM_PROGRAM_VERSION': '1.21.1', 'TMP': 'C:\\Users\\GOLDEN~1\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-EGNQ5KJ', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-EGNQ5KJ', 'USERNAME': 'Golden Cowry', 'USERPROFILE': 'C:\\Users\\Golden Cowry', 'VSCODE_CWD': 'C:\\Program Files\\Microsoft VS Code', 'VSCODE_IPC_HOOK': '\\\\.\\pipe\\05b0d990d279357716580f9c24c44b90-1.21.1-main-sock', 'VSCODE_NLS_CONFIG': '{"locale":"zh-cn","availableLanguages":{"*":"zh-cn"}}', 'VSCODE_NODE_CACHED_DATA_DIR_26276': 'C:\\Users\\Golden Cowry\\AppData\\Roaming\\Code\\CachedData\\79b44aa704ce542d8ca4a3cc44cfca566e7720f1', 'VSCODE_PID': '26276', 'WINDIR': 'C:\\Windows'})

'''