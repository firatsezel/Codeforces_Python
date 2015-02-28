__author__ = 'forevercode'
#accepted

VenusianGirl = [int(temp) for temp in raw_input().split(" ")]
ThatsMyBoy = [int(temp) for temp in raw_input().split(" ")]

vl = VenusianGirl[0]
vr = VenusianGirl[1]
bl = ThatsMyBoy[0]
br = ThatsMyBoy[1]
bool = None

if vl <= br + 1:
    if br <= 2 * vl + 2:
        bool = True

if vr <= bl + 1 and bool is None:
    if bl <= 2 * vr + 2:
        bool = True

if bool:
    print "YES"
else:
    print "NO"