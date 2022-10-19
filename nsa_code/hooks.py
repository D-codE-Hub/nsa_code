from . import __version__ as app_version

app_name = "nsa_code"
app_title = "NSA-codE"
app_publisher = "Networking Solutions Australia Pty Ltd"
app_description = "App for Networking Solutions Australia Pty Ltd"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "shane.reglin@nsau.com.au"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nsa_code/css/nsa_code.css"
# app_include_js = "/assets/nsa_code/js/nsa_code.js"

# include js, css files in header of web template
# web_include_css = "/assets/nsa_code/css/nsa_code.css"
# web_include_js = "/assets/nsa_code/js/nsa_code.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "nsa_code/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "nsa_code.install.before_install"
# after_install = "nsa_code.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "nsa_code.uninstall.before_uninstall"
# after_uninstall = "nsa_code.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nsa_code.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes
# /home/vasco/nsa-bench/apps/nsa_code/nsa_code/overrides/custom_project.py
override_doctype_class = {
	"Project": "nsa_code.overrides.custom_project.CustomProject"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Issue": {
		"on_update": "nsa_code.nsa_code.nsa_code.re_open_projects",	
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"nsa_code.tasks.all"
#	],
#	"daily": [
#		"nsa_code.tasks.daily"
#	],
#	"hourly": [
#		"nsa_code.tasks.hourly"
#	],
#	"weekly": [
#		"nsa_code.tasks.weekly"
#	]
#	"monthly": [
#		"nsa_code.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "nsa_code.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "nsa_code.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "nsa_code.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"nsa_code.auth.validate"
# ]

fixtures = [{
		"dt": "Custom Field", 
		"filters":[["name", "in", [
									'Project-project_number',
									'Project-lrd_code',
									'Project-issue_status'
								  ]
				  ]]
	}]