import tkinter as tk
from playsound import playsound

class AudioPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Audio Player")

        self.play_button = tk.Button(master, text="Play", command=self.play_audio)
        self.play_button.pack(pady=10)

    def play_audio(self):
        try:
            playsound("SunshineLjud.mp3")  # Uppdatera med sökvägen till din ljudfil
        except Exception as e:
            print("Error playing audio:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayer(root)
    root.mainloop()
