## n,m fibonacci sequences

### Simple python class that calculate the ratios of n-order fibonacci-type sequences.

 for example,
 
     fibonacci numbers: Fi+1 = Fi + Fi-1 -> phi as i -> inf. (golden ratio)
     padovan numbers: Pi+1 = Pi-1 + Pi-2 -> rho as i -> inf. (plastic ratio)
  

 definition:
 
    let Fi(n,m) be an n-order fibonacci-type number where n is the number of elements on the 
    left to skip and m is the number of elements to add, and i is the ith element in the list
     
 for example:
 
    fibonacci: Fi(0,2) = Fi+1 = Fi + Fi-1, i.e. skip 0 numbers to the left add two
    tribonacci: Fi(0,3) = Ti+1 = Ti + Ti-1 + Ti-2i, i.e. skip zero numbers to the left add three
    ...

    padovan: Fi(1,2) = Pi+1 = Pi-1 + Pi-2, i.e. skip one number and add the next two
    "tri"-adovan: Fi(1,3) = Pi+1 = Pi-1 + Pi-2 + Pi-3, i.e. skip one number and add the next three
    ...

converegence of Fi(n,m) series:
  
  let F(n,m) be the converegnce limit of an Fi(n,m) series defined as:
    
    for (n>=0 and m>=2) define F(n,m) = lim i -> inf. Fi+1(n,m)/Fi(n,m)
    
  examples:
  
    F(0,2) = lim i-> inf. Fi+1(0,2)/Fi(0,2) = phi (golden ratio)
    F(1,2) = lim i-> inf. Fi+1(1,2)/Fi(1,2) = rho (plastic ratio)

convergence of F(n,m) limits:
  
 let F(n) be the convergence limit of an F(n,m) series defined as:
 
     (for n>=0) define F(n) = lim m -> inf. F(n,m) = lim m,i -> inf. Fi+1(n,m)/Fi(n,m)

  examples:
  
      F(0) = lim m,i->inf. Fi+1(0,m)/Fi(0,m) = 2  (fibonacci sequeunce)
      F(1) = lim m,i->inf. Fi+1(1,m)/Fi(1,m) = 1.6180339887498952 (padovan sequence)
      F(2) = lim m,i->inf. Fi+1(2,m)/Fi(2,m) = 1.465571231876768
      F(3) = lim m,i->inf. Fi+1(3,m)/Fi(3,m) = 1.3802775690976141

Some properties of the convergences:

fibonnaci constant F(0,2)

    phi ~ 1.618033988749895
    phi^2 ~ 2.618033988749895
    phi^3 ~ 4.236067977499790 = phi^2 + phi
    phi^4 ~ 6.854101966249685 = phi^3 + phi^2

plastic ratio F(1,2)

    rho ~ 1.3247179572447460 
    rho^2 ~ 1.75487766624669
    rho^3 ~ 2.32471795724475
    rho^4 ~ 3.07959562349144 = rho + rho^2
    rho^5 ~ 4.07959562349144 = rho^3 + rho^2






also see: http://www.mscroggs.co.uk/blog/tags/golden%20spiral
  
