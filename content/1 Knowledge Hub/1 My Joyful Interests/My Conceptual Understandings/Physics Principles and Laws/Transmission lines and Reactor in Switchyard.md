- For a power that is generted in generator AC or with DC source like solar power or some other needs to sent to drive/motor/loads
- For that we send it through big copper wire which we call transmision lines
	- And in that for DC we need to send two wires, one for sending line, other return line for completing circuit
	- however in AC 3Ph, we don't need to and we actually don't send a neutral wire, because the 3 phase of R Y B, each of these uses other two as return paths per se. because you know all 3 are connected anyway be it in star or delta we just forcing the electricity flow in it by faraday's law, just 120Degress apart, so all are connected anyway, and so the current flows 
		- R returns through Y & B
		- Y returns through R & Y
		- B returns through R & Y
#### Capacitance and Inductance
- Now this copper wire, oscillating with charges(In AC) refer [[Current Travel in DC & AC - Micro level]], 3 wires, seperated by distance, hence they form similar to capacitor structure as charges of different polarities seperated by distance with insulator between.
- Similary each of thsi phase wire also forms a capacitor kind of structure with ground, 
- _In AC, charges move back and forth (oscillate), but they ALSO rearrange to create the electric field._
- So even with current flow, part of the electrons always
	- Accumulate slightly on surfaces → produces C
	- Move back and forth → produces I
- ##### **“But in AC, charges are switching polarity every half cycle…”**
	Yes — and that is why capacitance becomes extra important in AC:
	During every cycle:
	- The voltage changes polarity
	- The surface charge distribution reverses
	- The electric field collapses and reverses
	- This changing E-field creates **displacement current** 
#### About displacement current
- For this part go to [[Maxwells Laws]], because we know
	- ∇×B=μ(J+ϵdtdE​)
	- as with all [[Maxwells Laws]], right side is cause, left side is effect
	- so constant flow of current(I =μJ) gives rotating **constant** Magnetic field around it
	- same way, that fucker Ampere found that changing Electric field also creates same effect of constant current flowing that is producing rotating constant Magnetic field, so he termed it as "Displacement current"
- So coming to our transmission lines, as any line of this R, Y or B between them or between each of them to ground, there exists, a capacitor for obvious above mentioned reasons.
- Now this capacitor voltage also continuously varies, so this causes displacement current
- you can imagine a many million capacitors between line to earth and between line to line, as long as polarity difference between two conductors that forms a capacitor, and as long as the voltage across this capacitor continuously changes - causes displacement current
- Note that this current or this effect comes in play only with AC current, not with DC, as only when voltage varies that causes the capacitor plates between electric field varies and so creates displacement current from [[Maxwells Laws]]
#### Inductive Reactance
- ![[Reactance in Transmission line.svg]]
[[Reactance in Transmission line]]
- Now you see this induced current shall gets subtracted from the original current I we are sending, but you see, this happens with slight delay, because, only **rate** **of** **change** of magnetic field generates electricity, 
	- Constant current generates Magnetic field
	- Current changes with time hence Magnetic field also do
	- Changing B produces Faraday EMF, and incidentally we have a conductor placed in that EMF
	- EMF makes current flow in opposite direction of biot sovort law, but here in our case as B came with biot sovort law, this faraday's generated current direction opposite to original current
	- But it appears with a TIME OFFSET, a time offset from voltage variation to current variation
	- That time offset becomes a PHASE SHIFT, so voltage leads current by 90Dg
	- That phase shift is what we call **reactance**, and in a ideal inductor that is 90Dg
Now that you understood about capacitance and reactance we'll see about reactors
#### Reactors
- Now you see because of this, we can model a transmission line as a capacitor and  inductor as below ![[long-transmission-lines-121-compressor.jpg]]
- But you see, the R shown in figure is negligible, so mostly C and L in the line
- now somehting called ferranti effect come in play when there is very less load for this transmission line, 
###### Ferranti Effect
- This comes in play only when the load end load is very low or zero
- because 
- **STEP 1 — The line capacitance draws current even with NO load**
Each shunt capacitor draws **charging current**:
			I(C)=ωCVI_C = ωCV
This current is **leading the voltage by 90°**.
This is the first key point:
Even with NO load, the line still draws current
This current is purely reactive, leading
This current flows along the entire line
And this current must flow through the **series inductance** of the line.
Leading current through inductance creates a voltage BOOST**
This is the heart of the Ferranti effect.
Voltage drop across inductance:
VL=ICXLV_L = I_C X_LVL​=IC​XL​
But since **I_C leads V by 90°**, the “voltage drop” across the inductance actually becomes a **voltage rise**.
How?
Let me explain using phase:
Inductor voltage **lags** current by 90°
But capacitor current **leads** voltage by 90°
So the combination becomes:
The voltage across the inductor is IN PHASE with the sending-end voltage
Meaning:
VR​=VS​+VL​
This is why the receiving-end voltage becomes **greater** than the sending-end voltage.
Important thing to note here is that this gets cancelled when there is load at sink end
When a real load is connected:
- It draws **real current + some lagging current**
- Lagging current naturally **cancels the leading capacitive current**
- Net current becomes more “normal”
- The inductive drop becomes an actual drop
- Receiving voltage becomes **lower**
But with **no load**, nothing absorbs the capacitive VARs.
Result:
- All the charging current flows along full line
- Voltage continuously rises along the line
	- Peak is at the receiving end 
That is your **Ferranti Effect**.
So in one line 
- **Under no-load conditions, the only current flowing in the line is the capacitive charging current, which leads the voltage by 90°. This leading current passing through the line’s series inductance produces an in-phase voltage rise at the receiving end. When a real load is connected, the current becomes less leading or even lagging, so the voltage across the line inductance behaves as a normal voltage drop, eliminating the Ferranti effect**