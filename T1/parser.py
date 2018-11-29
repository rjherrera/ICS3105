import pandas as pd


class Parser:

    def __init__(self, file_name):
        self.excel = pd.ExcelFile(file_name)
        self.instances = self.excel.sheet_names

    def parameters_from_sheet_name(self, name):
        dataframe = self.excel.parse(name, header=None)
        n = dataframe.iloc[1, 1]
        B = dataframe.iloc[2, 1]

        dataframe = self.excel.parse(name, header=4, index_col=0)

        weights = dataframe.iloc[:, 1]
        values = dataframe.iloc[:, 0]
        return n, B, list(weights), list(values)

    def parameters_from_sheet_index(self, index):
        return parameters_from_sheet_name(self.excel.sheet_names[index])


if __name__ == '__main__':
    file = 'InstanciasKnapsackSinSolucionFixed.xlsx'
    p = Parser(file)
    print(p.instances)
    print(p.parameters_from_sheet_name('Fácil'))