# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
# from frappe.integrations.utils import create_request_log
from frappe.exceptions import DoesNotExistError


@frappe.whitelist()
def rfid(tag_no):
    tag = frappe.db.sql("""
        SELECT
            api
        FROM
            `tabRFID Setting`
        WHERE
            %(tag_no)s BETWEEN starting_number AND ending_number
    """, {"tag_no": tag_no}, as_dict=True)[0]
    if tag:
        try:
            # doc = frappe.get_doc("RFID Tag", tag_no)
            frappe.call(tag["api"], tag_no)
        except DoesNotExistError:
            return _("Tag not found")


@frappe.whitelist()
def stock(tag_no):
    print("trying ")
    return "Tag Number " + unicode(tag_no)
