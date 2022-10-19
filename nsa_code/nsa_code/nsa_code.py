# Copyright (c) 2022, Networking Solutions Australia Pty Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def re_open_projects(doc, method):
	# called via Issue hook
	if doc.project and doc.status =='Open':
		pr = frappe.get_doc( "Project",doc.project)
		pr.status =="Open"
		pr.issue_status='Re-Open'
		pr.save(ignore_permissions=True)


	