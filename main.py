import tkinter as tk

calc = tk.Tk()
calc.title("Calc")

buttons = [
'1',  '2',  '3',
'4',  '5',  '6',
'7',  '8',  '9',  '0',
'-', '/', '*' '.', '@',  '+',  '=', 'Clear']

# set up GUI
row = 1
col = 0
for i in buttons:
    button_style = 'raised'
    action = lambda x = i: click_event(x)
    tk.Button(calc, text = i, width = 7, height = 7, relief = button_style, command = action) \
		.grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 4:
        col = 0
        row += 1

display = tk.Entry(calc, width = 40, bg = "white")
display.grid(row = 0, column = 0, columnspan = 5)

def click_event(key):

    if key == '=':
        # safeguard against integer division
        if '/' in display.get() and '.' not in display.get():
            display.insert(tk.END, ".0")
			
        # attempt to evaluate results
        try:
            result = eval(display.get())
            display.insert(tk.END, " = " + str(result))
        except:
            display.insert(tk.END, "   Error, use only valid chars")
			
	# Clear -> clear display		
    elif key == 'Clear':
        display.delete(0, tk.END)

    else:
        if '=' in display.get():
            display.delete(0, tk.END)
        display.insert(tk.END, key)

# RUNTIME
calc.mainloop()
