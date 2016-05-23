#!/usr/bin/env python
# coding: UTF-8

import config
import os
from apps.main import main_app
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import xlrd


# 默认主页
@main_app.route("/main")
def main():
    name = "my"
    return render_template("main.html", name=name)


# 导入xls
@main_app.route('/import_xls')
def import_xls():
    return render_template("import.html")


# 接受文件检测
def allowed_file(filename):
    return '.' in filename \
        and filename.rsplit('.', 1)[1] in config.UPLOAD_EXTENSIONS


def resolve_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(3)
    print(u"t{0} \t {1}\n".format(table.nrows, table.ncols))
    print(u"{0}".format(table.row_values(1)))
    return table.row_values(1)


@main_app.route("/upfile", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = u"{0}".format(file.filename)
            # filename = secure_filename(file_name)
            file_path = os.path.join(config.UPLOAD_FOLDER, filename)
            file.save(file_path)
            # return resolve_xls(file_path)
            return redirect(url_for('main_app.xls_value', filename=filename))
    return 'erro!'


@main_app.route("/xls_value/<filename>")
def xls_value(filename):
    file_path = os.path.join(config.UPLOAD_FOLDER, filename)
    return render_template("xls_value.html", xls_value=resolve_xls(file_path))
