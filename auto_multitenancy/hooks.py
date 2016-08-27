# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "auto_multitenancy"
app_title = "Auto Multitenancy"
app_publisher = "New Indictrans Technologies pvt. ltd."
app_description = "This app automates the site creation from site master doctpye"
app_icon = "icon-book"
app_color = "#589494"
app_email = "gangadhar.k@indictranstech.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/auto_multitenancy/css/auto_multitenancy.css"
# app_include_js = "/assets/auto_multitenancy/js/auto_multitenancy.js"

# include js, css files in header of web template
# web_include_css = "/assets/auto_multitenancy/css/auto_multitenancy.css"
# web_include_js = "/assets/auto_multitenancy/js/auto_multitenancy.js"

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

# before_install = "auto_multitenancy.install.before_install"
# after_install = "auto_multitenancy.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "auto_multitenancy.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
permission_query_conditions = {
	"Employee": "erpnext.hr.doctype.attendance.attendance.get_permission_query_conditions",
}
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"all": [
		"erpnext.crm.doctype.appointment.appointment.create_site"
	]
	# ,"daily": [
	# 	"auto_multitenancy.tasks.daily"
	# ],
	# "hourly": [
	# 	"auto_multitenancy.tasks.hourly"
	# ],
	# "weekly": [
	# 	"auto_multitenancy.tasks.weekly"
	# ]
	# "monthly": [
	# 	"auto_multitenancy.tasks.monthly"
	# ]
}

# Testing
# -------

# before_tests = "auto_multitenancy.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "auto_multitenancy.event.get_events"
# }

