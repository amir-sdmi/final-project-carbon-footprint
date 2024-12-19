import pandas as pd

class ExcelReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_input_data(self):
        df = pd.read_excel(self.file_path)
        answers = df['Answers'].values
        answers = [float(answer) for answer in answers] 
        return answers