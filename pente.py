from tkinter import *
from images import *


currentPlayer = 0
beadsPlayed = 0


def main():
    root = Tk()
    root.title("Pente")
    root.geometry("760x760")

    window = LabelFrame(root, padx=1, pady=1, bg="grey")
    window.pack()

    header = LabelFrame(window, padx=10, pady=10)
    header.grid(row=0, column=0, columnspan=2, sticky=W+E)
    label = Label(header, text="Header Frame")
    label.pack()

    players = LabelFrame(window, padx=10, pady=10, width=30)
    players.grid(row=1, column=0, sticky=N+S)
    label = Label(players, text="Players Frame")
    label.pack()

    board = LabelFrame(window, padx=20, pady=20)
    board.grid(row=1, column=1)

    footer = LabelFrame(window, padx=20, pady=20)
    footer.grid(row=2, column=0, columnspan=2, sticky=W+E)
    label = Label(footer, text="Footer Frame")
    label.pack()

    for row in range(19):
        for column in range(19):
            image = getImage(row, column)
            label = Label(board, image=image, width=27, height=27, padx=0, pady=0)
            label.grid(row=row, column=column, padx=0, pady=0)
            label.bind("<Enter>", enter)
            label.bind("<Leave>", leave)
            label.bind("<Button-1>", playBead)

    root.mainloop()


def enter(e):
    global beadsPlayed

    row = e.widget.grid_info()['row']
    column = e.widget.grid_info()['column']

    if beadsPlayed == 0 and (row != 9 or column != 9):
        return

    if beadsPlayed == 1 and (row > 6 and row < 12 and column > 6 and column < 12):
        return

    e.widget.config(image=getBeadImage(row, column, currentPlayer))


def leave(e):
    row = e.widget.grid_info()['row']
    column = e.widget.grid_info()['column']
    e.widget.config(image=getImage(row, column))


def playBead(e):
    global beadsPlayed

    row = e.widget.grid_info()['row']
    column = e.widget.grid_info()['column']

    if beadsPlayed == 0 and (row != 9 or column != 9):
        return

    if beadsPlayed == 1 and (row > 6 and row < 12 and column > 6 and column < 12):
        return

    e.widget.config(image=getBeadImage(row, column, currentPlayer))
    e.widget.unbind("<Enter>")
    e.widget.unbind("<Leave>")
    e.widget.unbind("<Button-1>")
    nextPlayer()


def nextPlayer():
    global currentPlayer, beadsPlayed
    beadsPlayed += 1
    if currentPlayer == 0:
        currentPlayer = 1
    else:
        currentPlayer = 0


main()
