import re
import pandas as pd
from io import StringIO


class DataParser:
    def __init__(self, file: str):
        self.COLUMNS = ["Time", "Altitude", "Velocity", "Temperature (F)", "Voltage"]
        self.file = file
        self.split_file = self.file.split("\n")

    def parse(self):
        # get the csv data
        self.data_csv = ""
        self.metadata = ""
        csv_include = False
        for line in self.split_file:
            if line == "":
                # skip blank lines
                continue
            if line.startswith("Data"):
                csv_include = True
                continue
            if csv_include:
                self.data_csv += line
            else:
                self.metadata += line

        # make dataframe
        self.df = pd.read_csv(
            StringIO(self.data_csv),
            names=self.COLUMNS,
        )


if __name__ == "__main__":
    a = DataParser(".data/4B 109.pf2")
    a.parse()