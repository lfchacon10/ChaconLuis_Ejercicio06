x = [4.6, 6.0, 2.0, 5.8]

sigma = [2.0, 1.5, 5.0, 1.0]

umas = np.linspace(0, 1, 100)

def probXk( X, Sigma, Uma):
        r= (1/np.sqrt(2*np.pi*Sigma**2))* np.exp(-(0.5 * (X -Uma)**2 / Sigma))
        return r

def logProbXk( X, Sigma, Uma):
    r= np.log( 1/np.sqrt(2*np.pi*Sigma**2) ) - (0.5 * (X -Uma)**2 / Sigma)
    return r

post0 = probXk(x[0], sigma[0], umas[:])
post1 = probXk(x[1], sigma[1], umas[:])
post2 = probXk(x[2], sigma[2], umas[:])
post3 = probXk(x[3], sigma[3], umas[:])

logPos0 = logProbXk( x[0], sigma[0], umas[:])
logPos1 = logProbXk( x[1], sigma[1], umas[:])
logPos2 = logProbXk( x[2], sigma[2], umas[:])
logPos3 = logProbXk( x[3], sigma[3], umas[:])

post = post0+ post1+ post2 +post3


L = probX0+probX1+probX2+probX3

dL= np.gradient(L)

d2L= np.gradient(dL)

integral = np.trapz(L,umas)
print(integral)

plt.plot(post/integral, umas)

#No pude.
