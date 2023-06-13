import frappe

def remove_tax(doc, method=None):
    doc.taxes_and_charges = ""
    doc.taxes = []
    doc.calculate_taxes_and_totals()
    pass

@frappe.whitelist()
def before_save_quotation(doc, method=None):
    tax_id = frappe.db.get_value('Customer', doc.customer, 'tax_id')
    if tax_id and doc.order_type == "Shopping Cart":
        remove_tax(doc)
    pass

@frappe.whitelist()
def before_save_sales_order(doc, method=None):
    if doc.tax_id and doc.order_type == "Shopping Cart":
       remove_tax(doc)
    pass

@frappe.whitelist()
def before_save_sales_invoice(doc, method=None):
    sales_order = frappe.get_doc("Sales Order", doc.items[0].sales_order)
    if doc.tax_id and sales_order.order_type == "Shopping Cart":
       remove_tax(doc)
    pass