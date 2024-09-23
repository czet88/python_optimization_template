from dataclasses import dataclass
import os

import pandas as pd

@dataclass
class Input:
    """A class containing all the input information relevant to the solve and to the simulation"""
    data: dict[str, pd.DataFrame]
    """Dictionary containing multiple dataframes with keys as the names of the input csv files"""

    @classmethod
    def load_from_csv_files(cls, root_dir: str) -> "Input":
        """Method to retrieve the data from multiple csv files stored in the same directory"""
        data = {}
        for path, sub_dirs, files in os.walk(root_dir):
            for file_name in files:
                data.update(
                    {
                        file_name.split(sep=".")[0]:
                            pd.read_csv(os.path.join(path, file_name))
                    }
                )
        return cls(data=data)