
# reset memory, set directory, and turn off existing figures
rm(list=ls())
setwd(getwd())
graphics.off()

rnormmix <- function(n, prop, mu, sigma){

    k <- length(prop)
    if (!(k == length(mu) && k == length(sigma)))
        stop("The dimensions of 'prop', 'mu' and 'sigma' do NOT match.")
    if (!(all(prop > 0) && all(prop < 1)))
        stop("'prop' has to be between 0 and 1")
    if (! isTRUE(all.equal(sum(prop), 1)))
        stop("Sum of 'prop' has to be 1")
    if (!all(sigma > 0))
        stop("All 'sigma's have to be positive")

    c <- sample(1:k, size=n, replace=TRUE, prob=prop)
    y <- rep(0, n)
    for(i in 1:k){
        ci <- c==i
        y[ci] <- rnorm(sum(ci), mean=mu[i], sd=sigma[i])
    }
    cbind(y,c)
}


dat_generator <- function(truth) {
    set.seed(1)
    n = 5000
    
    f = function(x) {
        out = numeric(length(x))
        for (i in 1:length(truth$pi)) out = out + truth$pi[i] * dnorm(x, truth$mu[i], 
            truth$sigma[i])
        out
    }
    y = rnormmix(n, truth$pi, truth$mu, truth$sigma)
    for (i in 1:length(truth$pi)) {
        assign(paste0("y", i), rnorm(n, truth$mu[i], truth$sigma[i]))
    }
    dat <- data.frame(y = y, y1 = y1, y2 = y2, y3 = y3)
}

truth = data.frame(pi = c(0.1, 0.5, 0.4), mu = c(-3, 0, 3), sigma = sqrt(c(0.5, 
    0.75, 1)))
dat <- dat_generator(truth)

write.table(dat,file="dat.dat",row.names=FALSE)

