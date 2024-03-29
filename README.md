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
    rho^4 ~ 3.07959562349144 = rho^2 + rho
    rho^5 ~ 4.07959562349144 = rho^3 + rho^2

F(2,2)

    F(2,2) ~ 1.220744085
    F(2,2)^2 ~ 1.49021612
    F(2,2)^3 ~ 1.819172513
    F(2,2)^4 ~ 2.220744085 
    F(2,2)^5 ~ 2.710960205 = F(2,2)^2 + F(2,2)

Conject that for a given F(n,2) 

    F(n,2)^(n+3) = F(n,2)^2 + F(n,2)

Easy way to compute limits

    F(1) = phi = F(0,2)
    F(2) = 1.465571231876768 = F(1,3)
    F(3) = 1.3802775690976141 = F(2,4)
    F(4) = rho = F(3,5)

conject the limit of the series F(n) is given by an element in the previous series:

    F(n) = F(n-1,n+1)


First 100 series limits:

    F(0) ~ 2.0
    F(1) ~ 1.618033988749895     x^2 = x + 1
    F(2) ~ 1.465571231876768     x^3 = x^2 + 1
    F(3) ~ 1.3802775690976141
    F(4) ~ 1.324717957244746     x^3 = x + 1
    F(5) ~ 1.2851990332453493
    F(6) ~ 1.2554228710768465
    F(7) ~ 1.2320546314285723
    F(8) ~ 1.21314972305964
    F(9)  ~ 1.1974914335516809
    F(10) ~ 1.1842763223508939
    F(11) ~ 1.1729507500239802
    F(12) ~ 1.1631197906692043
    F(13) ~ 1.1544935507090563
    F(14) ~ 1.1468540421995068
    F(15) ~ 1.140033937477005
    F(16) ~ 1.1339024903348374
    F(17) ~ 1.128355939691603
    F(18) ~ 1.1233108062463268
    F(19) ~ 1.118699108052226
    F(20) ~ 1.1144648799534382
    F(21) ~ 1.1105615981223105
    F(22) ~ 1.1069502450168822
    F(23) ~ 1.1035978353382538
    F(24) ~ 1.1004762790343705
    F(25) ~ 1.0975614942323275
    F(26) ~ 1.0948327079053122
    F(27) ~ 1.092271899234358
    F(28) ~ 1.0898633526169947
    F(29) ~ 1.0875932957790584
    F(30) ~ 1.0854496045569988
    F(31) ~ 1.0834215603634179
    F(32) ~ 1.0814996496192069
    F(33) ~ 1.0796753968675168
    F(34) ~ 1.0779412251108815
    F(35) ~ 1.0762903382967246
    F(36) ~ 1.0747166219343687
    F(37) ~ 1.0732145586419175
    F(38) ~ 1.071779156054469
    F(39) ~ 1.0704058850202818
    F(40) ~ 1.069090626401449
    F(41) ~ 1.067829625104681
    F(42) ~ 1.066619450214228
    F(43) ~ 1.0654569602966095
    F(44) ~ 1.0643392731061976
    F(45) ~ 1.0632637390499107
    F(46) ~ 1.0622279178745109
    F(47) ~ 1.0612295581261757
    F(48) ~ 1.0602665790028432
    F(49) ~ 1.0593370542783376
    F(50) ~ 1.0584391980257963
    F(51) ~ 1.0575713519083083
    F(52) ~ 1.0567319738384184
    F(53) ~ 1.055919627836474
    F(54) ~ 1.055132974941605
    F(55) ~ 1.0543707650492578
    F(56) ~ 1.053631829566251
    F(57) ~ 1.0529150747888052
    F(58) ~ 1.0522194759213541
    F(59) ~ 1.0515440716645008
    F(60) ~ 1.0508879593095317
    F(61) ~ 1.0502502902846866
    F(62) ~ 1.0496302661050787
    F(63) ~ 1.049027134683961
    F(64) ~ 1.048440186968044
    F(65) ~ 1.04786875386393
    F(66) ~ 1.0473122034265143
    F(67) ~ 1.04676993828351
    F(68) ~ 1.0462413932731371
    F(69) ~ 1.0457260332745495
    F(70) ~ 1.0452233512127838
    F(71) ~ 1.0447328662219708
    F(72) ~ 1.0442541219522632
    F(73) ~ 1.0437866850074473
    F(74) ~ 1.0433301435015525
    F(75) ~ 1.0428841057239469
    F(76) ~ 1.0424481989034702
    F(77) ~ 1.0420220680630814
    F(78) ~ 1.0416053749573362
    F(79) ~ 1.0411977970857405
    F(80) ~ 1.040799026775703
    F(81) ~ 1.0404087703293814
    F(82) ~ 1.0400267472292637
    F(83) ~ 1.0396526893977895
    F(84) ~ 1.0392863405067418
    F(85) ~ 1.0389274553325312
    F(86) ~ 1.0385757991538263
    F(87) ~ 1.038231147188305
    F(88) ~ 1.0378932840655741
    F(89) ~ 1.0375620033335595
    F(90) ~ 1.0372371069959012
    F(91) ~ 1.0369184050780864
    F(92) ~ 1.036605715220252
    F(93) ~ 1.0362988622947453
    F(94) ~ 1.0359976780467006
    F(95) ~ 1.0357020007560167
    F(96) ~ 1.0354116749192566
    F(97) ~ 1.0351265509501044
    F(98) ~ 1.0348464848971208
    F(99) ~ 1.0345713381776367


also see: http://www.mscroggs.co.uk/blog/tags/golden%20spiral
  
