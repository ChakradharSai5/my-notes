---
{}
---
- Here very similar to [[AC Motor#Synchronous Motor]] but in reverse, instead of sending current of 3 ph from stator, we take supply of 3ph from stator, and for doing that, we rotate the rotor forcibly with help of turbine, in [[AC Motor#Synchronous Motor]], we get the rotation from thing, here we make the rotation and we get the electricity
- ### Excitation system
- Basically you have to understand, we need to give rotor a DC current to rotor, ideally we need to place magnets on rotor, because this magnetic field from rotor cutting through stator coil is what is getting our stator terminal voltage in generator, but we cannot have such big magnets and we cannot also control the power of magnetic field as it will be "permanent" magnets, so we prefer making magnets by sending current to a rotated coil so that we can control the magnetic field by adjusting the amount of current through it, only then 3 phase gets generated in stator, the system that gives DC to rotor is what "excites" to get our required generator stator output, hence, it is called "Excitation system"
- but here how to give DC to rotor
- for that we have two ways 1. brushed
						2. brushless
#### Brush excitation system
- Here we simply take out put from the generator out put voltage, and stepdown by Excitation transformer, after stepping down, we convert this AC to DC, and that DC as rotor is rotating, DC is given through brushes
- And that makes the coil on the rotor behave like magnet and so this makes current in generator![[Screenshot 2025-12-05 080937.jpg]]
- that FF thing is something i don't know, i guess no need to know now, rest all is self explanotory.
- 

#### Brushless excitation system

![[Screenshot 2025-12-05 072508.jpg]]
- Brushless mean, we want to skip using brushes, for that we made a jugaad
- Ultimately we want to give DC to rotor right?, how to give DC to rotor without touching it, through faraday's law as rotor is rotating, if we can place  permanent magnet on stator, this we call main excitor, that will generate AC to rotor coils, but we want DC, let us convert that AC to DC using diode wheels placed on the rotor itself and then give that to main rotor part where our stator coils of generator is present
- Now ok, we need DC to give to main excitor stator, for that instead of getting DC from outside somewhere, let us get that DC by doing AC to DC conversion from this rotating rotor, - which we call pilot excitor,- where we put small permanent magnets, and put coils on the stator, like we did for generator, only difference here we use permanent magnets as we want less voltage, so using this permanent magnets on the rotor and so cutting magnetic field of stator, we get three outputs from stator, that AC we give to AVR and get DC from it and this DC shall be given to main excitor stator, so that as rotor is rotating with coils on it, will generate AC on the rotor coils, that as already discussed will go to diode wheels and convert to DC and that is given to rotor coil of our generator
- note that we use 16PMG on pilot excitor that gives 400Hz reason being to mitigate ripple effect while AC to DC conversion, same reason for 6 pole excitor in main excitor also.
- That Q axis coil reason to measure current or something like that, we don't need that much details, this is enough