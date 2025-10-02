from pyproj import Transformer
import requests


loc1 = (122242, 484390)
loc2 = (120928, 492225)

# Define transformer: RD -> WGS84
rd_to_wgs84 = Transformer.from_crs("EPSG:28992", "EPSG:4326", always_xy=True)

loc1 = rd_to_wgs84.transform(loc1[0], loc1[1])
loc2 = rd_to_wgs84.transform(loc2[0], loc2[1])




url = f"http://router.project-osrm.org/route/v1/driving/{loc1[0]},{loc1[1]};{loc2[0]},{loc2[1]}?overview=false"
resp = requests.get(url).json()


t = resp["routes"][0]["duration"]
print("%.2f min" %(t/60))

dist = resp["routes"][0]["distance"]
if dist < 1000:
    print(dist, "meters")
else:
    print("%.2f km " %(dist/1000))
