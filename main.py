from interfaces import *

numberOfColumn = 7
numberOfRow = 6

window = Tk()
window.title('Puissance 4')

interface = Interface(window,numberOfRow,numberOfColumn)

interface.mainloop()
interface.destroy()