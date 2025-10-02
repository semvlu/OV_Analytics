import duckdb
import os
import math

os.chdir("../data/warehouse")

tab = duckdb.read_parquet("*.parquet")

tab.show()
for i in range(len(tab.columns)):
    print(tab.description[i][0], tab.description[i][1])


con = duckdb.connect()
result = con.execute("""
    SELECT lineplanningnumber, journeynumber, COUNT(vehiclenumber) as active_buses, rd_x, rd_y,  straight_line_distance
    FROM '*.parquet'
    WHERE lineplanningnumber IS NOT NULL
    GROUP BY lineplanningnumber, journeynumber, rd_x, rd_y, straight_line_distance
""").fetchdf()

print("--------------------------------")
print(result)
print("--------------------------------")
specline = result[result['lineplanningnumber'] == 19]
print(specline)

bus1 = float(specline.iloc[0]['rd_x']) if specline.iloc[0]['rd_x'] != '' else 0.0, \
        float(specline.iloc[0]['rd_y']) if specline.iloc[0]['rd_y'] != '' else 0.0

bus2 = float(specline.iloc[1]['rd_x']) if specline.iloc[1]['rd_x'] != '' else 0.0, \
        float(specline.iloc[1]['rd_y']) if specline.iloc[1]['rd_y'] != '' else 0.0

def dist(x1, y1, x2, y2):
    return round(math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)), 2)

print(dist(bus1[0], bus1[1], bus2[0], bus2[1]), "m")