

from gspread_pandas import Spread, Client


def postongdoc(dataframe,username,spreadsheetname,sheetname):
    SPREADSHEET = spreadsheetname
    USER = username
    s = Spread(USER, SPREADSHEET)

    s.df_to_sheet(dataframe, index=False, sheet=sheetname, start='A2', replace=True)
    s.update_cells((1,1), (1,2), ['Created by:', s.email])


# Example
# https://gspread-pandas.readthedocs.io/en/latest/getting_started.html
# from __future__ import print_function
# import pandas as pd
# from gspread_pandas import Spread, Client

# file_name = "http://stats.idre.ucla.edu/stat/data/binary.csv"
# df = pd.read_csv(file_name)

# # 'Example Spreadsheet' needs to already exist and your user must have access to it
# spread = Spread('example_user', 'Example Spreadsheet')
# # This will ask to authenticate if you haven't done so before for 'example_user'

# # Display available worksheets
# spread.sheets

# # Save DataFrame to worksheet 'New Test Sheet', create it first if it doesn't exist
# spread.df_to_sheet(df, index=False, sheet='New Test Sheet', start='A2', replace=True)
# spread.update_cells((1,1), (1,2), ['Created by:', spread.email])
# print(spread)
# # <gspread_pandas.client.Spread - User: '<example_user>@gmail.com', Spread: 'Example Spreadsheet', Sheet: 'New Test Sheet'>

# # You can now first instanciate a Client separately and query folders and
# # instanciate other Spread objects by passing in the Client
# client = Client('example_user')
# # Assumming you have a dir called 'example dir' with sheets in it
# available_sheets = client.find_spreadsheet_files_in_folders('example dir')
# spreads = []
# for sheet in available_sheets.get('example dir', []):
#     spreads.append(Spread(client, sheet['id']))


