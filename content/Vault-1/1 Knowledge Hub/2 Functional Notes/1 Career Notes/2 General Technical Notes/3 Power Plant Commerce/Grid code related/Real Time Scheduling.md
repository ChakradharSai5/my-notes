---
dg-publish: true
---
![[Pasted image 20250429083403.png]]
Figure -1



![[Pasted image 20250429083415.png]] 
Figure-2


may refer [[Components of SG]] for some more understanding
### Real Time Scheduling - NLDC perspective Figure-2
- In real time, any current block, shall have the planning started some 8 or 7 blocks ago, that is, from 7 or 8 blocks in real time, they see network or distribution limitations and beneficiaries schedule, and real time market demand and may be other things and with cost effective approach to bring down the overall cost of electricity and many other considerations might be there, to cater stable power for a block coming 7 or 8 blocks later.
- And for this the real time scheduling - is this is how it is going to work, if you see in figure-2 - below figure
	- Now we are talking about a block coming at D-Day zero hour, (For what is D-Day may refer [[Day ahead Scheduling]]), that is the first block.
	- we can safely say that though technically D-day starts at zero hour, as we have discussed above, the planning & scheduling starts from 6 blocks before excluding the delivery block, that is as we can see from figure-2, the delivery block being T7 block, that is 0000Hrs to 0015hrs, our ~ starts from 2230-2245Hrs, so as a generator you can change your DC for partial load through [[DC Revision Mechanism & Strategy]], in 6 blocks counting backwards from the delivery block, excluding the delivery block, in the 6th block
	- So here since our delivery block is 7th block 0000-0015hrs, counting backwards, 1, 2, 3, 4, 5, 6(Count excludes delivery block) , the 6th block comes out to be 2230-2245Hrs, the DC revision if need be by generator done, shall gets punched in and gets affected in to 0000-0015Hrs
	- **NOTE**: Here the understanding of block timings for DC revision I am telling perspective from NLDC & RLDC planning, from our - generator perspective - it shall be slightly different, only perspective understanding differs, working mechanism of course stays the same. From our - generator side refer [[DC Revision Mechanism & Strategy]]
- As from figure-2, self explanatory - in T1 block, NLDC sees WBES - web based Energy sheduling, (including DC taken from us punched in this block only, if we need any partial load as per [[DC Revision Mechanism & Strategy]]), and accordingly sees about GNA and TGNA through NOAR - National Open Acess registry, basically grid is seeing transmission system effeicincy best utilization, in real time, based on that it schedules in this T1 block
- in T2 block, from figure-2,
	- by the start of the block, we have revised DC from generators also latest by last block T1 shall be considered, using that LDC does this follows
	- 5 mins RLDC approval of GNA schedule revision in WBES, 
	- 5 mins see figure-2
	- 5 mins Approval of T-GNA application and pushing schedule to WBES
	- **parallelly** as seen from figure-2, RTM auction in PX  also happens, 
	- So basically three things happen as can be seen in figure-2, New TGNA application run, GNA schedule revision request approval and RTM auction in Power exchange - PX
- in T3 block, from figure-2
	- 5mins PX gives NLDC the provisional RTM trade
	- 5mins NLDC sees margin pull(don't know what it is) & congestion checking
	- 5 mins schedule pushing to WBES
- In T4 block from figure-2
	- SCED, TRAS Dispatch
- In T5 block at 2335Hrs - in our case RLDC issues final schedule
- T6 relax ;-)
- T7 the delivery starts
#### ODD and EVEN block clarity
- Here the thing is as per my current understanding, this thing is there because they want to do this T1 to T6 work every half an hour, 
- So what happens is for the example we took here 0000-0015Hrs as our delivery block being odd, the T1 to T6 is where the work happens, and T7 is our delivery block right?
- For 0015-0030Hrs, the even numbered block, simply the work that happened in T1 to T4 shall be the same, only extra work in T5 where they SCED run (I don't the reason), and so **as can be seen from figure-1**, from T5 work of Odd block scenario shall shift to T6 in even, T6 of odd to T7 of even, and so delivery being T7 in odd scenario, T8 in even block scenario
- notice that for this 0000-0015 & 0015-0030Hrs they-NLDC and co. started working from 2230-2245(Figure-1), which is termed T1 block, T1 to T4 same work, T5 to T8 slightly different, now for next half an hour i.e 0030-0045, 0045-0100, the **same** work starts from 2300-2315, so every half an hour their work does.
### Real Time Scheduling from out perspective - Figure-1
#### T1 block - Any ISGS and DC updating
- As shown in figure-1
- ISGS can change their SG up until in T1 block, for both odd and even blocks, in real time, they can change their schedule in T1 block
	- And in that, interesting thing is if any beneficiary surrenders partial or fully entitled portion, any other beneficiaries, even if it is beyond their entitlement, they can take that much portion - how much ever surrendered by former one.
	- that is called **URS** 
	- Be it ISGS or URS it can be set in side this T1 block, after T1 block ISGS cannot change their SG and so URS component cannot come
	- by the end, URS component gets shown in our SG 
#### T2 - block
- In figure-1, RTM goes for 10 mins, in T2 block, NVVN participates in it.
#### T3 - block
- In this, basically whatever bidding done in T2 block, the result by Power Exchange PX shall share the result to NLDC & RLDC in first 5 mins
- After that, NLDC & RLDC do the work of publishing this to WBES that'll take 10mins
- RTM component gets shown in our SG
#### T4- Block
-  During this, RRAS and SCED gets calculated by NLDC and the same shall - if gets generated - gets added our component of SG
- So, RRAS & SCED gets added
- Note that, for odd block scenario, this RRAS & SCED gets added in T5 block starting, however, in even block sceanrio, RRAS at T5 block start, and SCED gets added at T6 block start, an additional block used 
#### T5 - For odd block,  T6 block - Even block scenario
- They say, TRAS or RRAS or SCED gets added in T5 block - in odd block scenario, and in even block T6 block
#### T6- for odd block, T7- Even block scenario
- Prep time for generator that is, in our perspective, our SG is finalized 15mins before the delivery block, so that, we can prepare for next block
 