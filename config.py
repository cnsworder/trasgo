#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cnsworder<cnsworder@gmail.com>

SERVER_PORT = 80  # 服务端口号
IS_DEBUG = True   # 是否调试

SHEET_INDEX = 1
UPLOAD_EXTENSIONS = {'xls', 'png'}  # 支持上传文件类型
UPLOAD_FOLDER = '/Users/crossorbit/desktop'  # 上传文件目录
PHOTO_FOLDER = '/Users/crossorbit/desktop'  # 照片目录
DB_URL = "sqlite:///data/transgo.db"


class xls_index:
    clienter = 0
    time = 3
    ID = 4
    addr = 5
    tick = 7
    user = 8
    tel = 9
    count = 10
    express = 16
    descript = 18
    print_status = 19
    cancel_status = 6
