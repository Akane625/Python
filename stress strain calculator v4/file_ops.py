# stress_strain/io/file_ops.py
import pandas as pd


def export_csv(data: dict):
    df = pd.DataFrame(data)

    try:
        with open("Stress_Strain_Record.csv", "r"):
            df.to_csv("Stress_Strain_Record.csv", mode='a', index=False, header=False)

    except FileNotFoundError:
        df.to_csv("Stress_Strain_Record.csv", mode='w', index=False)
