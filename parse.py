import re
import pandas as pd
from io import StringIO


class DataParser:
    def __init__(self, file: str):
        self.COLUMNS = ["Time", "Altitude", "Velocity", "Temperature (F)", "Voltage"]
        self.file = file
        self.split_file = self.file.split("\n")

    def parse(self):
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
                if line.startswith("Apogee"):
                    self.apogee = re.search(r"^.+: (\d+)'.*$", line).group(1)
                elif line.startswith("Flight Number"):
                    self.flight_number = re.search(r"^.+: (\d+).*$", line).group(1)

        self.df = pd.read_csv(
            StringIO(self.data_csv),
            names=self.COLUMNS,
        )
        # self.metadata_json = {}

        # metadata_json = self.metadata.split("\n")[1:-2]
        # print(metadata_json)
        # self.metadata_json = {}
        # for row in metadata_json:
        #     key, value = row.split(":")
        #     self.metadata_json[key] = value
        # self.metadata_json = {
        #     name: value for name, value in m.split(":") for m in metadata_json
        # }


if __name__ == "__main__":
    Parser = DataParser(".data/4B 109.pf2")
    Parser.parse()