#Universal Gravitation
def universal_gravitation(mass1,mass2,radius,grav = 6.67 * (10**-11)):
    print("G =", str(grav) + "\n")
    return grav * ((mass1*mass2)/(radius^2))
