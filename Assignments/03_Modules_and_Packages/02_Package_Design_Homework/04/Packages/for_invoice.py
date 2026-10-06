def invoice(name,price,tax=10):
    print("\n\tInvoice\nProduct Name:",name)
    print("Product Price:",price)
    return price+price*tax/100
