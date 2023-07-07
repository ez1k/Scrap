from dotenv import dotenv_values
class EnvVariables:
    def __init__(self, env_file_path):
        self.env_vars = dotenv_values(env_file_path)
        self.proxy = self.env_vars.get("PROXY")
        self.input_url = self.env_vars.get("INPUT_URL")
        self.output_file = self.env_vars.get("OUTPUT_FILE")

    def are_defined(self):
        return self.proxy and self.input_url and self.output_file

    def print_values(self):
        if self.are_defined():
            print(f"Proxy: {self.proxy}")
            print(f"Input URL: {self.input_url}")
            print(f"Output File: {self.output_file}")
        else:
            print("Niektóre zmienne środowiskowe nie zostały zdefiniowane.")