import gym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fungsi untuk membuat GIF dari perjalanan karakter dalam Frozen Lake
def create_frozen_lake_gif():
    # Definisi custom map dengan posisi es dan finish sesuai instruksi
    custom_map = [
        'SFFFH',
        'HFHFF',
        'FFFHF',
        'FHFFF',
        'HFFFG'
    ]
    env = gym.make("FrozenLake-v1", desc=custom_map, is_slippery=False)
    env.reset()

    # Rincian perjalanan karakter utama
    # 0: Left, 1: Down, 2: Right, 3: Up
    actions = [3] + [2] * 3 + [1] * 1 + [2] + [1] + [1] + [1]

    # Fungsi untuk mengambil gambar dari lingkungan
    def render_env():
        return env.render(mode='rgb_array')

    # Fungsi animasi untuk membuat GIF
    def animate(i):
        action = actions[i]
        _, _, done, _ = env.step(action)
        img.set_array(render_env())
        if i == len(actions) - 1:
            # Ketika mencapai langkah terakhir, jangan lanjutkan ke langkah selanjutnya
            ani.event_source.stop()
        return img,

    # Membuat animasi GIF
    fig, ax = plt.subplots()
    img = ax.imshow(render_env())
    plt.axis('off')
    ani = animation.FuncAnimation(fig, animate, frames=len(actions), interval=500, blit=True)

    # Simpan animasi sebagai file GIF
    ani.save('frozen_lake.gif', writer='imagemagick', fps=1)

    plt.show()

# Panggil fungsi untuk membuat GIF
create_frozen_lake_gif()
