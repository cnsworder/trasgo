#!/usr/bin/env python
# coding: UTF-8

import config
import os
import json
from datetime import datetime

from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

import xlrd

from apps.main import main_app
from apps.data.transgodatabase import Order
from apps.data.transgodatabase import make_session
from apps import logging

import config


# 默认主页
@main_app.route("/main")
def main():
    if 'user' not in session:
        return redirect(url_for("login"))
    return render_template("main_frame.html", user_name=session['user'])


# 导入xls
@main_app.route('/import_xls')
def import_xls():
    return render_template("import_frame.html")


# 接受文件检测
def allowed_file(filename):
    return '.' in filename \
        and filename.rsplit('.', 1)[1] in config.UPLOAD_EXTENSIONS


def import_to_db(table):
    xls_index = config.xls_index
    session = make_session()
    print(table.ncols)
    try:
        for index in range(1, table.nrows - 1):
            row = table.row_values(index)
            if not row[xls_index.ID]:
                continue

            order = Order(row[xls_index.ID],
                        row[xls_index.clienter],
                        row[xls_index.tick],
                        row[xls_index.user],
                        row[xls_index.addr],
                        row[xls_index.tel],
                        int(row[xls_index.count]),
                        row[xls_index.express],
                        datetime.strptime(row[xls_index.time],
                                            "%Y/%m/%d  %H:%M:%S"),
                        row[xls_index.descript],
                        row[xls_index.print_status],
                        True if row[xls_index.cancel_status] else False)
            session.add(order)

        session.commit()
    except Exception as e:
        session.rollback()
        print(e.message)
        logging.info("{0}".format(e.message))
        return False
    return True


def resolve_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(config.SHEET_INDEX)
    print(u"t{0} \t {1}\n".format(table.nrows, table.ncols))
    print(u"{0}".format(table.row_values(1)))
    import_to_db(table)
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
    return render_template("xls_frame.html", xls_value=resolve_xls(file_path))


@main_app.route("/importdb", methods=["POST"])
def import_db():
    return "import"


def search_order(search_value):
    aSession = make_session()
    orders = aSession.query().filter(order_id=search_value)
    return orders


PAGE_COUNT = 20


@main_app.route("/search_order/<order_id>")
def search_order_by_id(order_id):
    session = make_session()
    orders = session.query(Order)\
        .filter(Order.ID == order_id)\
        .order_by(Order.time)
    page_num = 2
    return render_template("order_query_frame.html",
                           orders=orders,
                           num=page_num)


@main_app.route("/order_query")
def order_post_all():
    session = make_session()
    orders = session.query(Order)\
        .filter(Order.status != "Finish")\
        .filter(Order.courise == None)\
        .order_by(Order.time)\
        .limit(PAGE_COUNT)
    page_num = 2
    return render_template("order_query_frame.html",
                           orders=orders,
                           num=page_num)


@main_app.route("/order_query_page/<int:page_number>")
def order_post_page(page_number):
    session = make_session()
    orders = session.query(Order)\
        .filter(Order.status != "Finish")\
        .filter(Order.courise == None)\
        .order_by(Order.time)\
        .limit(PAGE_COUNT)\
        .offset((page_number - 1) * PAGE_COUNT)
    page_num = page_number + 1
    return render_template("order_query_frame.html",
                           orders=orders,
                           num=page_num)


@main_app.route("/post_order", methods=["POST"])
def post_order():
    courise_id = request.form["exp_id"]
    order_id = request.form["order"]
    if not courise_id:
        return '{"result": false}'
    session = make_session()

    try:
        order = session.query(Order).filter(Order.ID == order_id)[0]
        # order = Order(order_id, courise_id)
        # order.ID = order_id
        # order. courise = courise_id
        order.courise = courise_id
        session.merge(order)
        session.commit()
    except Exception as e:
        print(e.message)
        session.rollback()
        return '{"result": false}'
    return '{"result": true}'


@main_app.route("/order_post", methods=["GET"])
def order_query():
    session = make_session()
    orders = session.query(Order)
    session = make_session()
    orders = session.query(Order)\
                    .filter(Order.status != "Finish")\
                    .order_by(Order.time)\
                    .limit(PAGE_COUNT)
    page_num = 2
    return render_template("order_post_frame.html",
                           orders=orders,
                           num=page_num)


@main_app.route("/order_post_page/<int:page_number>")
def order_query_page(page_number):
    session = make_session()
    orders = session.query(Order)\
        .filter(Order.status != "Finish")\
        .order_by(Order.time)\
        .limit(PAGE_COUNT)\
        .offset((page_number - 1) * PAGE_COUNT)
    page_num = page_number + 1
    return render_template("order_post_frame.html",
                           orders=orders,
                           num=page_num)


@main_app.route("/order_post_by_condition/<int:cond_type>", methods=["GET"])
def order_query_by_condition(cond_type=0):
    session = make_session()
    orders = session.query(Order)
    session = make_session()
    if cond_type == 0:
        orders = session.query(Order)\
                        .filter(Order.status == "Import")\
                        .filter(Order.courise == None)\
                        .order_by(Order.time)\
                        .limit(PAGE_COUNT)
    elif cond_type == 2:
        orders = session.query(Order)\
                        .filter(Order.status == "Finish")\
                        .order_by(Order.time)\
                        .limit(PAGE_COUNT)
    else:
        orders = session.query(Order)\
                        .filter(Order.status != "Finish")\
                        .filter(Order.courise != None)\
                        .order_by(Order.time)\
                        .limit(PAGE_COUNT)
    page_num = 2
    return render_template("order_post_frame.html",
                           orders=orders,
                           num=page_num)
