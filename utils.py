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
    frame = pd.read_excel(excelpath)
    sheet_names = frame.sheet_names
    all_sheets = dict()
    for s in sheet_names:
        df = pd.read_excel('path/to/excel/file.xlsx', sheet_name='Sheet1')
        type_list = []
        k_list = []
        isovalue_list = []
        posx_list = []
        posy_list = []


if __name__ == '__main__':
    pass



