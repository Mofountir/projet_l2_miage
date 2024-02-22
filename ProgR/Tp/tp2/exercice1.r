#TP2

#exercice1

donnees<-function(n,K)
{
  u=K*runif(n)
  donnees=1+floor(u)
}

n=100000
K=10

x <- donnees(n,K)

table(x) # moyen empirique en fonction  de n



#exercice 2

donneesb<-function(n,P)
{
  u=runif(n)
  cP=cumsum(P)
  vX=c(20,10,0)
  v=c()
  
  for (i in 1:n)
  {
    b=u[i]
    a=(b<=cP)
    s=sum(a)
    v=c(v,s)
  }
  donneesb=v
}

P=c(1/6,10/36,20/36)

X <- donneesb(n,P)
table(X)
barplot(table(X)/n)



#exercice 3
setwd('~/ProgR/Tp/tp2')
