#!/usr/bin/env python
# -*- coding: utf-8 -*-
# upx压缩会导致莫名的程序运行失败

from PyInstaller.__main__ import run

if __name__ == '__main__':
    # opts = ['TargetOpinionMain.py', '-F']
    # opts = ['TargetOpinionMain.py', '-F', '-w']
    opts = ['main.py', '-D', '-w']
    run(opts)