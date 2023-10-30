import tkinter as tk
from tkinter import frame,label,entry,button,END, W

def hitung_luas():
    pj = float(txtpanjang.get)
    lb = float(txtlebar)

    l = pj * lb

    txtluas.delete(0,END)
    txtluas.insert(END,L)

    def hitung_keliling():
        pj = float(txtpanjang.get())
        lb = float(txtlebar.get())

        K = 2 * (pj + lb)

        txtkeliling.delete(0,END)
        txtkeliling.insert(END,K)

        def hitung():
            hitung_luas()
            hitung_keliling()

 # Create tkinter object
 app = tk.TK()

# Tambahkan judul
app.title(kalkulator luas dan keliling persegi panjang)

# windows
frame = frame(app)
frame.pack(padx=20, pady=20)

# label panjang
panjang = label(frame,text="panjang")
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# label lebar
lebar = label(frame, text="lebar:")
lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# texbox panjang
txtpanjang = entry(frame)
txtpanjang.grid(row=0, column=1)

# texbox lebar 
txtlebar = entry(frame)
txtlebar.grid(row=1, column=1)

# button
hitung_button = button(frame, text="hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output label luas
luas = label(frame, text="luas:")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

#Output label keliling
keliling = label(frame, text="keliling:")
keliling.grid(row=4, column=0, sticky=W, padx=5, pady=5)

#Output texbox luas
txtluas = entry(frame)
txtluas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output texbox keliling
txtkeliling = entry(frame)
txtkeliling.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop
