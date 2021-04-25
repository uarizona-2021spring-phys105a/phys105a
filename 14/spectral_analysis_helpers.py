import numpy as np

def powerspec(ts, H):
    n = len(ts) // H - 1
    w = np.concatenate((np.linspace(0, 1, H, endpoint=False),
                        np.linspace(1, 0, H, endpoint=False)))
    spec = 0.0
    for i in range(n):
        spec += abs(np.fft.fft(w * ts[i*H:(i+2)*H]))**2
    return 0.5 * (spec[:H] + np.flip(spec[H:],0)) / n

def plot_ts_spec(ax, col, ts, title=None):
    ax[0,col].plot(np.real(ts))
    ax[0,col].set_xlabel("Time")
    ax[0,col].set_ylim((-3,3))
    ax[1,col].loglog(powerspec(ts, len(ts)//32))
    ax[1,col].set_xlabel('Frequency')
    ax[1,col].set_ylim((1e-3,1e9))
    if col == 0:
        ax[0,col].set_ylabel("Time Series")
        ax[1,col].set_ylabel('Power Spectrum')
    if title is not None:
        ax[0,col].set_title(title)

def plot_specs(ax, ts, titles):
    ax[0].loglog(powerspec(    ts,  len(ts)//32), label=titles[0])
    ax[1].loglog(powerspec(abs(ts), len(ts)//32), label=titles[1])
    for i in range(2):
        ax[i].set_ylim((1e-3,1e9))
        ax[i].set_xlabel('Frequency')
        ax[i].legend()
    ax[0].set_ylabel('Power Spectrum')
