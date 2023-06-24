import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.playlist = []

        self.current_song = 0

        self.paused = False

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Create playlist label
        self.playlist_label = tk.Label(self.root, text="Playlist")
        self.playlist_label.pack()

        # Create listbox to display playlist
        self.playlist_box = tk.Listbox(self.root, width=50)
        self.playlist_box.pack()

        # Create buttons
        self.add_button = tk.Button(self.root, text="Add Song", command=self.add_song)
        self.add_button.pack()

        self.remove_button = tk.Button(self.root, text="Remove Song", command=self.remove_song)
        self.remove_button.pack()

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack()

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if song_path:
            self.playlist.append(song_path)
            self.playlist_box.insert(tk.END, song_path)

    def remove_song(self):
        selected_song = self.playlist_box.curselection()
        if selected_song:
            index = int(selected_song[0])
            self.playlist_box.delete(selected_song)
            self.playlist.pop(index)

    def play_music(self):
        if not self.paused:
           
            song_path = self.playlist[self.current_song]
            pygame.mixer.music.load(song_path)

        pygame.mixer.music.play()

    def pause_music(self):
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
        else:
            pygame.mixer.music.unpause()
            self.paused = False

    def stop_music(self):
        pygame.mixer.music.stop()

    def run(self):
        self.root.mainloop()


root = tk.Tk()


music_player = MusicPlayer(root)


music_player.run()