import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def on_click(event):
    if event.inaxes is not None:
        x, y = event.xdata, event.ydata
        print(f'{x}, {y}')
        ax.plot(x, y, 'ro')
        plt.draw()

fig, ax = plt.subplots()
img = mpimg.imread('konkurs.png')

height, width, _ = img.shape
aspect_ratio = width / height

ax.set_xlim(0, width)
ax.set_ylim(0, height)
fig.set_size_inches(8, 8 / aspect_ratio)

ax.imshow(img, extent=[0, width, 0, height], alpha=0.5, aspect='auto')
fig.canvas.mpl_connect('button_press_event', on_click)

plt.show()


