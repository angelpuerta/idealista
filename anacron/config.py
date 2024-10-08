from pathlib import Path
import toml 

class Config:
    """Class to hold configuration settings."""
    def __init__(self, periodicity, output_folder):
        self.periodicity = periodicity
        self.output_folder = output_folder

    @classmethod
    def from_toml(cls, config_file):
        """Factory method to create Config instance from TOML file."""
        config_data = toml.load(config_file)
        settings = config_data['settings']
        return cls(
            periodicity=settings['periodicity'],
            output_folder=settings['output_folder']
        )

config = Config.from_toml(Path(__file__).parent.joinpath('config.toml'))