import smartsheet
import pandas as pd
import pyodbc
from sqlalchemy import create_engine








class _SysSmartsheetServices:
    """
    A class to interact with Smartsheet API for retrieving, adding, and managing records.
    """

    def __init__(self, api_key):
        """
        Initializes the Smartsheet client with the provided API key.
        
        :param api_key: API key for Smartsheet authentication
        """
        self.smartsheet_client = smartsheet.Smartsheet(api_key)


    def get_column_name_to_id(self, sheet_id):
        """
        Retrieves a mapping of column names to their corresponding column IDs for a given Smartsheet sheet.
        
        :param sheet_id: The unique identifier of the Smartsheet sheet
        :return: Dictionary mapping column names to column IDs, or None in case of an error
        """
        try:
            sheet = self.smartsheet_client.Sheets.get_sheet(sheet_id)
            return {column.title: column.id for column in sheet.columns}
        except Exception as e:
            print(f"Error: {e}")
            return None



    def add_records_to_top_of_smartsheet(self, df, sheet_unique_id):
        """
        Adds records from a pandas DataFrame to a specified Smartsheet 
        sheet by loading records to the top of the sheet.
        
        :param df: DataFrame containing the records to add
        :param sheet_unique_id: The unique identifier of the Smartsheet sheet
        """
        col_ids = self.get_column_name_to_id(sheet_unique_id)
        if col_ids is None:
            print("Failed to retrieve column IDs.")
            return

        new_records = df.astype(str)  # Ensure all values are strings
        new_records_columns = list(new_records.columns)
        df_len = len(new_records)
        counter = 0

        while counter < df_len:
            row_a = smartsheet.models.Row()
            row_a.to_top = True

            for column_name in new_records_columns:
                if column_name in col_ids:
                    row_a.cells.append({
                        'column_id': int(col_ids[column_name]), 
                        'value': new_records.iloc[counter][column_name]
                    })

            response = self.smartsheet_client.Sheets.add_rows(
                sheet_id=sheet_unique_id, list_of_rows=[row_a]
            )

            if response.message == 'SUCCESS':
                print('Rows added successfully')
            else:
                print(f'Error: {response.message}')
            
            counter += 1


    def extract_and_load_to_dataframe_with_row_id(self, sheet_id):
        """
        Extracts data from a Smartsheet sheet and loads it into a pandas DataFrame, including row IDs.
        
        :param sheet_id: The unique identifier of the Smartsheet sheet
        :return: DataFrame containing the sheet data, or None in case of an error
        """
        try:
            sheet = self.smartsheet_client.Sheets.get_sheet(sheet_id, page_size=10000)
            column_headers = [column.title for column in sheet.columns]
            rows = sheet.rows

            data = []
            for row in rows:
                row_data = [row.id]  # Include row ID
                for cell in row.cells:
                    row_data.append(cell.display_value)
                data.append(row_data)

            column_headers.insert(0, "row_id")
            return pd.DataFrame(data, columns=column_headers)
        except Exception as e:
            print(f"Error: {e}")
            return None



    def delete_sheet_data(self, sheet_id):
        """
        Deletes all data (rows) from the specified Smartsheet.

        :param sheet_id: The ID of the Smartsheet to be cleared
        """
        try:
            sheet = self.smartsheet_client.Sheets.get_sheet(sheet_id, page_size=10000)
            row_ids = [row.id for row in sheet.rows]

            if not row_ids:
                print("No rows to delete.")
                return

            batch_size = 100  # Smartsheet API limits batch deletes
            for i in range(0, len(row_ids), batch_size):
                batch = row_ids[i:i+batch_size]
                response = self.smartsheet_client.Sheets.delete_rows(sheet_id, batch)

                if response.message == "SUCCESS":
                    print(f"Deleted {len(batch)} rows successfully.")
                else:
                    print(f"Error deleting rows: {response.message}")

            print("All rows deleted successfully.")
        except Exception as e:
            print(f"Error deleting data from sheet: {e}")



    def refresh_source_data(self, df, sheet_id):
        """
        Deletes all data (rows) from the specified Smartsheet.
        Adds records from a pandas DataFrame to a specified Smartsheet 
        sheet by loading records to the top of the sheet.
        
        :param df: DataFrame containing the records to add
        :param sheet_unique_id: The unique identifier of the Smartsheet sheet

        """

        self.delete_sheet_data(sheet_id)

        self.add_records_to_top_of_smartsheet(df, sheet_id)