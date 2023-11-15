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
    # If in the doc invoice there is customer check if it has tax_id, it's country and if it is a shopping cart order remove tax
    if doc.customer:
        
        tax_id = frappe.db.get_value('Customer', doc.customer, 'tax_id')
        territory = frappe.db.get_value('Customer', doc.customer, 'territory')
        if tax_id and doc.is_pos == 1 and territory != "Cyprus":
            remove_tax(doc)

    pass