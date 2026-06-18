---
{}
---
Generator protection is broadly classified into three types: Class A, B, and C, 
In this, normally when we trip the unit, during shut down, that comes under Class B, which means, we trip the turbine first, and so Turbine Stop valves gets closed, and so the complete energy from turbine gets exhausted through generator to grid throuhg GCB (Of course), and then, GCB gets open I think on low forward power relay.
But Class A is the type of protection, where instead of exhausting this energy, and let the turbine stop in stable manner, if our priority is to save generator or any related electrical equipment, then those type is called Class A type, where GCB trips first, and then SV gets closed, of course all happen in millisecond difference probably.
# Class A
- Generally, electrical faults of the generator, generator transformer and unit auxiliary transformer will lead to Class A tripping.
- In this tripping mode, the generator and turbine will be **tripped simultaneously and instantly**. which may cause slight turbine overspeed as energy of current running MW load entrapped in turbine makes turbine to rotate and so may cause overspeed, so slightly unsafe
- Ex: stator earth fault and the differential fault in a generator are the faults that show problems in the generator winding

## Class A1
Class-A1 comprises the faults that need immediate isolation of the **generator**

- **Generator Differential Protection(87G)**
    The relay detects winding faults by identifying discrepancies in the stator winding's incoming and outgoing current..

- **Generator Over Voltage Protection(59)**
    sudden load throw-off, lightning strike, AVR malfunctioning, and turbine over speed etc.

- **100% Stator Earth Fault Protection(64G2)**

- **95% Stator Earth Fault Protection (64G1)**

- **Starting Over Current Protection**

### Actuation of Class-A1 protection
- Trip GCB
- Tripping FCB
- Turbine Tripping
## Class A2
Faults in the generator transformer(GT), isolated phase bus duct(IPBT), and unit transformer(UT)
- Over fluxing Protection of Generator
- Back up Impedance Protection of Generator
- GT
    - Differential Protection of GT
    - Buchholz Relay of GT
    - [PRD](https://www.electricalvolt.com/2019/12/prd-of-transformer-pressure-relief-device-for-transformer/) of GT
    - Trip from OTI & WTI of GT
    - Fire protection of GT
- UT
    - Differential Protection of UT
    - Buchholz Relay & PRD of Main Tank of UT
    - Trip from OTI & WTI of UT
    - Fire protection of UT

### Actuation of Class-A2 protection

- Trip GCB
- Tripping FCB
- Tripping GT circuit breakers
- Tripping UT LV circuit breakers
- Turbine Tripping

# Class B
- Class B tripping is followed for all turbine faults which are mechanical in nature
- for which it is safe to first trip the turbine and then the generator through low **forward power interlock relay 32F**
- this will ensure that energy trapped in turbine gets completely exhausted and finally then closing stop valves will ensure turbine not to overspeed
    - **The problem in the turbine or in the steam process**
    - **Loss of generator Excitation(40G)**
    - **Rotor Earth fault (64F)**

# **Class-C**
To isolate the generator if the fault is in the grid
- Under Frequency (81G)
- Over frequency(81G))
- Negative Phase Sequence or Unbalance(46)
- Back up Impedance Protection(21)
When Class-B protection acts first turbine trips that sends signal to generator to trip through relays 186/286B through LFP interlock, and as it is class-B again generator will **not** return trip signal to turbine
- and this 186/286B need to be in reset for excitation
- and this won’t get reset unless turbine gets reset, that is SV gets open
- so it is recommended to first reset turbine, then roll it, then just before exciting, reset this 186 and 286B - so that extra protection in inadvertent closing of GCB