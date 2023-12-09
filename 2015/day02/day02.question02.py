total_area=0
file = open('input', 'r')
lines = file.readlines()
for line in lines:
    l, w, h = line.split('x')
    l=int(l)
    w=int(w)
    h=int(h)
    wrap=min((l+w),(w+h),(h+l)) * 2
    bow=l*w*h
    total_area=total_area+wrap+bow
print(total_area)
