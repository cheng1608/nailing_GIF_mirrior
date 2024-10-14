import os
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
from gifPlayer import GifPlayer
import sys

input_folder = r'nailong_input'
output_folder = r'nailong_output'

if not os.path.exists(input_folder):
    os.makedirs(input_folder)

# pyinstaller --onefile --add-data "resources;resources" main.py

def mirLR(input_path, output_path):
    gif = Image.open(input_path)
    frames = []
    try:
        while True:
            frame = gif.copy()
            width, height = frame.size

            mid = width // 2
            left_half = frame.crop((0, 0, mid, height))  # 提取左边
            mirrored_half = left_half.transpose(Image.FLIP_LEFT_RIGHT)  # 镜像左边

            new_frame = Image.new('RGB', (width, height))
            new_frame.paste(left_half, (0, 0))  # 画左边
            new_frame.paste(mirrored_half, (mid, 0))  # 画右边

            frames.append(new_frame)
            gif.seek(len(frames))
    except EOFError:
        pass

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=gif.info['duration'], loop=0)
    print(f'{os.path.basename(input_path)}')

def mirTB(input_path, output_path):
    gif = Image.open(input_path)
    frames = []
    try:
        while True:
            frame = gif.copy()
            width, height = frame.size

            mid = height // 2
            bottom_half = frame.crop((0, 0, width, mid))  # 提取下边
            mirrored_half = bottom_half.transpose(Image.FLIP_TOP_BOTTOM)  # 镜像下边

            new_frame = Image.new('RGB', (width, height))
            new_frame.paste(bottom_half, (0, 0))  # 画上边
            new_frame.paste(mirrored_half, (0, mid))  # 画下边

            frames.append(new_frame)
            gif.seek(len(frames))
    except EOFError:
        pass

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=gif.info['duration'], loop=0)
    print(f'{os.path.basename(input_path)}')

def mirFO(input_path, output_path):
    gif = Image.open(input_path)
    frames = []
    try:
        while True:
            frame = gif.copy()
            width, height = frame.size

            midh = height // 2
            midw = width // 2

            bottom_half = frame.crop((0, 0, width, midh))
            mirrored_half = bottom_half.transpose(Image.FLIP_TOP_BOTTOM)
            new_frame = Image.new('RGB', (width, height))
            new_frame.paste(bottom_half, (0, 0))
            new_frame.paste(mirrored_half, (0, midh))

            frame = new_frame

            left_half = frame.crop((0, 0, midw, height))
            mirrored_half = left_half.transpose(Image.FLIP_LEFT_RIGHT)
            new_frame = Image.new('RGB', (width, height))
            new_frame.paste(left_half, (0, 0))
            new_frame.paste(mirrored_half, (midw, 0))

            frames.append(new_frame)
            gif.seek(len(frames))
    except EOFError:
        pass

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=gif.info['duration'], loop=0)
    print(f'{os.path.basename(input_path)}')


def funBW(input_path, output_path):
    gif = Image.open(input_path)
    frames = []

    try:
        while True:
            frame = gif.copy()
            black_and_white_frame = frame.convert('L')

            frames.append(black_and_white_frame)

            gif.seek(len(frames))
    except EOFError:
        pass

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=gif.info['duration'], loop=0)
    print(f'{os.path.basename(input_path)} 转换完成，保存为 {os.path.basename(output_path)}')


def funRB(input_path, output_path):
    gif = Image.open(input_path)
    frames = []
    gap_counter=0
    GAP =7 #决定变换的时间
    isRed=True
    try:
        while True:
            gap_counter+=1
            if gap_counter == GAP:
                gap_counter=0
                isRed^=1

            frame = gif.copy()
            # 转换为 RGB 模式
            rgb_frame = frame.convert('RGB')
            new_frame = Image.new('RGB', rgb_frame.size)

            if isRed == True:
                # 遍历每个像素，将绿色和蓝色通道设为 0
                for x in range(rgb_frame.width):
                    for y in range(rgb_frame.height):
                        r, g, b = rgb_frame.getpixel((x, y))
                        new_frame.putpixel((x, y), (r, 0, 0))
            else:
                # 遍历每个像素，将绿色和红色通道设为 0
                for x in range(rgb_frame.width):
                    for y in range(rgb_frame.height):
                        r, g, b = rgb_frame.getpixel((x, y))
                        new_frame.putpixel((x, y), (0, 0, b))

            frames.append(new_frame)
            gif.seek(len(frames))
    except EOFError:
        pass

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=gif.info['duration'], loop=0)
    print(f'{os.path.basename(input_path)} 转换完成，保存为 {os.path.basename(output_path)}')

def cut9(input_path, output_path):
    gif = Image.open(input_path)
    frames = []

    try:
        while True:
            frame = gif.copy()
            width, height = frame.size

            lenh = height // 3
            lenw = width // 3

            shikuai=[] #奶龙 石块
            index=[3,8,1,2,4,6,7,0,5]
            for i in range(3):
                for j in range(3):
                    new_cut = frame.crop((i*lenw, j*lenh, (i+1)*lenw, (j+1)*lenh))
                    shikuai.append(new_cut)

            new_frame = Image.new('RGB', (width, height))

            for i in range (9):
                pas = index[i]
                new_frame.paste(shikuai[i], ((pas//3)*lenw, (pas%3)*lenh))

            frames.append(new_frame)
            gif.seek(len(frames))
    except EOFError:
        pass

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=gif.info['duration'], loop=0)
    print(f'{os.path.basename(input_path)} 转换完成，保存为 {os.path.basename(output_path)}')


def RevC(input_path, output_path):
    gif = Image.open(input_path)
    frames = []

    try:
        while True:
            frame = gif.copy()
            rev_frame = Image.eval(frame, lambda x: 255 - x)

            frames.append(rev_frame)

            gif.seek(len(frames))
    except EOFError:
        pass

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=gif.info['duration'], loop=0)
    print(f'{os.path.basename(input_path)} 转换完成，保存为 {os.path.basename(output_path)}')


def mosaic(input_path, output_path ):
    gif = Image.open(input_path)
    frames = []
    block_size = 20
    try:
        while True:
            frame = gif.copy().convert('RGB')  # 确保转换为 RGB 模式
            width, height = frame.size
            mosaic_img = Image.new('RGB', frame.size)

            for y in range(0, height, block_size):
                for x in range(0, width, block_size):
                    box = (x, y, min(x + block_size, width), min(y + block_size, height))
                    block = frame.crop(box)

                    #计算平均颜色
                    pixels = list(block.getdata())
                    if not pixels:  # 防止空块导致的错误
                        continue

                    # 确保所有像素都是 RGB 格式
                    if isinstance(pixels[0], int):  # 处理灰度图像的情况
                        pixels = [(p, p, p) for p in pixels]  # 转换为 RGB

                    avg_color = tuple(
                        sum(channel) // len(channel) for channel in zip(*pixels)
                    )

                    # 在新图像中填充
                    for i in range(block_size):
                        for j in range(block_size):
                            if x + i < width and y + j < height:
                                mosaic_img.putpixel((x + i, y + j), avg_color)

            frames.append(mosaic_img)
            gif.seek(len(frames))
    except EOFError:
        pass

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=gif.info['duration'], loop=0)
    print(f'Processed {os.path.basename(input_path)}')

def unique_output_path(output_folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(output_folder, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return os.path.join(output_folder, new_filename)

def batch_process(input_folder, output_folder, operation):
    os.makedirs(output_folder, exist_ok=True)  # 确保输出文件夹存在

    tot = 0
    for filename in os.listdir(input_folder):
        if filename.endswith('.gif'):
            input_path = os.path.join(input_folder, filename)
            output_path = unique_output_path(output_folder, f'mir_{filename}')  # 生成唯一的输出文件名
            tot += 1

            if operation == 'mirLR':
                mirLR(input_path, output_path)
            elif operation == 'mirTB':
                mirTB(input_path, output_path)
            elif operation == 'mirFO':
                mirFO(input_path, output_path)
            elif operation == 'funBW':
                funBW(input_path, output_path)
            elif operation == 'funRB':
                funRB(input_path,output_path)
            elif operation == 'cut9':
                cut9(input_path, output_path)
            elif operation == 'RevC':
                RevC(input_path, output_path)
            elif operation == 'mosaic':
                mosaic(input_path, output_path)


    messagebox.showinfo("处理完成", f'共处理{tot}张奶龙！')

def select_input_folder():
    global input_folder
    input_folder = filedialog.askdirectory()
    input_folder_label.config(text=f"输入文件夹: {input_folder}")

def select_output_folder():
    global output_folder
    output_folder = filedialog.askdirectory()
    output_folder_label.config(text=f"输出文件夹: {output_folder}")

def process_gifs(operation):
    if not input_folder or not output_folder:
        messagebox.showwarning("警告", "请先选择输入和输出文件夹！")
        return
    batch_process(input_folder, output_folder, operation)

def update_labels():
    input_folder_label.config(text=f"输入文件夹: {input_folder}")
    output_folder_label.config(text=f"输出文件夹: {output_folder}")



# 创建主窗口
root = tk.Tk()
root.title("奶龙奶龙")
root.geometry("600x400")
root.resizable(False, False)

# 输入和输出文件夹选择
input_folder_button = tk.Button(root, text="选择输入文件夹", command=select_input_folder)
input_folder_button.place(x=30, y=20)

output_folder_button = tk.Button(root, text="选择输出文件夹", command=select_output_folder)
output_folder_button.place(x=30, y=60)

input_folder_label = tk.Label(root, text="输入文件夹: ")
input_folder_label.place(x=20, y=350)

output_folder_label = tk.Label(root, text="输出文件夹: ")
output_folder_label.place(x=20, y=370)

# 操作按钮
mirLR_button = tk.Button(root, text="左右翻转", command=lambda: process_gifs('mirLR'))
mirLR_button.place(x=30, y=120)

mirTB_button = tk.Button(root, text="上下翻转", command=lambda: process_gifs('mirTB'))
mirTB_button.place(x=30, y=160)

mirFO_button = tk.Button(root, text="四角翻转", command=lambda: process_gifs('mirFO'))
mirFO_button.place(x=30, y=200)

funBW_button = tk.Button(root, text="转换黑白", command=lambda: process_gifs('funBW'))
funBW_button.place(x=30, y=240)

funRB_button = tk.Button(root, text="一念神魔", command=lambda: process_gifs('funRB'))
funRB_button.place(x=100, y=120)

cut9_button = tk.Button(root, text="三阶幻方", command=lambda: process_gifs('cut9'))
cut9_button.place(x=100, y=160)

RevC_button = tk.Button(root, text="颜色反相", command=lambda: process_gifs('RevC'))
RevC_button.place(x=100, y=200)

mosaic_button = tk.Button(root, text="龟兔打马", command=lambda: process_gifs('mosaic'))
mosaic_button.place(x=100, y=240)

# 使用资源文件
def resource_path(relative_path):
    try:
        return os.path.join(sys._MEIPASS, relative_path)
    except Exception:
        return os.path.join(os.path.abspath("."), relative_path)

gif_path = resource_path(r'resources/mir_show.gif')
# 显示GIF的路径
scale_factor = 0.6  # 设置缩放因子
gif_player = GifPlayer(root, gif_path, scale_factor)

update_labels()
# 启动主循环
root.mainloop()
