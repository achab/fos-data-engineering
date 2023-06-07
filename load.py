import folium


def main():
    with open("transformed_data.csv", "r") as f:
        lines = f.readlines()

    # we skip the row that contains column names, this is why we write [1:]
    data = [l.split(",") for l in lines[1:]]

    # we compute the mean coordinates to put it as center of the map
    lat_mean = sum([float(row[1]) for row in data]) / len(data)
    lon_mean = sum([float(row[2]) for row in data]) / len(data)

    m = folium.Map([lat_mean, lon_mean], zoom_start=5)

    # we add marker
    for row in data:
        city, lat, lon, temp, _ = row
        folium.Marker(
            location=[lat, lon],
            popup=f"<p><b>{city}</b><br>{temp}°C</p>",
        ).add_to(m)

    m.save("index.html")


if __name__ == "__main__":
    main()
