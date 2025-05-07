---
dg-publish: true
draft: false
---
- security constraint unit commitment
- if as mentioned in [[Day ahead Scheduling]], if all after 1430Hrs, many units get below technical minimum, and they all decide to shutdown the unit and purchase the power from somewhere then there's a great chance that when frequency is low, it is difficult to pump in the power to grid to improve the frequency, so what NLDC shall do is it measures the what is called "spinning reserve"
	- it shall already have [[RRAS]], and AGC under its control for this, for short control, 
	- And for long control it has [[RSD]], units are not on bar
	- but for medium control it needs this ''spinning reserve" from the units which are on bar
- spinning reserve means, there should be enough margin from generators to compensate the frequency up or down may be due to RE or anything, simply to do up side and down side both side it should have enough margin to cater the frequency fluctuation
	- the thing is, during checking what it will mostly is which units are getting less than technical minimum, because those are the units that most probably go under shut down, of course from where they'll compensate is different thing, because they are bound to do it, but ultimately spinning reserve shall come down
- so to keep that in check this SCUC software engine is made and what it does is after all scheduling, it shall run and see the above thing is in check or not, if not it makes some units from least cost ECR units for margin to increase and higher cost units to margin to decrease to adjust the spinning reserve, based on **merit order**
- For example: say Farakka got 35% SG, and kaniha got 100%, then during SCUC, they may make 20% from kaniha Farakka, so that 55% for Farakka, and 80% for kaniha, and so NLDC got both up and down spinning reserve
	- during this shit, generator or beneficiary shall make no profit or loss, only overall price of electricity, and that is the tradeoff we are taking for having grid stability, and the price to generator and beneficiray shall be adjusted/tallied by NLDC which is whole different topic, so no need to worry about money from both sides
- only during [[SCED]] or [[RTM]], the SG may vary, unless other wise once you get [[SCUC]], your SG shall most probably not vary, because once SCUC comes, beneficiary shall have some 15% of its allocation can only be varied, remaining 85% shall be in hands of SCED or RTM 