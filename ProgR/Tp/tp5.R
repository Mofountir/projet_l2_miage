
n <- 10000


U1 <- runif(n)
U2 <- runif(n)


Z1 <- sqrt(-2 * log(U1)) * cos(2 * pi * U2)
Z2 <- sqrt(-2 * log(U1)) * sin(2 * pi * U2)
Z3 <- sqrt(2) * Z1

xx <- seq(-4,4,by=0.01)
yy <- 1/sqrt(2 * pi) * exp((-1) * (xx^2)/2)
V3 <- 2
yyy <- 1/sqrt(2 * pi* V3)  *exp((-1) * (xx^2)/(2 * V3))


par(mfrow = c(1,3))

hist(Z1, main = "Distribution de Z1", freq=FALSE)
lines(xx,yy,col='red')
hist(Z2, main = "Distribution de Z2", freq=FALSE)
lines(xx,yy,col='red')
hist(Z3, main = "Distribution de Z3", freq=FALSE)
lines(xx,yyy,col='red')










