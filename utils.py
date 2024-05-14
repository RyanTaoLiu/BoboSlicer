import uuid, base64
import pandas as pd

# all unit use mm
inf = 1e8

## utils
def get_uuid():
    # Generate a UUID
    unique_id = uuid.uuid4().bytes
    # Encode the UUID bytes into URL-safe base64 format
    r_uuid = base64.urlsafe_b64encode(unique_id)
    # Decode to string and remove padding characters
    return r_uuid.decode('utf-8').replace('=', '')

def excel2list(excelpath):
    xl = pd.ExcelFile(excelpath)
    sheet_names = xl.sheet_names
    all_sheets = []

    for sn in sheet_names:
        df = pd.read_excel(excelpath, sheet_name=sn)
        excelHeaderList = ['Code', 'Type', 'K', 'IsoValue', 'PosX', 'PosY', 'xPadding', 'yPadding']
        df_dict = df.to_dict(orient='split', index=False)

        assert df_dict['columns'] == excelHeaderList, \
            'Error Excel columns is {}, but need to be {}'.format(str(df_dict['columns']), str(excelHeaderList))
        all_sheets.append(df_dict)
    return sheet_names, all_sheets

if __name__ == '__main__':
    excel2list('TPMS-param.xlsx')



