import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib import rcParams

rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 10
rcParams['lines.linewidth'] = 0.8
rcParams['lines.color'] = 'C0'
rcParams['legend.frameon'] = False
rcParams['axes.linewidth'] = 0.5
rcParams['xtick.major.width'] = 0.9
rcParams['xtick.minor.width'] = 0.9
rcParams['ytick.major.width'] = 0.9
rcParams['ytick.minor.width'] = 0.9
rcParams["savefig.format"] = 'jpg'
rcParams["savefig.transparent"] = False
rcParams["grid.alpha"] = 0.35
rcParams["grid.color"] = 'k'
rcParams["grid.linewidth"] = 0.5
rcParams['figure.titleweight'] = 'bold'
rcParams['savefig.dpi'] = 600


def plot(N, rD, rA, aA, eF, dt_out, num_steps, tFinal, K, Py):
    
    z = lambda x: np.min(x) if abs(np.min(x)) > abs(np.max(x)) else np.max(x)
    t = np.arange(0, num_steps) * dt_out
    
    # Plotting absolute accelerations
    fig, axs = plt.subplots(N+1, figsize=(8, 5), sharex=True, sharey=True)
    fig.suptitle('Absolute Accelerations')

    gm = aA[0]
    peak = z(gm)
    axs[0].plot(t, gm, f'k', label=f'Ground   peak: {peak:.2f} [m/s2]')

    for i, ax in enumerate(axs[1:]):
        x = aA[i+1]
        peak = z(x)
        ax.plot(t, x, f'C{i+1}', label=f'Floor {i+1}   peak: {peak:.2f} [m/s2]')

    for ax in axs:
        ax.set_xlim(.0, tFinal)
        ax.set_ylim(-8, 8)
        ax.grid()
        ax.legend(loc=(0.72, 1.0))
        ax.label_outer()
        ax.xaxis.set_major_locator(MultipleLocator(5))
        ax.yaxis.set_major_locator(MultipleLocator(4))

    axs[1].set_ylabel('Acceleration [m/s2]', loc='top')
    axs[1].yaxis.set_label_coords(-0.05, .5)
    axs[3].set_xlabel('Time [s]')

    plt.subplots_adjust(0.08, 0.1, 0.97, 0.9, 0.1, 0.4)
    plt.savefig(r'./nonlinear_mdof_abs_accel.jpg')


    # Plotting relative accelerations
    fig, axs = plt.subplots(N, figsize=(8, 3.8))
    fig.suptitle('Relative Accelerations')

    for i, ax in enumerate(axs):
        peak = z(rA[i])
        ax.plot(t, rA[i], f'C{i+1}', label=f'Floor {i+1}   peak: {peak:.2f} [m/s2]')
        ax.set_xlim(.0, tFinal)
        ax.set_ylim(-8, 8)
        ax.xaxis.set_major_locator(MultipleLocator(5))
        ax.yaxis.set_major_locator(MultipleLocator(4))
        ax.grid()
        ax.legend(loc=(0.72, 1.0))
        ax.label_outer()
    axs[1].set_ylabel('Acceleration [m/s2]')
    axs[2].set_xlabel('Time [s]')
    plt.subplots_adjust(0.08, 0.12, 0.97, 0.9, 0.1, 0.4)
    plt.savefig(r'./nonlinear_mdof_rel_accel.jpg')

    # Plotting relative displacements
    fig, axs = plt.subplots(N, figsize=(8, 3.8))
    fig.suptitle('Relative Displacements')

    for i, ax in enumerate(axs):
        peak = z(rD[i])
        ax.plot(t, rD[i], f'C{i+1}', label=f'Floor {i+1}   peak: {peak:.2f} [mm]')
        ax.set_xlim(.0, tFinal)
        ax.set_ylim(-80, 80)
        ax.xaxis.set_major_locator(MultipleLocator(5))
        ax.yaxis.set_major_locator(MultipleLocator(40))
        ax.grid()
        ax.legend(loc=(0.72, 1.0))
        ax.label_outer()
    axs[1].set_ylabel('Displacement [mm]')
    axs[2].set_xlabel('Time [s]')
    plt.subplots_adjust(0.08, 0.12, 0.97, 0.9, 0.1, 0.4)
    plt.savefig(r'./nonlinear_mdof_rel_disp.jpg')


    # Plotting Hysteresis by floor
    fig, axs = plt.subplots(1, N, figsize=(10, 3.5))
    fig.suptitle('Floor Hysteresis')

    axs[0].plot(rD[0,:], eF[0,:], 'C1', label=f'Floor 1 (K={K[0]} [kN/m]; Py={Py[0]:.2f} [kN])')
    axs[1].plot(rD[1,:] - rD[0,:], eF[1,:], 'C2', label=f'Floor 2 (K={K[1]} [kN/m]; Py={Py[1]:.2f} [kN])')
    axs[2].plot(rD[2,:] - rD[1,:], eF[2,:], 'C3', label=f'Floor 3 (K={K[2]} [kN/m]; Py={Py[2]:.2f} [kN])')

    for ax in axs:
        # ax.set_xlim(.0, tFinal)
        ax.set_ylim(-0.6, 0.6)
        ax.set_xlim(-30, 30)
        ax.grid()
        ax.legend(loc=(0.06, 1.0))
        ax.label_outer()
        ax.set_xlabel('Displacement [mm]')
        ax.xaxis.set_major_locator(MultipleLocator(10))
        ax.yaxis.set_major_locator(MultipleLocator(0.2))

    axs[0].set_ylabel('Force [kN]')
    plt.subplots_adjust(0.06, 0.13, 0.97, 0.86, 0.1)
    plt.savefig(r'./nonlinear_mdof_hysteresis.jpg')

    plt.show()


