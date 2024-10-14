from PIL import Image,ImageTk
import tkinter as tk


class GifPlayer:
    def __init__(self, master, gif_path, scale_factor=1.0):
        self.master = master
        self.gif_path = gif_path
        self.frames = []
        self.load_gif(scale_factor)
        self.current_frame = 0
        self.label = tk.Label(master)
        self.label.place(x=300, y=50)  # 设置初始位置

        # 开始播放 GIF
        self.play_gif()

    def load_gif(self, scale_factor):
        gif = Image.open(self.gif_path)
        try:
            while True:
                frame = gif.copy()
                if scale_factor != 1.0:  # 如果需要缩放
                    new_size = (int(frame.width * scale_factor), int(frame.height * scale_factor))
                    frame = frame.resize(new_size, Image.LANCZOS)  # 使用 LANCZOS 替代 ANTIALIAS
                self.frames.append(ImageTk.PhotoImage(frame))
                gif.seek(len(self.frames))  # 移动到下一个帧
        except EOFError:
            pass  # 到达 GIF 的末尾

    def play_gif(self):
        self.label.config(image=self.frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.master.after(100, self.play_gif)  # 每100毫秒更新一次