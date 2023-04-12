p1=float(input("digite sua nota da p1"))
p2=float(input("digite sua nota da p2"))
m = (p1 + p2*2)/3
print("sua média é {:.2f}".format(m))
if m < 5:
    print("você está de dp")
elif m >= 5:
    print("você passou, parabéns")
