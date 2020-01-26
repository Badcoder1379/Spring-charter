from math import cos, sqrt, exp, sin


def get_result_points(a, b, w0, dt, t1, t2):
    list1 = func1(a, b, w0, dt, t1, t2)  # canvas
    list2 = func2(a, b, w0, dt, t1, t2)
    list3 = func3(a, b, w0, dt, t1, t2)

    return [list1, list2, list3]


def func1(a, b, w0, dt, t1, t2):
    a = float(a)
    b = float(b)
    w0 = float(w0)
    dt = float(dt)
    endTime = float(t2)

    x1 = a
    x2 = 0.0
    currentTime = 0.0

    def f1(x1, x2, t):
        dx1dt = x2
        return dx1dt

    def f2(x1, x2, t):
        dx2dt = -b * x2 - sin(x1) + w0 * cos(0.7 * t)
        return dx2dt

    results = []

    for j in range(int(endTime / dt)):
        if currentTime >= float(t1):
            results.append([x1, x2])
        k11 = dt * f1(x1, x2, currentTime)
        k21 = dt * f2(x1, x2, currentTime)
        k12 = dt * f1(x1 + 0.5 * k11, x2 + 0.5 * k21, currentTime + 0.5 * dt)
        k22 = dt * f2(x1 + 0.5 * k11, x2 + 0.5 * k21, currentTime + 0.5 * dt)
        k13 = dt * f1(x1 + 0.5 * k12, x2 + 0.5 * k22, currentTime + 0.5 * dt)
        k23 = dt * f2(x1 + 0.5 * k12, x2 + 0.5 * k22, currentTime + 0.5 * dt)
        k14 = dt * f1(x1 + k13, x2 + k23, currentTime + dt)
        k24 = dt * f2(x1 + k13, x2 + k23, currentTime + dt)
        x1 += (k11 + 2 * k12 + 2 * k13 + k14) / 6
        x2 += (k21 + 2 * k22 + 2 * k23 + k24) / 6
        currentTime += dt

    return results


def func2(a, b, w0, dt, t1, t2):
    a = float(a)
    b = float(b)
    w0 = float(w0)
    dt = float(dt)
    endTime = float(t2)

    x1 = a
    x2 = 0.0
    currentTime = 0.0

    def f1(x1, x2, t):
        dx1dt = x2
        return dx1dt

    def f2(x1, x2, t):
        dx2dt = -b * x2 - sin(x1) + w0 * cos(0.7 * t)
        return dx2dt

    results = []

    for j in range(int(endTime / dt)):
        if currentTime >= float(t1):
            results.append([currentTime, x1])
        k11 = dt * f1(x1, x2, currentTime)
        k21 = dt * f2(x1, x2, currentTime)
        k12 = dt * f1(x1 + 0.5 * k11, x2 + 0.5 * k21, currentTime + 0.5 * dt)
        k22 = dt * f2(x1 + 0.5 * k11, x2 + 0.5 * k21, currentTime + 0.5 * dt)
        k13 = dt * f1(x1 + 0.5 * k12, x2 + 0.5 * k22, currentTime + 0.5 * dt)
        k23 = dt * f2(x1 + 0.5 * k12, x2 + 0.5 * k22, currentTime + 0.5 * dt)
        k14 = dt * f1(x1 + k13, x2 + k23, currentTime + dt)
        k24 = dt * f2(x1 + k13, x2 + k23, currentTime + dt)
        x1 += (k11 + 2 * k12 + 2 * k13 + k14) / 6
        x2 += (k21 + 2 * k22 + 2 * k23 + k24) / 6
        currentTime += dt

    return results


def func3(a, b, w0, dt, t1, t2):
    a = float(a)
    b = float(b)
    w0 = float(w0)
    dt = float(dt)
    endTime = float(t2)

    x1 = a
    x2 = 0.0
    currentTime = 0.0

    def f1(x1, x2, t):
        dx1dt = x2
        return dx1dt

    def f2(x1, x2, t):
        dx2dt = -b * x2 - sin(x1) + w0 * cos(0.7 * t)
        return dx2dt

    results = []

    for j in range(int(endTime / dt)):
        if currentTime >= float(t1):
            results.append([currentTime, x2])
        k11 = dt * f1(x1, x2, currentTime)
        k21 = dt * f2(x1, x2, currentTime)
        k12 = dt * f1(x1 + 0.5 * k11, x2 + 0.5 * k21, currentTime + 0.5 * dt)
        k22 = dt * f2(x1 + 0.5 * k11, x2 + 0.5 * k21, currentTime + 0.5 * dt)
        k13 = dt * f1(x1 + 0.5 * k12, x2 + 0.5 * k22, currentTime + 0.5 * dt)
        k23 = dt * f2(x1 + 0.5 * k12, x2 + 0.5 * k22, currentTime + 0.5 * dt)
        k14 = dt * f1(x1 + k13, x2 + k23, currentTime + dt)
        k24 = dt * f2(x1 + k13, x2 + k23, currentTime + dt)
        x1 += (k11 + 2 * k12 + 2 * k13 + k14) / 6
        x2 += (k21 + 2 * k22 + 2 * k23 + k24) / 6
        currentTime += dt

    return results
