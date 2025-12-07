from utils import load_template
from config import settings

def generate_invoice():
    print("Starting Invoice Automation System...")
    template = load_template()
    print(f"Template loaded: {template}")
    print(f"Customer name: {settings['customer_name']}")
    print("Invoice generation complete (mock).")

if __name__ == "__main__":
    generate_invoice()
