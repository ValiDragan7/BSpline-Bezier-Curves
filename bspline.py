import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FFMpegWriter
from scipy import interpolate

plt.rcParams['animation.ffmpeg_path'] = 'C:/Users/Vali/Desktop/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe'


def plot_bspline_evolution(ctr):
    ctr = np.array(ctr)
    x = ctr[:, 0]
    y = ctr[:, 1]
    l = len(x)

    t = np.linspace(0, 1, l - 2, endpoint=True)
    t = np.append([0, 0, 0], t)
    t = np.append(t, [1, 1, 1])

    tck = [t, [x, y], 3]
    u3 = np.linspace(0, 1, max(l * 2, 70), endpoint=True)

    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'b', linewidth=2.0, label='B-spline curve')
    control_polygon, = ax.plot([], [], 'k--', label='Control polygon', marker='o', markerfacecolor='red')

    def init():
        ax.set_xlim(min(x) - 1, max(x) + 1)
        ax.set_ylim(min(y) - 1, max(y) + 1)
        ax.legend(loc='best')
        ax.set_title('Cubic B-spline curve evolution')
        return line, control_polygon

    def update(frame):
        t = np.linspace(0, 1, frame, endpoint=True)
        t = np.append([0, 0, 0], t)
        t = np.append(t, [1, 1, 1])

        tck = [t, [x, y], 3]
        out = interpolate.splev(u3, tck)

        line.set_data(out[0], out[1])
        control_polygon.set_data(x, y)
        return line, control_polygon

    # Increase the interval value for slower animation
    interval = 2000  # milliseconds (2 seconds)

    repeat_delay = 2000  # milliseconds (2 seconds)

    ani = animation.FuncAnimation(
        fig, update, frames=l, init_func=init, blit=True,
        interval=interval, repeat=True, repeat_delay=repeat_delay
    )

    # Save the animation as an MP4 video
    ani.save('bspline_cubic.mp4', writer='ffmpeg')


def plot_bspline_interpolation(ctr_list, frame):
    ctr = np.array(ctr_list[:frame])
    x = ctr[:, 0]
    y = ctr[:, 1]

    if len(x) < 4:
        return

    tck, u = interpolate.splprep([x, y], k=3, s=0)
    u = np.linspace(0, 1, num=100, endpoint=True)
    out = interpolate.splev(u, tck)

    plt.cla()  # Clear the current plot
    plt.plot(x, y, 'ro', out[0], out[1], 'b')
    plt.legend(['Points', 'Interpolated B-spline', 'True'], loc='best')
    plt.axis([min(x) - 1, max(x) + 1, min(y) - 1, max(y) + 1])
    plt.title('B-Spline Interpolation')


def interpolationFilm(ctr_list):
    plt.rcParams['animation.ffmpeg_path'] = 'C:/Users/Vali/Desktop/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe'
    metadata = dict(title='Interpolation', artist='Matplotlib', comment='B-Spline Interpolation')
    writer = FFMpegWriter(fps=1, metadata=metadata)
    fig = plt.figure()

    # Calculate the number of extra frames to hold the final position
    extra_frames = 5

    with writer.saving(fig, 'bspline_interpolation.mp4', dpi=100):
        for i in range(1, len(ctr_list) + 1):
            plot_bspline_interpolation(ctr_list, i)
            writer.grab_frame()

        # Hold the final position for extra frames
        for _ in range(extra_frames):
            plot_bspline_interpolation(ctr_list, len(ctr_list))
            writer.grab_frame()


def justplot_bspline_interpolation(ctr):
    ctr = np.array(ctr)
    x = ctr[:, 0]
    y = ctr[:, 1]

    tck, u = interpolate.splprep([x, y], k=3, s=0)
    u_new = np.linspace(0, 1, 100)
    out = interpolate.splev(u_new, tck)

    plt.plot(x, y, 'k--', label='Control polygon', marker='o', markerfacecolor='red')
    # plt.plot(x, y, 'ro', label='Control points only')
    plt.plot(out[0], out[1], 'b', linewidth=2.0, label='B-spline curve')
    plt.legend(loc='best')
    plt.axis([min(x) - 1, max(x) + 1, min(y) - 1, max(y) + 1])
    plt.title('Cubic B-spline curve evaluation')
    plt.show()


def justplot_cubic_bspline_curve(ctr):
    ctr = np.array(ctr)
    x = ctr[:, 0]
    y = ctr[:, 1]

    l = len(x)

    t = np.linspace(0, 1, l - 2, endpoint=True)
    t = np.append([0, 0, 0], t)
    t = np.append(t, [1, 1, 1])

    tck = [t, [x, y], 3]
    u = np.linspace(0, 1, max(l * 2, 70), endpoint=True)
    out = interpolate.splev(u, tck)

    plt.plot(x, y, 'k--', label='Control polygon', marker='o', markerfacecolor='red')
    # plt.plot(x, y, 'ro', label='Control points only')
    plt.plot(out[0], out[1], 'b', linewidth=2.0, label='B-spline curve')
    plt.legend(loc='best')
    plt.axis([min(x) - 1, max(x) + 1, min(y) - 1, max(y) + 1])
    plt.title('Cubic B-spline curve evaluation')
    plt.show()
