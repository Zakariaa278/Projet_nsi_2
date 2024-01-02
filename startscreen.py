"""
Startscreen of the snake game  
Credit : 
Designed by Zakaria ;
implemented by Zakaria ;
Graphisme by Demba ;
Music and sound by Zakaria
"""

import pyxel

class Menu:
    def __init__(self):
        self.team_selected = False
        self.player_team = None
        self.indesicive_player = False

    def update(self):
        pyxel.mouse(visible=True)

        if not self.team_selected and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if pyxel.mouse_x > 136:
                self.player_team = 'Apple'
                self.team_selected = True
                print(1)
            elif pyxel.mouse_x < 135:
                self.player_team = 'Snake'
                self.team_selected = True
                print(2)
            else:
                self.indesicive_player = True
                print(3)

    def draw(self):
        pyxel.cls(0)
        if not self.team_selected:
            pyxel.blt(0, 0, 0, 0, 0, 256, 256)
            pyxel.text(101, 40, 'Choose your team', 0)
            if self.indesicive_player:
                pyxel.text(15, 75, 'I can see you are undecided but you have to make a choice', 15)
        pyxel.text(10, 10, f"Mouse X: {pyxel.mouse_x}", 7)

    def start(self):
        pyxel.init(256, 256, title="Snake")
        pyxel.load("snakee.pyxres")
        pyxel.run(self.update, self.draw)