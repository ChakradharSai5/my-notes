---
{}
---
##### When one UT was not available
1. During Mini OH of Unit-2, 2UA and 2UB both charged under ST-1 and also one of the bus in unit-1 is loaded with ST-1 as some UT non available
2. To keep ST-1 load minimum, while light up of Unit-2,  U-1 MDBFP kept in manual, and Unit-2 light up done with one set of ID  & FD fans.
3. Later after synch, one of buses changeover done to unit load
4. and after around 50MW another bus also changeover done from SB bus to GT back charging.
5. after synch ID FD , PA , then mill purged and taken I/S
##### Did it alone
This is briefing, then I will explain each step 
- During Unit-1 Lightup I was UCE with Hitesh, Abhinav, and unit under shutdown, with leakage at RH circuit.
- Boiler did not drained as lightup did that day morning, unit tripped at 55ksc MS pressure.
- Major things I did are Vacuum pulling, Gland steam charging, connected RH circuit to vacuum, then disconnected after clearance from them.
- Then MD-C started - talked to chemistry for 200Tph clearance, kept in 200Tph, started pegging, then, after pegging, made temperature increase in MD-C suction
- Then, handled SDCS valves
- Then came home, slept, again went to lightup activity at 0400Hrs, at almost 74ksc, then achieved 85ksc, then rolling done, done ATT, then done FCB closing, then synch, then handled RH temperature control for stress control. 
- Then, handled a small emergency of LPH-2 valve closing, then, both TD-A loaded along with MD-C, then both kept in auto, then changed to IP mode, then feedwater kept in auto.
- Then tried to roll TD-B, then came this problem of engaging problem, attempted to handle that. but as it was already 2100Hrs, and needed rest for that day night shift, came back home
- Overall good experience, I'd say, I can now single handedly handle lightup procedure, only thing, I need to know more about systems, much deeper like LLD, seal oil logics, Stator water exact scheme tracing, AFT TFT drains exact scheme, H2 cooler logics, need to get crisper clear clarity on them. Also on handling off site, be it Ash handling, or CWPH - this scheme need to know clearly
###### **Debriefing**
-  Unit got shutdown initially due to BTL in water wall and RH circuit, however, while attending so, they-BMD, have opened two vents (Not entirely sure), and forgot to close one.
- Leading to, though unit lightup done and reached 55ksc, with RH pressure 12ksc, the RH vent found heavily sound, hence unit had to be stopped.
- In evening shift, after this shutdown, I am in UCE (safe shutdown status), and as leakage is at RH circuit, no need for boiler draining, but for attending leakage RH circuit has to be completely depressurized, hence I waited for boiler depressurization with HPBP and LPBP slight open
- After MS pressure reaching some 0.8ksc, to drop the vacuum faster, I intentionally closed Gland steam from CRH(as changeover was already done at MS Pr 40skc I think), which led to faster Vacuum dropping, when vacuum dropped to 200mmhg in DCS roughly - Vacuum breaker got tripped
- And that's fine.
- Made all drain MOVs that can be opened here made open. Sent Murmu ji for opening 48Mtr & 5.5 reheater drain.
- For welding of RH circuit at that place, they need no pulling of air or pressurizing of air coming out, hence, they asked as it is pressurizing, to decrease that, I said I was opening drains, however with 48Mtr drains made open only, before even opening 5.5Mtr RH master drain opening, they called and told this is perfect for welding, hence I did not made that RH master drain to open. - That's interesting
- Then after they gave clearance for Vacuum pulling
	- Breaker made close, then, Vacuum pump started, and other vacuum pump also started, made the vacuum built up to 200mmhg- DCS
	- Then after achieving 200mmhg, Gland steam charged
	- Charging Gland steam : first open the exhaust bypass valve full, we tried to open it by inching, but it is taking some 10 pulses, hence directly opened it
	- Then, already opened the drain of Aux steam source valve, then, reaching at least 180DegC, Aux PRDS isolation valve made open
	- Then, observed the Gland steam temperature - suppose to go above 100DegC, at least.
	- Only after achieving at least 100DegC, we start closing the exhaust bypass and so slowly, actually here also, we directly made the inching valve to close.
	- And so the gland steam pressure that is till now showing -ve something, slowly builds, as the pressure increases above the set point (which is technically 0.05ksc, but here it is 0.03ksc) the pressure goes slightly above 0.03ksc, and then the admission valve starts closing
	- The admission valve gets stable at certain may be some 50-80%, and maintains pressure set.
	- The gland steam working mechanism is [[Gland steam Working mechanism]]
- Then as per BMD request to connect the vacuum, LPBP made reset, and then, LPBP taken to manual, and slowly opened to 5-10%, the RH pressure in DCS (which is boiler side) made negative to some -0.2ksc.
- Then after clearance from BMD, LPBP CV made close
- Then BMD gave clearance for Lightup, here for that, as boiler in already filled condition, only thing is to start MDBFP-C to be started and keep it in 200Tph recirculation
	- as usual - discharge valve module off, - IBV manually crack opening- then discharge valve module on and off until pressure matches, then LLCV slowly opened for 200Tph recirculation
- Then started pegging, with FST heating from ASL inching valve, and with pegging valve at may be some 20%, and pegging CV to De-aerator  opening and maintained pressure at some 1.5ksc around, rated 2.5ksc
	- Here I did not kept the FST heating valve open for long time, that is one of the reason for not getting temperature increase
- SDCS valve story
	- Technically we have to keep AA, AN in auto which gets opened mostly
	- ANB to be kept in manual, with may be some 10-30% opening
	- But what I did is ANB valve in auto, and AN valve manually opened, so as to send the whole water of boiler to ANB for fast increasing of temperature of Feedwater
	- Actually, I don't know that AA, AN to be kept in auto and ANB in manual like that, thank god I found of very absolute good logic for what I have done
	- this worked good for some time, but when clearance recieved for 600Tph and so did. it became difficult for only ANB & AN, AN also had to be made some 80%open
	- Luckily Kasi sir came asked why am I sending all the dirty water to De-aerator, luckily I have a very good logic that, as boiler not drained, there is no dirty water, chemisty said we already have remaining chemical parameters, except for FW DO, which can attained early with increasing FW temperature, which can be done with sending most water to De-aerator instead of sending water to Hot well AA & AN.
	- Guess he got conviced, however opened the AA CV and kept in auto, all AA & AN both kept in auto, and ANB kept in manual to some 20-30%
	- The level maintained smooth
- Then after achieving 600Tph, I came home.
- Then again at night at 0400Hrs, went to plant for lightup continuation
- By the time I went pressure was around some 70ksc, and increasing
- Increased to 85ksc, got the parameters achieved for rolling 
	- for rolling 85ksc corresponding saturation temperature difference to temperature the steam needs to 55DegC
- And after reaching these rolling parameters, we select Load mode, which got the CV to open and so rolling of the turbine
	- While rolling, Ashok sir told, for only one particular range of critical speeds has higher ramp rate, for remaining critical speeds the ramp rate is normal. #pending 
- Then, after completion of rolling, i.e. reaching 3000rpm, then kept in No Load excitation, then, the FCB gets closed manually or gets closed in auto - not sure, then, I increased the Excitation voltage by giving pulse by pulse up until 20.5kv
- Then after this, we kept in Load mode, PRS synch Auto, then Synch Device on, then unit synchronizes in auto, but before that we need to keep the MW control click and ready to make it on, if gets on in auto when synch, well and good, if not then, we have to keep it in MW control and increase the Set point to atleast 55MW, also, low forward power relay acts at 15MW - as said by Ashok sir #pending 
- Once synchs, as usual maintain the RH temperature control with spray to control streess I handled very good I maintained around 400-425DegC, from [[Main TG rolling#**Bypass mode**]], it can be  seen that for rolling clearance for TG rolling. may be linked to that 
- refer [[Stress calculation and logic]],
- Then, did things, as usual, but important are the sequence of steps
- Maintained Feedwater around 850Tph to 900Tph, as it drops or rises due to pressure or decrease is maintained with MD-C scoop & TD-A - both were in loaded condition with TD-A RC open
- Then, first changeover of RC done from TD-A to MD-C.
- Then FRS bypass valve made open, I wanted to keep BFPs in auto before doing, but Kasi sir insisted to do it with both in manual, so did accordingly pressure got dipped by may be 10ksc and feedwater increased by some 200-250Tph. but decreased the same proporationately in MD-C & TD-A, so ok.
- Increase FW Man command at Feedwater master station, and matched with scoop command and kept that in auto, then, TD-A also adjusted speed to match with internal command, and kept that also in remote.
- Then controlled feedwater directly from Feedwater station, then after taking to MW control, feedwater kept in auto.

