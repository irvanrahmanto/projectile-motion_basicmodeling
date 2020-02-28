import numpy as np
import matplotlib.pyplot as plt
import math


def print_solution(total, range_var, max_var):
    print("Total: ", total)
    print("Jarak: ", range_var)
    print("Tinggi Maksimal: ", max_var)


def get_plot(nx, ny, ax, ay):
    plt.figure()
    plt.plot(nx, ny, c='r', label='numerical')
    plt.plot(ax, ay, c='b', label='analytic')
    plt.axhline(c='black')
    plt.axvline(c='black')
    plt.legend()
    plt.show()


class Projectile:
    ANGLE = 35
    ANGLE_RAD = (ANGLE / 360) * (2 * np.pi)
    GRAVITY = 9.806

    def __init__(self, x, y, v, time, dt, d, m):
        self.x = x
        self.y = y
        self.v = v
        self.time = time
        self.dt = dt
        self.d = d
        self.m = m

    def numeric(self):
        array_x = [self.x]
        array_y = [self.y]
        array_t = [self.time]

        ax = 0
        ay = -self.GRAVITY

        vx = self.v * np.cos(self.ANGLE_RAD)
        vy = self.v * np.sin(self.ANGLE_RAD)

        while self.y >= 0:
            vy += ay * self.dt
            vx += ax * self.dt
            self.y += vy * self.dt
            self.x += vx * self.dt
            self.time += self.dt

            if self.y <= 0:
                break

            array_x.append(self.x)
            array_y.append(self.y)
            array_t.append(self.time)

        return {
            "total_num": array_t[-1],
            "range_num": array_x[-1],
            "max_num": np.max(array_y),
            "array_x": array_x,
            "array_y": array_y,
            "array_t": array_t
        }

    def analytic(self, array_t):
        array_x = [0]
        array_y = [0]

        x0 = 0
        y0 = 0

        vx0 = self.v * np.cos(self.ANGLE_RAD)
        vy0 = self.v * np.sin(self.ANGLE_RAD)

        vx = vx0
        vy = -vy0

        for t in array_t:
            v = math.sqrt((vx ** 2) + (vy ** 2))
            ax = (-self.d / self.m) * v * vx
            ay = -self.GRAVITY - ((self.d / self.m) * v * vy)
            x = x0 + (vx0 * t) + ((ax / 2) * t ** 2)
            y = y0 + (vy0 * t) + ((ay / 2) * t ** 2)
            array_x.append(x)
            array_y.append(y)

        total = (2 * self.v * np.sin(self.ANGLE_RAD)) / self.GRAVITY

        return {
            "total_num": total,
            "range_num": self.v * np.cos(self.ANGLE_RAD) * total,
            "max_num": (self.v ** 2 * np.sin(self.ANGLE_RAD) ** 2) / (2 * self.GRAVITY),
            "array_x": array_x,
            "array_y": array_y
        }

    def print_result(self):
        numeric = self.numeric()
        analytic = self.analytic(numeric["array_t"])

        print("Solusi numerik")
        print_solution(numeric["total_num"], numeric["range_num"], numeric["max_num"])

        print("Solusi analytic")
        print_solution(analytic["total_num"], analytic["range_num"], analytic["max_num"])

        get_plot(numeric["array_x"], numeric["array_y"], analytic["array_x"], analytic["array_y"])


pr = Projectile(0, 0, 50, 0, 0.1, 0.0013, 150)
pr.print_result()
