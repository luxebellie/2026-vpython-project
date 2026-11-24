Web VPython 3.2

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
selected_country = ""

bigben_pos = get_position(51.5007,-0.1246)
bigben_up = norm(bigben_pos)
bigben_side = vec(cos(radians(-0.1246)),0,-sin(radians(-0.1246)))
bigben_front = norm(cross(bigben_side,bigben_up))

b1 = box(pos=bigben_pos+bigben_up*0.5,size=vec(2.5,0.7,2.5),axis=bigben_side,up=bigben_up,color=vec(0.48,0.38,0.27))
b2 = box(pos=bigben_pos+bigben_up*3.1,size=vec(1.9,5,1.9),axis=bigben_side,up=bigben_up,color=vec(0.78,0.68,0.53))
b3 = box(pos=bigben_pos+bigben_up*5.7,size=vec(2.1,0.5,2.1),axis=bigben_side,up=bigben_up,color=vec(0.65,0.53,0.39))
b4 = box(pos=bigben_pos+bigben_up*6.5,size=vec(1.8,1.2,1.8),axis=bigben_side,up=bigben_up,color=vec(0.78,0.68,0.53))
b5 = pyramid(pos=bigben_pos+bigben_up*7.7,axis=bigben_up*1.8,up=bigben_side,size=vec(2.1,2.1,2.1),color=vec(0.28,0.32,0.3))
b6 = cone(pos=bigben_pos+bigben_up*9.5,axis=bigben_up*1.3,radius=0.16,color=vec(0.65,0.53,0.39))

clock1 = cylinder(pos=bigben_pos+bigben_up*4.1+bigben_front*0.98,axis=bigben_front*0.12,radius=0.72,color=vec(0.75,0.58,0.22))
clock2 = cylinder(pos=bigben_pos+bigben_up*4.1+bigben_front*1.11,axis=bigben_front*0.06,radius=0.62,color=color.white)

bigben_dots = []

for i in range(12):
    angle = 2*pi*i/12
    p = bigben_pos+bigben_up*(4.1+0.49*cos(angle))+bigben_side*(0.49*sin(angle))+bigben_front*1.2
    dot1 = sphere(pos=p,radius=0.035,color=color.black)
    bigben_dots.append(dot1)

number12 = label(pos=bigben_pos+bigben_up*4.65+bigben_front*1.2,text="XII",height=8,color=color.black,box=False,opacity=0)
number3 = label(pos=bigben_pos+bigben_up*4.1+bigben_side*0.48+bigben_front*1.2,text="III",height=8,color=color.black,box=False,opacity=0)
number6 = label(pos=bigben_pos+bigben_up*3.58+bigben_front*1.2,text="VI",height=8,color=color.black,box=False,opacity=0)
number9 = label(pos=bigben_pos+bigben_up*4.1-bigben_side*0.48+bigben_front*1.2,text="IX",height=8,color=color.black,box=False,opacity=0)

hour_hand = box(pos=bigben_pos+bigben_up*4.1+bigben_front*1.23,size=vec(0.07,0.32,0.035),axis=bigben_up,up=bigben_side,color=color.black)
minute_hand = box(pos=bigben_pos+bigben_up*4.1+bigben_front*1.24,size=vec(0.07,0.45,0.035),axis=bigben_side,up=bigben_up,color=color.black)
clock_center = sphere(pos=bigben_pos+bigben_up*4.1+bigben_front*1.28,radius=0.07,color=vec(0.7,0.55,0.2))

bigben_name = label(pos=bigben_pos+bigben_up*11,text="BIG BEN",color=color.white,height=10,box=False,opacity=0)

for obj in [b1,b2,b3,b4,b5,b6,clock1,clock2,hour_hand,minute_hand,clock_center]:
    obj.visible = False

for obj in bigben_dots:
    obj.visible = False

for obj in [number12,number3,number6,number9,bigben_name]:
    obj.visible = False


korea_pos = get_position(37.5596,126.9753)
korea_up = norm(korea_pos)
korea_side = vec(cos(radians(126.9753)),0,-sin(radians(126.9753)))
korea_front = norm(cross(korea_side,korea_up))

k1 = box(pos=korea_pos+korea_up*0.15,size=vec(2.4,0.2,1.7),axis=korea_side,up=korea_up,color=vec(0.7,0.68,0.62))
k2 = box(pos=korea_pos+korea_up*0.7,size=vec(1.9,0.7,1.2),axis=korea_side,up=korea_up,color=vec(0.65,0.22,0.12))
k3 = pyramid(pos=korea_pos+korea_up*1.2,size=vec(0.65,2.5,1.8),axis=korea_up,color=vec(0.12,0.18,0.16))
k4 = box(pos=korea_pos+korea_up*1.55,size=vec(1.6,0.4,1.0),axis=korea_side,up=korea_up,color=vec(0.65,0.22,0.12))
k5 = pyramid(pos=korea_pos+korea_up*1.9,size=vec(0.55,2.1,1.5),axis=korea_up,color=vec(0.1,0.16,0.15))

korea_parts = [k1,k2,k3,k4,k5]

for x in [-0.8,0,0.8]:
    for z in [-0.5,0.5]:
        p = cylinder(pos=korea_pos+korea_up*0.35+korea_side*x+korea_front*z,axis=korea_up*0.7,radius=0.045,color=vec(0.5,0.16,0.1))
        korea_parts.append(p)

korea_name = label(pos=korea_pos+korea_up*2.5,text="SUNGNYEMUN",color=color.white,height=7,box=False,opacity=0)

for obj in korea_parts:
    obj.visible = False

korea_name.visible = False


china_pos = get_position(40.4319,116.5704)
china_up = norm(china_pos)
china_side = vec(cos(radians(116.5704)),0,-sin(radians(116.5704)))
china_front = norm(cross(china_side,china_up))

china_parts = []

z_list = [0,0.7,1.5,2.2,2.8,3.4,3.9,4.3,4.7,4.9,5.0,5.0,4.8,4.6,4.3,3.9,3.4,2.8,2.2,1.4,0.7,-0.1,-0.8,-1.6,-2.3,-2.9,-3.5,-4.0,-4.4,-4.7,-4.9,-5.0,-5.0,-4.8,-4.5,-4.1,-3.7,-3.1,-2.5,-1.8,-1.1,-0.3,0.4,1.2,1.9,2.6,3.2,3.7,4.2,4.5,4.8,5.0,5.0,4.9,4.7,4.4,4.0,3.6,3.0,2.4]

y_list = [0,0.2,0.5,0.7,0.9,1.1,1.3,1.5,1.6,1.8,1.9,1.9,2.0,2.0,2.0,1.9,1.9,1.8,1.6,1.5,1.3,1.1,0.9,0.7,0.5,0.2,0.0,-0.2,-0.5,-0.7,-0.9,-1.1,-1.3,-1.5,-1.6,-1.8,-1.9,-1.9,-2.0,-2.0,-2.0,-1.9,-1.9,-1.8,-1.6,-1.5,-1.3,-1.1,-0.9,-0.7,-0.5,-0.2,0.0,0.2,0.5,0.7,0.9,1.1,1.3,1.5]

for i in range(60):
    x = (i-30)*0.3
    y = y_list[i]*0.3
    z = z_list[i]*0.3

    wall = box(pos=china_pos+china_up*(y+0.375)+china_side*x+china_front*z,size=vec(0.42,0.75,0.54),axis=china_side,up=china_up,color=vec(0.74,0.70,0.65))
    china_parts.append(wall)

    if i % 2 == 0:
        top1 = box(pos=china_pos+china_up*(y+0.795)+china_side*x+china_front*(z+0.225),size=vec(0.21,0.105,0.066),axis=china_side,up=china_up,color=vec(0.65,0.63,0.58))
        top2 = box(pos=china_pos+china_up*(y+0.795)+china_side*x+china_front*(z-0.225),size=vec(0.21,0.105,0.066),axis=china_side,up=china_up,color=vec(0.65,0.63,0.58))
        china_parts.extend([top1,top2])

    if i % 15 == 7:
        tower1 = box(pos=china_pos+china_up*(y+0.56)+china_side*x+china_front*z,size=vec(0.84,1.125,0.84),axis=china_side,up=china_up,color=vec(0.58,0.56,0.52))
        tower2 = box(pos=china_pos+china_up*(y+1.125)+china_side*x+china_front*z,size=vec(0.93,0.09,0.93),axis=china_side,up=china_up,color=vec(0.45,0.43,0.40))
        china_parts.extend([tower1,tower2])

china_name = label(pos=china_pos+china_up*2.5,text="GREAT WALL OF CHINA",color=color.white,height=6,box=False,opacity=0)

for obj in china_parts:
    obj.visible = False

china_name.visible = False


russia_pos = get_position(55.7520,37.6175)
russia_up = norm(russia_pos)
russia_side = vec(cos(radians(37.6175)),0,-sin(radians(37.6175)))
russia_front = norm(cross(russia_side,russia_up))

red_brick = vec(0.72,0.18,0.15)
white_trim = vec(0.92,0.92,0.92)
green_roof = vec(0.12,0.45,0.25)
gold = vec(0.95,0.78,0.15)

russia_parts = []

r1 = box(pos=russia_pos+russia_up*3.0,size=vec(3.2,6.0,3.2),axis=russia_side,up=russia_up,color=red_brick)
r2 = box(pos=russia_pos+russia_up*0.6+russia_front*1.62,size=vec(1.2,1.2,0.1),axis=russia_side,up=russia_up,color=color.black)

russia_parts.extend([r1,r2])

for y in [2.0,4.2,6.0]:
    trim = box(pos=russia_pos+russia_up*y,size=vec(3.45,0.25,3.45),axis=russia_side,up=russia_up,color=white_trim)
    russia_parts.append(trim)

for x,z in [(-1.35,-1.35),(1.35,-1.35),(-1.35,1.35),(1.35,1.35)]:
    column = cylinder(pos=russia_pos+russia_up*6.2+russia_side*x+russia_front*z,axis=russia_up*1.4,radius=0.22,color=red_brick)
    roof = cone(pos=russia_pos+russia_up*7.6+russia_side*x+russia_front*z,axis=russia_up*1.1,radius=0.26,color=green_roof)
    russia_parts.extend([column,roof])

for z in [-1.62,1.62]:
    clock = sphere(pos=russia_pos+russia_up*5.1+russia_front*z,radius=0.65,color=color.black)
    clock_ring = ring(pos=russia_pos+russia_up*5.1+russia_front*z,axis=russia_front,radius=0.65,thickness=0.07,color=gold)
    russia_parts.extend([clock,clock_ring])

for x in [-1.62,1.62]:
    clock = sphere(pos=russia_pos+russia_up*5.1+russia_side*x,radius=0.65,color=color.black)
    clock_ring = ring(pos=russia_pos+russia_up*5.1+russia_side*x,axis=russia_side,radius=0.65,thickness=0.07,color=gold)
    russia_parts.extend([clock,clock_ring])

r3 = box(pos=russia_pos+russia_up*6.8,size=vec(2.2,1.4,2.2),axis=russia_side,up=russia_up,color=red_brick)
r4 = box(pos=russia_pos+russia_up*7.55,size=vec(2.4,0.2,2.4),axis=russia_side,up=russia_up,color=white_trim)
r5 = cylinder(pos=russia_pos+russia_up*7.65,axis=russia_up*1.1,radius=0.85,color=white_trim)
r6 = pyramid(pos=russia_pos+russia_up*8.75,size=vec(3.5,1.6,1.6),axis=russia_up,color=green_roof)
r7 = cylinder(pos=russia_pos+russia_up*12.25,axis=russia_up*1.1,radius=0.06,color=gold)
r8 = sphere(pos=russia_pos+russia_up*13.5,radius=0.25,color=color.red,emissive=True)

russia_parts.extend([r3,r4,r5,r6,r7,r8])

russia_name = label(pos=russia_pos+russia_up*14.5,text="SPASSKAYA TOWER",color=color.white,height=9,box=False,opacity=0)

for obj in russia_parts:
    obj.visible = False

russia_name.visible = False


sky_pos = get_position(-36.8485,174.7633)
sky_up = norm(sky_pos)

concrete = vec(0.85,0.85,0.85)
dark_gray = vec(0.45,0.45,0.45)
glass_blue = vec(0.2,0.55,0.8)
spire_red = vec(0.85,0.2,0.2)

sky_parts = []

s1 = cylinder(pos=sky_pos,axis=sky_up*14,radius=0.45,color=concrete)
s2 = cylinder(pos=sky_pos+sky_up*11,axis=sky_up*1.2,radius=1.25,color=glass_blue)
s3 = cylinder(pos=sky_pos+sky_up*12.2,axis=sky_up*0.2,radius=1.35,color=concrete)
s4 = cone(pos=sky_pos+sky_up*12.4,axis=sky_up*1.0,radius=1.25,color=dark_gray)
s5 = ring(pos=sky_pos+sky_up*11.6,axis=sky_up,radius=1.35,thickness=0.06,color=concrete)
s6 = cylinder(pos=sky_pos+sky_up*14,axis=sky_up*2.5,radius=0.2,color=concrete)
s7 = cone(pos=sky_pos+sky_up*16.5,axis=sky_up*4.0,radius=0.2,color=spire_red)
s8 = sphere(pos=sky_pos+sky_up*18.2,radius=0.18,color=color.red,emissive=True)

sky_parts = [s1,s2,s3,s4,s5,s6,s7,s8]

sky_name = label(pos=sky_pos+sky_up*19.5,text="SKY TOWER",color=color.white,height=9,box=False,opacity=0)

for obj in sky_parts:
    obj.visible = False

sky_name.visible = False



tokyo_pos = get_position(35.6586,139.7454)
tokyo_up = norm(tokyo_pos)
tokyo_side = vec(cos(radians(139.7454)),0,-sin(radians(139.7454)))
tokyo_front = norm(cross(tokyo_side,tokyo_up))

tokyo_red = vec(0.85,0.12,0.08)
tokyo_white = vec(0.92,0.92,0.88)
tokyo_parts = []

def tokyo_point(x,y,z):
    return tokyo_pos + tokyo_side*x + tokyo_up*y + tokyo_front*z

def add_tokyo_rod(x1,y1,z1,x2,y2,z2,r,c):
    p1 = tokyo_point(x1,y1,z1)
    p2 = tokyo_point(x2,y2,z2)
    obj = cylinder(pos=p1,axis=p2-p1,radius=r,color=c)
    tokyo_parts.append(obj)

tokyo_base = box(pos=tokyo_point(0,0.15,0),size=vec(5,0.3,5),axis=tokyo_side,up=tokyo_up,color=vec(0.45,0.43,0.4))
tokyo_parts.append(tokyo_base)

tokyo_levels = [0.3,2,4,6,8,10,12,14]
tokyo_widths = [2.1,1.85,1.55,1.25,0.95,0.7,0.45,0.2]

for i in range(7):
    a = tokyo_widths[i]
    b = tokyo_widths[i+1]
    y1 = tokyo_levels[i]
    y2 = tokyo_levels[i+1]

    for sx in [-1,1]:
        for sz in [-1,1]:
            c = tokyo_red if i%2 == 0 else tokyo_white
            add_tokyo_rod(sx*a,y1,sz*a,sx*b,y2,sz*b,0.14,c)

    for sz in [-1,1]:
        add_tokyo_rod(-a,y1,sz*a,b,y2,sz*b,0.055,tokyo_white)
        add_tokyo_rod(a,y1,sz*a,-b,y2,sz*b,0.055,tokyo_white)

    for sx in [-1,1]:
        add_tokyo_rod(sx*a,y1,-a,sx*b,y2,b,0.055,tokyo_white)
        add_tokyo_rod(sx*a,y1,a,sx*b,y2,-b,0.055,tokyo_white)

for i in range(1,7):
    w = tokyo_widths[i]
    y = tokyo_levels[i]
    c = tokyo_white if i%2 == 0 else tokyo_red

    for z in [-w,w]:
        add_tokyo_rod(-w,y,z,w,y,z,0.08,c)

    for x in [-w,w]:
        add_tokyo_rod(x,y,-w,x,y,w,0.08,c)

tokyo_deck1 = box(pos=tokyo_point(0,8,0),size=vec(2.4,0.35,2.4),axis=tokyo_side,up=tokyo_up,color=tokyo_white)
tokyo_parts.append(tokyo_deck1)

tokyo_deck2 = box(pos=tokyo_point(0,12,0),size=vec(1.3,0.3,1.3),axis=tokyo_side,up=tokyo_up,color=tokyo_white)
tokyo_parts.append(tokyo_deck2)

for sx in [-1,1]:
    for sz in [-1,1]:
        add_tokyo_rod(sx*0.65,8,sz*0.65,sx*0.65,8.5,sz*0.65,0.06,tokyo_red)
        add_tokyo_rod(sx*0.35,12,sz*0.35,sx*0.35,12.4,sz*0.35,0.05,tokyo_red)

add_tokyo_rod(0,14,0,0,15,0,0.09,tokyo_red)
add_tokyo_rod(0,15,0,0,16,0,0.06,tokyo_white)
add_tokyo_rod(0,16,0,0,17,0,0.035,tokyo_red)

tokyo_name = label(pos=tokyo_point(0,18,0),text="TOKYO TOWER",color=color.white,height=10,box=False,opacity=0)

liberty_pos = get_position(40.6892,-74.0445)
liberty_up = norm(liberty_pos)
liberty_side = vec(cos(radians(-74.0445)),0,-sin(radians(-74.0445)))
liberty_front = norm(cross(liberty_side,liberty_up))

liberty_green = vec(0.25,0.55,0.43)
liberty_parts = []

lp1 = box(pos=liberty_pos+liberty_up*0.5,size=vec(3.8,1.0,3.8),axis=liberty_side,up=liberty_up,color=vec(0.55,0.48,0.38))
lp2 = box(pos=liberty_pos+liberty_up*1.3,size=vec(3.0,0.7,3.0),axis=liberty_side,up=liberty_up,color=vec(0.62,0.55,0.43))
lp3 = box(pos=liberty_pos+liberty_up*2.0,size=vec(2.4,0.7,2.4),axis=liberty_side,up=liberty_up,color=vec(0.62,0.55,0.43))
liberty_parts.extend([lp1,lp2,lp3])

liberty_body = cone(pos=liberty_pos+liberty_up*2.3,axis=liberty_up*3.0,radius=0.9,color=liberty_green)
liberty_neck = cylinder(pos=liberty_pos+liberty_up*5.0,axis=liberty_up*0.45,radius=0.32,color=liberty_green)
liberty_head = sphere(pos=liberty_pos+liberty_up*5.7,radius=0.48,color=liberty_green)
liberty_parts.extend([liberty_body,liberty_neck,liberty_head])

liberty_crown = cone(pos=liberty_pos+liberty_up*6.0,axis=liberty_up*0.65,radius=0.55,color=liberty_green)
liberty_parts.append(liberty_crown)

for i in range(7):
    angle = 2*pi*i/7
    crown_spike = cylinder(pos=liberty_pos+liberty_up*6.35+liberty_side*(0.42*cos(angle))+liberty_front*(0.42*sin(angle)),axis=liberty_up*0.65,radius=0.055,color=liberty_green)
    liberty_parts.append(crown_spike)

liberty_arm = cylinder(pos=liberty_pos+liberty_up*4.7+liberty_side*0.55,axis=liberty_up*1.8+liberty_side*0.65,radius=0.18,color=liberty_green)
liberty_parts.append(liberty_arm)

liberty_torch = cylinder(pos=liberty_pos+liberty_up*6.3+liberty_side*1.2,axis=liberty_up*0.65,radius=0.13,color=gold)
liberty_flame = cone(pos=liberty_pos+liberty_up*6.95+liberty_side*1.2,axis=liberty_up*0.65,radius=0.25,color=vec(0.95,0.65,0.15))
liberty_parts.extend([liberty_torch,liberty_flame])

liberty_tablet = box(pos=liberty_pos+liberty_up*4.1-liberty_side*0.75+liberty_front*0.35,size=vec(0.65,1.1,0.18),axis=liberty_side,up=liberty_up,color=liberty_green)
liberty_parts.append(liberty_tablet)

liberty_name = label(pos=liberty_pos+liberty_up*8.0,text="STATUE OF LIBERTY",color=color.white,height=9,box=False,opacity=0)

for obj in liberty_parts:
    obj.visible = False

liberty_name.visible = False


for name,lat,lon in countries:
    pos = get_position(lat,lon)
    country_label = label(pos=pos,text=name,color=color.white,height=8,box=False,opacity=0)
    marker = box(pos=pos,size=vec(len(name),1,1),color=color.white,opacity=0.1)
    labels.append((country_label,pos,marker,name))


def country_clicked(evt):
    global selected_country
    picked = scene.mouse.pick

    for country_label,pos,marker,name in labels:
        if picked == marker:
            selected_country = name
            scene.caption = name+" 선택!"


scene.bind("click",country_clicked)


while True:
    rate(60)

    view_dir = norm(scene.camera.pos-earth.pos)

    for country_label,pos,marker,name in labels:
        front = dot(norm(pos),view_dir)>0
        country_label.visible = front
        marker.visible = front

    show_bigben = selected_country == "UNITED KINGDOM" and dot(bigben_up,view_dir)>0

    for obj in [b1,b2,b3,b4,b5,b6,clock1,clock2,hour_hand,minute_hand,clock_center]:
        obj.visible = show_bigben

    for obj in bigben_dots:
        obj.visible = show_bigben

    for obj in [number12,number3,number6,number9,bigben_name]:
        obj.visible = show_bigben


    show_tokyo = selected_country == "JAPAN" and dot(tokyo_up,view_dir)>0

    for obj in tokyo_parts:
        obj.visible = show_tokyo

    tokyo_name.visible = show_tokyo

    show_liberty = selected_country == "UNITED STATES" and dot(liberty_up,view_dir)>0

    for obj in liberty_parts:
        obj.visible = show_liberty

    liberty_name.visible = show_liberty

    show_korea = selected_country == "SOUTH KOREA" and dot(korea_up,view_dir)>0

    for obj in korea_parts:
        obj.visible = show_korea

    korea_name.visible = show_korea

    show_china = selected_country == "CHINA" and dot(china_up,view_dir)>0

    for obj in china_parts:
        obj.visible = show_china

    china_name.visible = show_china

    show_russia = selected_country == "RUSSIA" and dot(russia_up,view_dir)>0

    for obj in russia_parts:
        obj.visible = show_russia

    russia_name.visible = show_russia

    show_sky = selected_country == "NEW ZEALAND" and dot(sky_up,view_dir)>0

    for obj in sky_parts:
        obj.visible = show_sky

    sky_name.visible = show_sky
