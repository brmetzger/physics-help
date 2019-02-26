#Calculate the circumference of a circle
def circumference(radius):
    return radius * 2 * 3.14

#Meters per second to revolutions per minute
def mps_to_rpm(mps,radius):
    print("MPS =", mps)
    print("r =", radius)

    #Calculate the circumference
    circum = circumference(radius)
    print("C =", circum)

    #Calculate the meters per minute
    mpm = mps * 60
    print("MPM =", mpm)

    #Calculate the revolutions per minute
    return mpm/circum

#Revolutions per minute to meters per second
def rpm_to_mps(rpm,radius):
    print("RPM =",rpm)
    print("r =", radius)
    
    #Calculate the circumference
    circum = circumference(radius)
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
