# Invoice / Quotation Business Logic

## 1. Required Inputs
- Customer Name
- Customer Phone / ID
- Product List
  - Product Name
  - Quantity
  - Unit Price
- Discount (optional)
- Tax (optional)

## 2. Calculations
- Line Total = Quantity × Unit Price
- Subtotal = Sum of Line Totals
- Discount Amount
- Tax Amount
- Final Payable Amount

## 3. Outputs
- Unique Invoice ID
- Invoice Date
- Customer Information
- Itemized Product Table
- Total Amount
- Status (Draft / Sent / Approved)

## 4. Automation Targets
- Auto-generate invoice number
- Auto-calculate totals
- Auto-save file
- Auto-log invoice in Excel
- Auto-send via Telegram or Email

## 5. Future Integrations
- CRM
- Payment Gateway
- Accounting Software

