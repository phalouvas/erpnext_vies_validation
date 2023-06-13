from . import __version__ as app_version

app_name = "vies_validation"
app_title = "Vies Validation"
app_publisher = "KAINOTOMO PH LTD"
app_description = "Validate customers Tax ID vs EU VIES system"
app_email = "info@kainotomo.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vies_validation/css/vies_validation.css"
# app_include_js = "/assets/vies_validation/js/vies_validation.js"

# include js, css files in header of web template
# web_include_css = "/assets/vies_validation/css/vies_validation.css"
# web_include_js = "/assets/vies_validation/js/vies_validation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "vies_validation/public/scss/website"

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "vies_validation.utils.jinja_methods",
#	"filters": "vies_validation.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "vies_validation.install.before_install"
# after_install = "vies_validation.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "vies_validation.uninstall.before_uninstall"
# after_uninstall = "vies_validation.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "vies_validation.notifications.get_notification_config"

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

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# vies_validation/hooks.py
doc_events = {
    "Quotation": {
        "before_save": "vies_validation.remove_tax.before_save_quotation"
    },
    "Sales Order": {
        "before_save": "vies_validation.remove_tax.before_save_sales_order"
    },    
    "Sales Invoice": {
        "before_save": "vies_validation.remove_tax.before_save_sales_invoice"
    }
}
# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"vies_validation.tasks.all"
#	],
#	"daily": [
#		"vies_validation.tasks.daily"
#	],
#	"hourly": [
#		"vies_validation.tasks.hourly"
#	],
#	"weekly": [
#		"vies_validation.tasks.weekly"
#	],
#	"monthly": [
#		"vies_validation.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "vies_validation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "vies_validation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "vies_validation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["vies_validation.utils.before_request"]
# after_request = ["vies_validation.utils.after_request"]

# Job Events
# ----------
# before_job = ["vies_validation.utils.before_job"]
# after_job = ["vies_validation.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"vies_validation.auth.validate"
# ]
