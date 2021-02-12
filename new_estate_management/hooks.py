# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "new_estate_management"
app_title = "New Estate Management"
app_publisher = "ridwan"
app_description = "Estate management App for Agents"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "ridwan.ajibola@manqala.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/new_estate_management/css/new_estate_management.css"
# app_include_js = "/assets/new_estate_management/js/new_estate_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/new_estate_management/css/new_estate_management.css"
# web_include_js = "/assets/new_estate_management/js/new_estate_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "new_estate_management/public/scss/website"

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

# before_install = "new_estate_management.install.before_install"
# after_install = "new_estate_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "new_estate_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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

# scheduler_events = {
# 	"all": [
# 		"new_estate_management.tasks.all"
# 	],
# 	"daily": [
# 		"new_estate_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"new_estate_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"new_estate_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"new_estate_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "new_estate_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "new_estate_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "new_estate_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

