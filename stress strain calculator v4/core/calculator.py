# stress_strain/core/calculator.py
import pandas as pd
import matplotlib.pyplot as plt


def compute_stress(force_n: float, area_m2: float) -> float:  # whole thing
    try:
        res = force_n / area_m2
        return res
    except ZeroDivisionError:
        print("In getting the stress, cross-sectional area cannot be 0")


def compute_strain(delta_length_m: float, original_length_m: float) -> float:  # whole thing
    try:
        res = delta_length_m / original_length_m
        return res
    except ZeroDivisionError:
        print("In getting the strain, original length cannot be 0")


def compute_youngs_modulus(stress: float, strain: float) -> float:
    try:
        res = stress / strain
        return res
    except ZeroDivisionError:
        print("In young's modulus, strain cannot be 0")


def stats(data):
    df = pd.DataFrame(data)
    return df.describe()


def plot(x, y):
    plt.scatter(x, y)
    plt.xlabel("Stress (Pa)")
    plt.ylabel("Strain")
    plt.title("Correlation of Stress and Strain Between Materials")
    return plt.show()
