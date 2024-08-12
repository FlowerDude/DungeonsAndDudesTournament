import tkinter as tk
import random

class Participant:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    
class RRScheduler:
    def __init__(self, root):
        self.pcs = []
        self.rndCnt = 0
        self.rr = []

        self.result_text = tk.Text(root, height=25, width=50)
        self.result_text.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.charBtn = tk.Button(root, text="Assign Chars", command=self.assignChars)
        self.charBtn.grid(row=0, column=0, padx=10, pady=10)

        self.nextBtn = tk.Button(root, text="Next Round", command=self.generateSchedule, state=tk.DISABLED)
        self.nextBtn.grid(row=0, column=1, padx=10, pady=10)

    def assignChars(self):
        chars=[
        Participant('Ivan der Schreckliche'),
        Participant('Elara Abendklinge'),
        Participant('Thorin Eisenfaust'),
        Participant('Gorak der Ungebrochene'),
        Participant('Lyria Sternenweber'),
        Participant('Draven Schwarzdorn'),
        Participant('Finn der Waldläufer'),
        Participant('Orin Eisdrache')
        ]

        players = [
        'Dude',
        'Basti',
        'Michi',
        'Fidi',
        'Matto'
        ]

        for pl in random.sample(players, len(players)):
            chr = random.choice(chars)
            chars.remove(chr)
            self.pcs.append(chr)
            self.result_text.insert(tk.END, f"{pl} => {chr.getName()}\n")
        self.charBtn.config(state=tk.DISABLED)
        self.nextBtn.config(state=tk.NORMAL)

    def generateRR(self):
        chars = self.pcs[:]
        if len(chars) % 2 != 0:
            chars.append('')
        
        amnt = len(chars)
        for r in range(amnt-1):
            matches=[]
            for i in range(amnt//2):
                comp1 = chars[i]
                comp2 = chars[amnt-1-i]
                if comp1 != '' and comp2 != '':
                    matches.append((comp1.getName(), comp2.getName()))
            self.rr.append(matches)
            chars.insert(1, chars.pop())

    def generateSchedule(self):
        if self.rndCnt == 0:
            self.generateRR()    
            self.result_text.insert(tk.END, "\nRound Robin Schedule:\n")
        
        self.result_text.insert(tk.END, f"Round {self.rndCnt+1}:\n")
        for match in self.rr[self.rndCnt]:
            self.result_text.insert(tk.END, f"{match[0]} vs {match[1]}\n")

        self.rndCnt = self.rndCnt + 1
        if self.rndCnt == len(self.rr):
            self.result_text.insert(tk.END, "\nEND?\n")
            self.nextBtn.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    root.title("Round Robin Scheduler")
    app = RRScheduler(root)
    root.mainloop()

if __name__ == "__main__":
    main()
