from datetime import datetime

def generate_invoice(customer_name, total_amount):
    invoice_id = datetime.now().strftime("%Y%m%d%H%M%S")
    
    invoice_data = {
        "invoice_id": invoice_id,
        "customer": customer_name,
        "amount": total_amount,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    return invoice_data


if __name__ == "__main__":
    invoice = generate_invoice("Test Customer", 12500000)
    print("Invoice Generated:")
    print(invoice)
