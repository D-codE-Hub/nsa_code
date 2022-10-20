# Copyright (c) 2022, Networking Solutions Australia Pty Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def create_task_from_issue(doc, method):
	# called via Issue hook
	if doc.project and doc.status =='Open':
		if not frappe.db.exists("Task", doc.subject):
			task = frappe.new_doc("Task")
			task.status = "Open"
			task.subject = doc.subject
			task.issue = doc.name
			task.description =doc.description
			task.project = doc.project
			task.save(ignore_permissions=True)
	


# def re_open_projects(doc, method):

# 	if doc.project and doc.status =='Open':
# 		pr = frappe.get_doc( "Project",doc.project)
# 		pr.status =="Open"
# 		pr.issue_status='Re-Open'
# 		pr.save(ignore_permissions=True)