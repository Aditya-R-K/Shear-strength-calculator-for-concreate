import pandas as pd


def retrive_value_from_xlsxandcsv(path,row,column):
    try:
        xl = pd.ExcelFile(path)
        df = xl.parse('Sheet1')
        try:
            retrived_value = df.iat[row, column]
            return retrived_value
        except IndexError:
            return 0
    except ValueError:
        df = pd.read_csv(path)
        try:
            retrived_value = df.iat[row, column]
            return retrived_value
        except IndexError:
            return 0
    except Exception:
        return 0
    except TypeError:
        return 0