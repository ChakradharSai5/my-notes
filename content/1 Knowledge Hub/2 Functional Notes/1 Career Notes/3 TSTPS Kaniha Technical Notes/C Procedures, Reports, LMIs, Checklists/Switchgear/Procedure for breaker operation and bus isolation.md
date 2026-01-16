
## Terminology

- **Breaker** - A big switch kind of thing, which "makes" or "breaks" supply, usually for higher current rated.
- **Module** - A big switch kind of thing, which  "Makes" or "breaks" supply, usually for lower current rated
- **Feeder** - Breaker from which supply is "going out"
	- Ex: On 11kv 1UA bus you can find UAT-1A feeder
	- So breaker that "Feeds"
- **Incomer** -  Breaker to which supply "coming to"
	- Ex: On 3.3kv UAA Sec-A you can find incomer from 1UAT
- This Feeder and Incomer I mentioned above are upstream and downstream breakers of UAT-1A Transformer
- **Bus** - A big copper bars (3 bars - one for each phase in 3 phase) running, from which drive supply taken for module or breaker
- **Bus coupler** - Usually a breaker(sometimes can be a module), that extends
- 
## Procedure for isolation of specific buses:
### ESP Board
- Any ESP Board has two incomers with one from ESP Serv. Trf.-A (Sourced from 1UA) & ESP Serv. Trf.-B (Sourced from 1UB)
- Both incomers and bus coupler – all 3 – can be operated from PB provided on the bus coupler panel only
- To cut off control supply (220V DC) to this bus, remove the fuses from the DCFB provided from the left and right corner of the Switch gear room, towards entry side, numbered DCFB-4 & DCFB #OHPending 
	- It is to be noted that, each breaker control supply has 2 consecutive fuses in the order to be identified as written on the panel as for any DCFB(DC Fuse Board)
### Coal Mill MCC
- To isolate a particular Coal Mill MCC, corresponding incomer and bus coupler to be made trip
- The feeder to MCC from corresponding SSS Section is manually operated only, no provision to operate from remote
- Incomer can be operated from remote, hence preferably to be tripped from remote
- Bus coupler also can be operated from remote
### DM Plant & FWPH
- Both section typically shall be individually charged and bus coupler in open condition
- Bus coupler panel shall have a selection handle, with three selections marked as A, B, & AB - representing incomer-A, incomer-B and Bus coupler - this is called "Trip selection" - which means the one that is to be tripped
- To charge through bus coupler
	1. Make the selection change towards breaker that is to tripped
	2. Now the close the bus coupler "Trip selection" panel
	3. Ensure the bus coupler closing, and selected breaker got tripped

### UAA Bus
- As UAA Sec-A/B/C shall have only drives related to IAC, PAC, CEP, DMCW etc.
- Necessary changeovers may be done before proceeding to isolation
- The connected bus coupler of respective section DC to be kept off to avoid auto closure on tripping the corresponding feeder from UA/UB
- After ensuring no running drives in particular UAA section, the corresponding feeder from UA/UB to be tripped
- Ensure incomer tripping in UAA section incomer(Bus coupler shall not close as DC off)

### SSS Bus
- Follows standard procedure
1. The feeders going from this bus to be identified(Ex: Here, Coal Mill MCC), and the incomers in those respective MCC to be tripped and isolated to ensure no back charging
	- The section with the incomer that is being isolated, to be charged through bus coupler
2. Ensure the running drives to be stopped
3. Ensure bus coupler in open condition and make the DC off
4. Trip the HT breaker (Here, from UA/UB ) of the corresponding LT incomer of this bus, and isolate the HT breaker
This ensures complete bus dead, no way supply can flow from HT side or LT side(back flow).
### Fly Ash MCC
- Standard procedure to be followed

### Raw water MCC
- Standard procedure, only additional point to be noted is about Tie to Sec-C
	- For Incomer-A to close, Tie and bus coupler both need be open

### DM MCC
- Standard procedure



