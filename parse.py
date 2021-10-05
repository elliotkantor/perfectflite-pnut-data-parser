import re
import pandas as pd
from io import StringIO


class DataParser:
    def __init__(self, file):
        with open(file) as f:
            self.file = f.readlines()

    def parse(self):
        self.data_csv = ""
        include = False
        for line in self.file:
            if line.startswith("Data"):
                include = True
                continue
            if include:
                self.data_csv += line
        print(self.data_csv)

    def get_dataframe(self):
        self.df = pd.read_csv(
            StringIO(self.data_csv),
            names=["Time", "Altitude", "Velocity", "Temperature (F)", "Voltage"],
        )
        return self.df


if __name__ == "__main__":
    a = DataParser(".data/4B 109.pf2")
    a.parse()
    a.get_dataframe()