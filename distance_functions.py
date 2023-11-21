from math import pi,cos,sin,sqrt,atan2,degrees,radians,floor,atan
rad = 6372795
def get_distance(lat1,long1, lat2, long2):
    
    lat1 = lat1*pi/180.
    lat2 = lat2*pi/180.
    long1 = long1*pi/180.
    long2 = long2*pi/180.
    #косинусы и синусы широт и разницы долгот
    cl1 = cos(lat1)
    cl2 = cos(lat2)
    sl1 = sin(lat1)
    sl2 = sin(lat2)
    delta = long2 - long1
    cdelta = cos(delta)
    sdelta = sin(delta)

    #вычисления длины большого круга
    y = sqrt(pow(cl2*sdelta,2)+pow(cl1*sl2-sl1*cl2*cdelta,2))
    x = sl1*sl2+cl1*cl2*cdelta
    ad = atan2(y,x)
    dist = ad*rad

    #вычисление начального азимута
    # x = (cl1*sl2) - (sl1*cl2*cdelta)
    # y = sdelta*cl2
    # z = degrees(atan(-y/x))

    # if (x < 0):
    #     z = z+180.

    # z2 = (z+180.) % 360. - 180.
    # z2 = - radians(z2)
    # anglerad2 = z2 - ((2*pi)*floor((z2/(2*pi))) )
    # angledeg = (anglerad2*180.)/pi
    
    dist/=1000
    return dist