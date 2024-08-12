import tkinter as tk
import random

class Participant:
    
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
        

pcs = []
rndCnt = 0
rr = []

def assignChars(result_text, charBtn, nextBtn):

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
        pcs.append(chr)
        result_text.insert(tk.END, f"{pl} => {chr.getName()}\n")
    charBtn.config(state=tk.DISABLED)
    nextBtn.config(state=tk.NORMAL)
    return pcs

def generateRR(chars):
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
        rr.append(matches)
        chars.insert(1, chars.pop())

def generateSchedule(result_text, nextBtn):
    global rndCnt
    if rndCnt == 0:
        generateRR(pcs)    
        result_text.insert(tk.END, "\nRound Robin Schedule:\n")
    result_text.insert(tk.END, f"Round {rndCnt+1}:\n")
    for match in rr[rndCnt]:
        result_text.insert(tk.END, f"{match[0]} vs {match[1]}\n")



    rndCnt = rndCnt + 1
    if rndCnt == len(rr):
        result_text.insert(tk.END, "\nEND\n")
        nextBtn.config(state=tk.DISABLED)

def clear(result_text):
    result_text.delete()

def main():
    root = tk.Tk()
    root.title("Round Robin Scheduler")
    
    nextBtn = tk.Button(root, text="Next Round", command=lambda: generateSchedule(result_text, nextBtn), state=tk.DISABLED)
    charBtn = tk.Button(root, text="Assign Chars", command=lambda: assignChars(result_text, charBtn, nextBtn))

    result_text = tk.Text(root, height=25, width=50)

    charBtn.grid(row=0, column=0, padx=10, pady=10)
    nextBtn.grid(row=0, column=1, padx=10, pady=10)
    result_text.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
