#Revolutions per minute to meters per second
def rpm_to_mps(rpm,radius):
    print("RPM =",rpm)
    print("r =", radius)
    #Calculate the circumference
    circum = radius * 2 * 3.14
    print("C =", circum)

    #Calculate the meters per minute
    mpm = rpm * circum
    print("MPM =", mpm)

    #Calculate the meters per second
    return mpm/60

#Universal Gravitation
def universal_gravitation(mass1,mass2,distance,grav = 6.67 * (10**-11)):
    print("M1 =", mass1)
    print("M2 =", mass2)
    print("r =", distance)
    print("G =", grav)
    print("m*m =", (mass1*mass2))
    print("r² =", (distance**2))
    print("mm/r²", ((mass1*mass2)/(distance**2)))
    return grav * ((mass1*mass2)/(distance**2))
