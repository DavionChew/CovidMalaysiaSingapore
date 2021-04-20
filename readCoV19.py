import numpy as np
import pandas as pd
from wikisearch import GetLatestMalaysiaData_func, GetLatestSingaporeData_func


def Compare_LatestTotalCase(curr_TotalMalaysia, currTotalSingapore):
    lastest_totalMy = int(GetLatestMalaysiaData_func())
    lastest_totalSg = int(GetLatestSingaporeData_func())
    newIncreaseMy = lastest_totalMy - curr_TotalMalaysia
    newIncreaseSg = lastest_totalSg - currTotalSingapore

    if (lastest_totalMy > curr_TotalMalaysia) and (lastest_totalSg > currTotalSingapore):
        lastest_arr = np.array([[lastest_totalMy, lastest_totalSg, newIncreaseMy, newIncreaseSg]])
        lastest_df = pd.DataFrame(csv)
        lastest_arr = pd.DataFrame(lastest_arr)
        lastest_arr.columns = ['Malaysia', 'Singapore', 'New Case in My', 'New Case in Sg']
        result = lastest_df.append(lastest_arr, ignore_index = True, sort=False)

        print(result.tail(2))

        result.to_csv('file_name.csv', mode = 'w', index=False, na_rep='Unknown', encoding='utf-8')
    else:
        print("Latest Total Cases: ", lastest_totalMy, ' ', lastest_totalSg)
        print("Latest New Cases: ", newIncreaseMy, ' ', newIncreaseSg)

csv= pd.read_csv("E:\\Users\\ChewDK\\Documents\\Selenium\\CoV_19.csv")
last_df = csv.tail(1)
curr_arr = np.array(last_df)
print(curr_arr[0])

curr_TotalMalaysia = int(curr_arr[0][0])
print(curr_TotalMalaysia)

currTotalSingapore = int(curr_arr[0][1])
print(currTotalSingapore)

#lastest_df = csv
Compare_LatestTotalCase(curr_TotalMalaysia, currTotalSingapore)