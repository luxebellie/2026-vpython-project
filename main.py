earth = sphere(texture=textures.earth, radius=90)

def get_position(lat, lon):
    lat = radians(lat)
    lon = radians(lon)
    r = 91
    x = r * cos(lat) * sin(lon)
    y = r * sin(lat)
    z = r * cos(lat) * cos(lon)
    return vector(x, y, z)
    
countries = [("AFGHANISTAN", 33.94, 67.71),("ALBANIA", 41.15, 20.17),("ALGERIA", 28.03, 1.66),("ANDORRA", 42.55, 1.60),("ANGOLA", -11.20, 17.87),("ANTIGUA AND BARBUDA", 17.06, -61.80),
             ("ARGENTINA", -38.42, -63.62),("ARMENIA", 40.07, 45.04),("AUSTRALIA", -25.27, 133.78),("AUSTRIA", 47.52, 14.55),("AZERBAIJAN", 40.14, 47.58),("BAHAMAS", 25.03, -77.40),
             ("BAHRAIN", 25.93, 50.64),("BANGLADESH", 23.68, 90.36),("BARBADOS", 13.19, -59.54),("BELARUS", 53.71, 27.95),("BELGIUM", 50.50, 4.47),("BELIZE", 17.19, -88.50),("BENIN", 9.31, 2.32),
             ("BHUTAN", 27.51, 90.43),("BOLIVIA", -16.29, -63.59),("BOSNIA AND HERZEGOVINA", 43.92, 17.68),("BOTSWANA", -22.33, 24.68),("BRAZIL", -14.24, -51.93),("BRUNEI", 4.54, 114.73),("BULGARIA", 42.73, 25.49),
             ("BURKINA FASO", 12.24, -1.56),("BURUNDI", -3.37, 29.92),("CABO VERDE", 16.00, -24.01),("CAMBODIA", 12.57, 104.99),("CAMEROON", 7.37, 12.35),("CANADA", 56.13, -106.35),
             ("CENTRAL AFRICAN REPUBLIC", 6.61, 20.94),("CHAD", 15.45, 18.73),("CHILE", -35.68, -71.54),("CHINA", 35.86, 104.20),("COLOMBIA", 4.57, -74.30),("COMOROS", -11.88, 43.87),
             ("COSTA RICA", 9.75, -83.75),("CROATIA", 45.10, 15.20),("CUBA", 21.52, -77.78),("CYPRUS", 35.13, 33.43),("CZECHIA", 49.82, 15.47),("DEMOCRATIC REPUBLIC OF THE CONGO", -4.04, 21.76),
             ("DENMARK", 56.26, 9.50),("DJIBOUTI", 11.83, 42.59),("DOMINICA", 15.41, -61.37),("DOMINICAN REPUBLIC", 18.74, -70.16),("ECUADOR", -1.83, -78.18),("EGYPT", 26.82, 30.80),
             ("EL SALVADOR", 13.79, -88.90),("EQUATORIAL GUINEA", 1.65, 10.27),("ERITREA", 15.18, 39.78),("ESTONIA", 58.60, 25.01),("ESWATINI", -26.52, 31.47),("ETHIOPIA", 9.15, 40.49),("FIJI", -16.58, 179.41),
             ("FINLAND", 61.92, 25.75),("FRANCE", 46.23, 2.21),("GABON", -0.80, 11.61),("GAMBIA", 13.44, -15.31),("GEORGIA", 42.32, 43.36),("GERMANY", 51.17, 10.45),("GHANA", 7.95, -1.02),("GREECE", 39.07, 21.82),
             ("GRENADA", 12.26, -61.60),("GUATEMALA", 15.78, -90.23),("GUINEA", 9.95, -9.70),("GUINEA-BISSAU", 11.80, -15.18),("GUYANA", 4.86, -58.93),("HAITI", 18.97, -72.29),("HONDURAS", 15.20, -86.24),
             ("HUNGARY", 47.16, 19.50),("ICELAND", 64.96, -19.02),("INDIA", 20.59, 78.96),("INDONESIA", -0.79, 113.92),("IRAN", 32.43, 53.69),("IRAQ", 33.22, 43.68),("IRELAND", 53.41, -8.24),("ISRAEL", 31.05, 34.85),
             ("ITALY", 41.87, 12.57),("JAMAICA", 18.11, -77.30),("JAPAN", 36.20, 138.25),("JORDAN", 30.59, 36.24),("KAZAKHSTAN", 48.02, 66.92),("KENYA", -0.02, 37.91),("KIRIBATI", -3.37, -168.73),("KUWAIT", 29.31, 47.48),
             ("KYRGYZSTAN", 41.20, 74.77),("LAOS", 19.86, 102.50),("LATVIA", 56.88, 24.60),("LEBANON", 33.85, 35.86),("LESOTHO", -29.61, 28.23),("LIBERIA", 6.43, -9.43),("LIBYA", 26.34, 17.23),("LIECHTENSTEIN", 47.17, 9.56),
             ("LITHUANIA", 55.17, 23.88),("LUXEMBOURG", 49.82, 6.13),("MADAGASCAR", -18.77, 46.87),("MALAWI", -13.25, 34.30),("MALAYSIA", 4.21, 101.98),("MALDIVES", 3.20, 73.22),("MALI", 17.57, -4.00),
             ("MALTA", 35.94, 14.38),("MARSHALL ISLANDS", 7.13, 171.18),("MAURITANIA", 21.01, -10.94),("MAURITIUS", -20.35, 57.55),("MEXICO", 23.63, -102.55),("MICRONESIA", 7.43, 150.55),("MOLDOVA", 47.41, 28.37),
             ("MONACO", 43.75, 7.41),("MONGOLIA", 46.86, 103.85),("MONTENEGRO", 42.71, 19.37),("MOROCCO", 31.79, -7.09),("MOZAMBIQUE", -18.67, 35.53),("MYANMAR", 21.91, 95.96),("NAMIBIA", -22.96, 18.49),
             ("NAURU", -0.52, 166.93),("NEPAL", 28.39, 84.12),("NETHERLANDS", 52.13, 5.29),("NEW ZEALAND", -40.90, 174.89),("NICARAGUA", 12.87, -85.21),("NIGER", 17.61, 8.08),("NIGERIA", 9.08, 8.68),
             ("NORTH KOREA", 40.34, 127.51),("NORTH MACEDONIA", 41.61, 21.75),("NORWAY", 60.47, 8.47),("OMAN", 21.51, 55.92),("PAKISTAN", 30.38, 69.35),("PALAU", 7.51, 134.58),("PALESTINE", 31.95, 35.23),
             ("PANAMA", 8.54, -80.78),("PAPUA NEW GUINEA", -6.31, 143.96),("PARAGUAY", -23.44, -58.44),("PERU", -9.19, -75.02),("PHILIPPINES", 12.88, 121.77),("POLAND", 51.92, 19.15),("PORTUGAL", 39.40, -8.22),
             ("QATAR", 25.35, 51.18),("PUBLIC OF THE CONGO", -0.23, 15.83),("ROMANIA", 45.94, 24.97),("RUSSIA", 61.52, 105.32),("RWANDA", -1.94, 29.87),("SAINT KITTS AND NEVIS", 17.36, -62.78),("SAINT LUCIA", 13.91, -60.98),
             ("SAINT VINCENT AND THE GRENADINES", 12.98, -61.29),("SAMOA", -13.76, -172.10),("SAN MARINO", 43.94, 12.46),("SAO TOME AND PRINCIPE", 0.19, 6.61),("SAUDI ARABIA", 23.89, 45.08),("SENEGAL", 14.50, -14.45),
             ("SERBIA", 44.02, 21.01),("SEYCHELLES", -4.68, 55.49),("SIERRA LEONE", 8.46, -11.78),("SINGAPORE", 1.35, 103.82),("SLOVAKIA", 48.67, 19.70),("SLOVENIA", 46.15, 15.00),("SOLOMON ISLANDS", -9.65, 160.16),
             ("SOMALIA", 5.15, 46.20),("SOUTH AFRICA", -30.56, 22.94),("SOUTH KOREA", 35.91, 127.77),("SOUTH SUDAN", 6.88, 31.31),("SPAIN", 40.46, -3.75),("SRI LANKA", 7.87, 80.77),("SUDAN", 12.86, 30.22),
             ("SURINAME", 3.92, -56.03),("SWEDEN", 60.13, 18.64),("SWITZERLAND", 46.82, 8.23),("SYRIA", 34.80, 39.00),("TAJIKISTAN", 38.86, 71.28),("TANZANIA", -6.37, 34.89),("THAILAND", 15.87, 100.99),
             ("TIMOR-LESTE", -8.87, 125.73),("TOGO", 8.62, 0.82),("TONGA", -21.18, -175.20),("TRINIDAD AND TOBAGO", 10.69, -61.22),("TUNISIA", 33.89, 9.54),("TURKEY", 38.96, 35.24),("TURKMENISTAN", 38.97, 59.56),
             ("TUVALU", -7.11, 177.65),("UGANDA", 1.37, 32.29),("UKRAINE", 48.38, 31.17),("UNITED ARAB EMIRATES", 23.42, 53.85),("UNITED KINGDOM", 55.38, -3.44),("UNITED STATES", 37.09, -95.71), 
             ("URUGUAY", -32.52, -55.77),("UZBEKISTAN", 41.38, 64.59),("VANUATU", -15.38, 166.96),("VATICAN CITY", 41.90, 12.45),("VENEZUELA", 6.42, -66.59),("VIETNAM", 14.06, 108.28),
             ("YEMEN", 15.55, 48.52),("ZAMBIA", -13.13, 27.85),("ZIMBABWE", -19.02, 29.15)]

labels = []

def country_clicked(evt):
    picked = scene.mouse.pick

    for country_label, pos, marker, name in labels:
        if picked == marker:
            scene.caption = name + " 선택!"

for name, lat, lon in countries:
    pos = get_position(lat, lon)
    country_label = label(pos=pos,text=name,color=color.white,height=8,box=False,opacity=0)
    marker = box(pos=pos,size=vec(len(name)*1, 1, 1),color=color.white,opacity=0.1)

    labels.append((country_label, pos, marker, name))

scene.bind("click", country_clicked)
    
while True:
    rate(60)
    view_dir = norm(scene.camera.pos - earth.pos)
    for country_label, pos in labels:
        country_label.visible = dot(norm(pos), view_dir) > 0
