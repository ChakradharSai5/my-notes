### ST-1 and SA bus PTW
- We know that before overhauling, we need to give some of buses overhauling PTWs mainly MLDBs, Welding DBs, today I came to know that we need to give ST-1 and SA bus also, for of course obvious reasons as once unit get to shut down, we may have to trip that 400kv two breakers, so we will be forced to use supply from Start up Transformer, as we cannot give at that time, we have to give now
- Coming to know that we have to give this PTW, I thought it will be quite complicated, as felts afterwards, it's not that complicated
- First to understand, I realized I need to understand the scheme, and you know from yesterday I am making an electrical SLD for Unit-1 and partial offsite, to understand, I included this ST-1 and SA bus scheme to that SLD diagram
- After drawing that diagram, I clearly understood, what needs to be done, but don't know how to do it, like the breaker in the switchyard.
#### Procedure
- Important thing to note here is, for any bus we need to isolate
	1. the supply coming from the feeder to that bus, that is the source, and 
	2. downstream breakers which that bus is feeding, 
	so that there should be no voltage coming from either end, as they work in that bus
- And usually, we give a bus and corresponding transformer at a time, so that that transformer unavailability due to bus non availability can be exploited.
- So here whiling giving SA Bus we also gave Start up transformer
As per drawing seen from [[Unit-1 and related OFS SLD]], we are suppose to isolate breakers in SA bus, one in SB bus, and a breaker connected to 220kv switchyard, and in downstream to SA bus an incomer bus at Miscellaneous Switchgear connected upstream of Start up transformer.

The breakers at SA, SB bus, and at Miscellenous switchgear were simply racked out and DC off, like regular HT breakers
however for 220kv side CB it think CB 252, and this is peculiar
##### Isolating CB 252 connected to 220kv Transfer bus
- First, In switchyard control room, identify the drawing on the big control panel, identify  corresponding isolators, and earth switches, in our case, 252CB, 289T - isolator in transformer side, 289A/B/C as can be seen in [[Unit-1 and related OFS SLD]]
- Now after identification, you will know which bay it is, I think it will mentioned there, or ask the switchyard operator, he will let you know which bay it is, and that bay particular key shall be in that key hanging place in that control room, that bay key is must, that one bay shall open all that corresponding bay located breakers, isolators, earth switches local control box
- Now, we went to our required CB 252 bay with that bay respective key, first we unlocked that CB local control box, and I think there is provision of selection of DC on/off and selection of Local or remote, and usually DC shall be off and selection shall be in Local - For breakers I don't remember, but one thing for sure, the selection is to be in remote, and then, we call switchyard control room they trip the breaker from the switchyard control panel I told you about, while we stand little far from breaker, as it makes a good enough sound.
- For isolators and earth switches, it will be like this shown below here , DC, power switch, operation selector switch, all three in off usually![[20251213_084505.jpg]]
- After ensuring breaker open, here CB 252, we need to make 289T open, and 289TE close, 289A/B/C must be open, in our case, only 289A to be made open, as other two B & C is already open.
- Now, as expected, for isolator to open, we open that particular local  control panel with the bay key we got(that bay key opens all that bay located breakers and isolators and earth switches), and make the three DC on, power on, selector switch remote, and inform #pending - ASK SRIKANTH
- after opening isolators and closing one earth switch and locked each of them with our own locks along with bay lock, PTW issued

Later that day in evening, they have cancelled the PTW, as said by our Shrimali sir, initially EMD planned it for 2 days, but due to i think GM O&M pressure, they completed work fast and gave it back in that day, so we had to normalize at the day end
- For normalization the procedure is almost as expected
- first incomers from ST-1 to SA bus i.e SA bus incomer, and SB bus incomer, normalized but not closed.
- then came to switchyard, first earth switch made open, then 289T transformer side isolator made close, then 220kv isolator 289A made close, (gave zzzz spark as 220kv bus-A live), then, other isolator just lock removed, as they should be open
- Then CB lock removed kept in remote
- Here comes the tricky part, we just don't directly close this CB, after this noramalization at local, we got switchyard control room and there something called synchroscopy trolly, that we drag it and connect it to a multi pin beside the breaker we want to close, in our case CB 252
	- Then here in our case as ST-1 downstream is dead, we don't need synchonizing, hence, there is two rotating knobs on the trolly, as far as i remember #pending - ASK SRIKANTH 
	- we made both turn, one knob is for bypassing that synchroscopy as we are charging a dead side to 220kv side, and with that rotation, we get to see to lights glowing, which is our clearance to proceed to close the breaker
	- close from small T type isolator on the control panel to which this trolley connnected
- So this ST-1 is idle charged
- Then we went to SA bus closed the incomer there, closed, Tie to UA/UB in SA bus, went to SB bus and closed SB bus incomer, then went to miscellenous switchgear and normalized downstream to MS Trf-A, and then closed MS-A feeder in SA bus, then went to SB bus closed MS-B feeder and kept both MS Trf-A & B idle charged

