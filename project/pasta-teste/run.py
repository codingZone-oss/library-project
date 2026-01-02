import tkinter as tk

# window informations
window = tk.Tk()
window.geometry('800x430')
window.title('Tela login')

# inside window
# lablels data1
lbl1 = tk.Label(window, text='User Name', font=('Arial', 11))
lbl1.pack(pady=10)

# text fild data1
txt_user = tk.Entry(window, font=('Arial', 11))
txt_user.pack(pady=10)


# lablels data1
lbl2 = tk.Label(window, text='Password', font=('Arial', 11))
lbl2.pack(pady=11)


# text fild data2
txt_password = tk.Entry(window, font=('Arial', 11))
txt_password.pack(pady=11)


# get text fild 1
def get_text():
    user = txt_user.get()
    password = txt_password.get()
    print(f'Hello {user} he´is your password {password}')


# button send
btn = tk.Button(window, text='enviar', font=('Arial', 12), command= get_text)
btn.pack(pady=12)


window.mainloop()