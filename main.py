import tkinter as tk  #for ui tkinter
import fnmatch        
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
canvas.config(bg = "Black")


rootpath = r"C:\\Users\USER\Music\Music"
pattern = "*.mp3"

mixer.init()

def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    mixer.music.play()
    mixer.music.set_volume(Volume.get())
    print(mixer.music.get_volume())
    print(Volume.get())

def stop():
    mixer.music.stop()
    listbox.select_clear("active")

def next():
    next=listbox.curselection()
    next = next[0]+1
    next_name = listbox.get(next )
    label.config(text= next_name)
    mixer.music.load(rootpath + "\\" + next_name)
    mixer.music.play()
    listbox.select_clear(0,'end')
    listbox.activate(next)
    listbox.select_set(next)

def prev():
    next=listbox.curselection()
    next = next[0]-1
    next_name = listbox.get(next )
    label.config(text= next_name)
    mixer.music.load(rootpath + "\\" + next_name)
    mixer.music.play()
    listbox.select_clear(0,'end')
    listbox.activate(next)
    listbox.select_set(next)

def pause():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play Again"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"


listbox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = "100", font = ('poppins', 14))
listbox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text = '', bg = 'black', fg = 'yellow', font = ('poppins', 18))
label.pack(pady = 15)

top=tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor="center")


#for next previous button
prevButton = tk.Button(canvas, text = "Perv", borderwidth = 10, command = prev )
prevButton.pack(pady = 15, in_=top, side='left')
nextButton = tk.Button(canvas, text = "Next", borderwidth = 10, command = next)
nextButton.pack(pady = 15, in_=top, side='right')
stopButton = tk.Button(canvas, text = "Stop", borderwidth = 10, command = stop)
stopButton.pack(pady = 15, in_=top, side='left')
playButton = tk.Button(canvas, text = "Play", borderwidth = 10, command=select)
playButton.pack(pady = 15, in_=top, side='left')
pauseButton = tk.Button(canvas, text = "Pause", borderwidth = 10, command= pause)
pauseButton.pack(pady = 15, in_=top, side='left')



Volume = tk.Scale(canvas, from_= 0.0, to_=1.0, orient= tk.HORIZONTAL, resolution = 0.1)
Volume.pack(pady = 15, in_=top, side='right')

for root, dirs, files in os.walk(rootpath):     #for list of songs
    for filename in fnmatch.filter(files, pattern):
        listbox.insert("end", filename)

canvas.mainloop()