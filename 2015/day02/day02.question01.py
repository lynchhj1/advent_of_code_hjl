total_area=0
file = open('input', 'r')
lines = file.readlines()
for line in lines:
    l, w, h = line.split('x')
    l=int(l)
    w=int(w)
    h=int(h)
    extra=min((l*w),(w*h),(h*l))
    area=(2*l*w) + (2*w*h) + (2*h*l) + extra
    total_area=total_area+area
print(total_area)
