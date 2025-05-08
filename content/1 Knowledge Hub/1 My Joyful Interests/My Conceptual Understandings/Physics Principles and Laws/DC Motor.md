---
draft: false
---
- Now before reading this it is recommended to read [[DC Vs AC Motor Working mechanism]], where I have explained how DC motor works
-  Now the thing is, DC motors speed control is easy, by just controlling the DC voltage supplied to rotor, by simply, increasing or decreasing the voltage, causes the rotor to speed faster or lesser
- Also application where we need this is, where we need precise control over speed and high starting torque, because the first one is ~, the second one is because in AC first induced current has to build up and then the rotation starts, so just at the very start it will not have heavy torque, however that is not the case with DC, here, if we send enough current, the loop starts to rotate
- next you may refer [[AC Motor]]
### Types
- They are majorly two types
	- Brushed DC Motors (Have Brushes & Commutator)
	- Brushless DC Motors (BLDC)

#### Brushed
 - Brushed DC motors provide higher starting torque but struggle at high speeds.
	- Brushed motors are cheaper and simpler but wear out faster due to brush friction.
	- Torque and speed control is Simple (Controlled by voltage)
	- Efficiency Lower (Energy lost in brush friction)
	- Torque at High Speed - drops due to friction
	- Control is Slightly jerky (due to mechanical commutation)

#### Brushless
 - This working mechanism is interesting
		- in a brushless DC motor (BLDC):

	1. The rotor has permanent magnets instead of windings.
    
	2. The stator (stationary part) has multiple coils (windings).
    
	3. Instead of brushes, an electronic speed controller (ESC) switches current to different stator coils at the right time using transistors.
    
	4. This creates a rotating magnetic field (RMF), which attracts the permanent magnets in the rotor, making it spin.
	- ###### Speed Control
		- - The ESC changes the switching frequency (how fast the stator's magnetic field rotates).
    
		- Higher switching speed → Faster rotation of the rotor.
    
		- Lower switching speed → Slower rotation of the rotor.
    
		- This is like adjusting the RPM (Revolutions Per Minute) of the motor.
	- ###### Torque Control
		- Torque is proportional to current (more current = more torque).
    
		- The ESC increases current in the stator windings when more torque is needed.
    
		- If the motor faces a heavy load, the ESC automatically boosts current to maintain speed and overcome resistance.
