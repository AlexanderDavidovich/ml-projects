# simple_distances.py
import pickle, math, csv, sys, itertools

R = 6371.0088  # км

def haversine_km(p1, p2):
    lat1, lon1 = map(math.radians, p1)
    lat2, lon2 = map(math.radians, p2)
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(a))

inp, out = sys.argv[1], sys.argv[2]  # входной .pkl и выходной .csv

cities = pickle.load(open(inp, "rb"))  # {'Город': (lat, lon), ...}

with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["city1", "city2", "distance_km"])
    for c1, c2 in itertools.combinations(sorted(cities), 2):
        w.writerow([c1, c2, f"{haversine_km(cities[c1], cities[c2]):.3f}"])
