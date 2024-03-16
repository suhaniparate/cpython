import tkinter as tk
from forex_python.converter import CurrencyRates

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = combo_from_currency.get()
    to_currency = combo_to_currency.get()

    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate

    lbl_result.config(text=f"{converted_amount:.2f} {to_currency}")

root = tk.Tk()
root.title("Currency Converter")

lbl_amount = tk.Label(root, text="Amount:")
lbl_amount.grid(row=0, column=0, padx=5, pady=5)

entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=5, pady=5)

lbl_from_currency = tk.Label(root, text="From Currency:")
lbl_from_currency.grid(row=1, column=0, padx=5, pady=5)

combo_from_currency = tk.Entry(root)
combo_from_currency.grid(row=1, column=1, padx=5, pady=5)

lbl_to_currency = tk.Label(root, text="To Currency:")
lbl_to_currency.grid(row=2, column=0, padx=5, pady=5)

combo_to_currency = tk.Entry(root)
combo_to_currency.grid(row=2, column=1, padx=5, pady=5)

btn_convert = tk.Button(root, text="Convert", command=convert_currency)
btn_convert.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

lbl_result = tk.Label(root, text="")
lbl_result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
