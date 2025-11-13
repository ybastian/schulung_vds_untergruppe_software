import tkinter as tk
root=tk.Tk()
root.title('Hallo, tkinter!')
label=tk.Label(root,text='Hallo, Welt!',font=('Arial',16))
label.pack(padx=50,pady=70)
button=tk.Button(root,text='Schließen',command=root.destroy)
button.pack(pady=10)
root.mainloop()


mit Teilnehmern im Workshop angepasst:

import tkinter as tk
root=tk.Tk()
root.title('Hallo, tkinter!')
label=tk.Label(root,text='Hallo, Welt!',font=('Arial',16))
label.pack(padx=50,pady=70)
button=tk.Button(root,text='Schließen',command=root.destroy)
button.pack(pady=10)
root.mainloop()
