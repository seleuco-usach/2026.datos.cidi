

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
from gspread_dataframe import set_with_dataframe

# Configurar el alcance y credenciales
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/xenomorfo/Descargas/bamboo-sweep-465617-i4-06b9bd6f36a5.json', scope)
client = gspread.authorize(credentials)
#jose-hoyos-usach-cl@bamboo-sweep-465617-i4.iam.gserviceaccount.com 
#https://docs.google.com/spreadsheets/d/17LhWP9zmDMxmyqkmlB-PTc8kf7_p6LcFHdCGAhEvi9E/edit?gid=1818427118#gid=1818427118
# Abrir la hoja de cálculo por ID

#https://docs.google.com/spreadsheets/d/1r1nsHibT3kCTnSPhiPxOOZU3-pIP5oq5kfLi6pYE-os/edit?gid=218228292#gid=218228292
spreadsheet = client.open_by_key('1r1nsHibT3kCTnSPhiPxOOZU3-pIP5oq5kfLi6pYE-os')

# Abrir la hoja de cálculo por ID


cidi = (
gspread.authorize(credentials)
.open_by_key('1r1nsHibT3kCTnSPhiPxOOZU3-pIP5oq5kfLi6pYE-os')
.worksheet("cidi")
.get_all_values())



cidi = pd.DataFrame(cidi[1:], columns=cidi[0])

cidi.to_csv("tabla_cidi.csv", index=False)

cidi_rev = (
gspread.authorize(credentials)
.open_by_key('1r1nsHibT3kCTnSPhiPxOOZU3-pIP5oq5kfLi6pYE-os')
.worksheet("rev_")
.get_all_values())



cidi = pd.DataFrame(cidi_rev[1:], columns=cidi_rev[0])

cidi.to_csv("tabla_cidi_rev.csv", index=False)