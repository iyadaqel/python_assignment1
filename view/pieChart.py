import tkinter
root = tkinter.Tk()
def prop(n): 
    return 360.0 * n / 1000

#Sales
"""
tkinter.Label(root, text='Sales').pack()
c = tkinter.Canvas(width=154, height=154)
c.pack()
c.create_arc((2,2,152,152), fill="#FAF402", outline="#FAF402", start=prop(0), extent = prop(200))
c.create_arc((2,2,152,152), fill="#00AC36", outline="#00AC36", start=prop(200), extent = prop(400))
c.create_arc((2,2,152,152), fill="#7A0871", outline="#7A0871", start=prop(600), extent = prop(50))
c.create_arc((2,2,152,152), fill="#E00022", outline="#E00022", start=prop(650), extent = prop(200))
c.create_arc((2,2,152,152), fill="#294994", outline="#294994",  start=prop(850), extent = prop(150))
root.mainloop()
"""

#Payment

tkinter.Label(root, text='Credit Card vs Cash').pack()
c = tkinter.Canvas(width=154, height=154)
c.pack()
c.create_arc((2,2,152,152), fill="#FAF402", outline="#FAF402", start=prop(0), extent = prop(200))
c.create_arc((2,2,152,152), fill="#00AC36", outline="#00AC36", start=prop(200), extent = prop(800))

root.mainloop()
