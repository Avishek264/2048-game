from Tkinter import Frame, Label, CENTER

import LogicsFinal
import constants as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>",self.key_down)
        self.commands = {c.KEY_UP: LogicsFinal.move_up, c.KEY_DOWN: LogicsFinal.move_down,
                         c.KEY_LEFT: LogicsFinal.move_left, c.KEY_RIGHT: LogicsFinal.move_right}

        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.updated_grid_cells()

        self.mainloop()

    def init_grid(self):
