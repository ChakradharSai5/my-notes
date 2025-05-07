---
dg-publish: true
draft: false
---
Delta P= − (∑ ULSP)

- So for changing delta p( = AGC correction)
    - You can either change ULSP(affects inversely)
    - Or you can limit AGC SP coming from NLDC by changing unit load capabilities(affects proportionally )
#pending to excalidraaw
![[p8rcac8 - Imgur.png]]

## AGC

- Primary control – RGMO/FGMO

Secondary control – AGC

Incentive @ 50ps/kwhr of over and above normative energy

Teritirary control-  RRAS

- Here at kaniha, in CMC, the MW demand signal that is getting generated is
	- Setpoint - AGC correction
	- **NOT** setpoint - AGC correction - RGMO, 
- so that means I guess this RGMO command is directly going to Turbine command after this MW demand signal from CMC #pending 



### AGC benefitting logic
- As per our EEMG, TSTPS Kaniha is performing not upto mark in AGC performance, they'll see how much our AG is following AGC and percentage of accuracy following shall be calculated, based on that incentive shall be given
- Now the thing is as per sudhanshu EEMG for St-1 TSTPS especially, it is not recommended to give SP more than 502MW, if we do we are loosing on performance(I don't know why), also said, that 2MW given, because APC is higher