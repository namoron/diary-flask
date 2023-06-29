import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 認証情報のパス（JSONファイルのパスを指定してください）
credentials_path = './diary-flask-fd4d4e08aa16.json'

# スコープと認証情報を設定
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)

# Google APIに認証
client = gspread.authorize(credentials)

# 編集するスプレッドシートのキーを指定（スプレッドシートのURLから取得できます）
spreadsheet_key = '1fik2qXLKA1OcbacbH-EmHA4RTSNu666vHC_pRZGJAJU'

# スプレッドシートを開く
spreadsheet = client.open_by_key(spreadsheet_key)

# 編集するワークシートを選択
worksheet = spreadsheet.sheet1

# セルに値を書き込む
worksheet.update_cell(1, 1, 'Hello, World!')

# セルの値を読み込む
cell_value = worksheet.cell(1, 1).value
print(cell_value)
