import duckdb
import os
import math

os.chdir("../data/lake/")

tab = duckdb.read_parquet("part-00000-21f0573e-fa95-421d-9b8f-46b811121441-c000.snappy.parquet")

tab.show()
for i in range(len(tab.columns)):
    print(tab.description[i][0], tab.description[i][1])

'''
con = duckdb.connect()
result = con.execute("""
    SELECT lineplanningnumber, journeynumber, COUNT(vehiclenumber) as active_buses, rd_x, rd_y,  straight_line_distance
    FROM '*.parquet'
    WHERE lineplanningnumber IS NOT NULL
    GROUP BY lineplanningnumber, journeynumber, rd_x, rd_y, straight_line_distance
""").fetchdf()
'''
