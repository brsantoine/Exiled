import tkinter as tk
import sys

class NamePrompt:
    def __init__(self):
        
        self.nameWindow = tk.Tk()
        self.nameLabel = tk.Label(self.nameWindow, text="Entrez votre pseudo ici")
        self.nameLabel.pack()
        self.nameValue = tk.StringVar()
        self.nameInput = tk.Entry(self.nameWindow, textvariable=self.nameValue, width=30)
        self.nameInput.pack()
        self.quitButton = tk.Button(self.nameWindow, text="Quitter", command=self.quit)
        self.quitButton.pack()
        self.continueButton = tk.Button(self.nameWindow, text="Continuer", command=self.nameWindow.quit)
        self.continueButton.pack()
        self.nameWindow.mainloop()

        self.name = self.nameValue.get()
        self.name = self.name.replace(' ','')
        self.name = self.name.replace(';','')
        if self.name == "":
            self.name = "UnknownPlayer"

        self.nameWindow.destroy()

    def quit(self):
        sys.exit()

    def getName(self):
        return self.name