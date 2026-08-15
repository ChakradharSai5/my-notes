## Big Picture

An air conditioner does not create "cold".

It **moves heat from the room to the outside** using a refrigerant and external work supplied by the compressor.

The refrigerant continuously circulates through four main components:

**Evaporator → Compressor → Condenser → Expansion Valve → Evaporator**
![[AC parts.jpg]]
The refrigerant is useful because its equilibrium between liquid and vapor changes strongly with pressure. By controlling its pressure, we can make it evaporate at a low temperature inside the room and condense at a higher temperature outside.
![[E-H.jpg]]
See:

- [[Phase Equilibrium & Stability]]
    
- [[1 Thermodynamic State & Degrees of Freedom]]
    
- [[Enthalpy]]
    
- [[Valve Throttling Losses]]
    
- [[Latent Heat & Phase Change]]
    
- [[P-H Diagram]]
    

---

## 1. Evaporator — Removing Heat From the Room

The evaporator is the indoor coil.

Before entering it, the refrigerant is at:

- Low pressure
    
- Low temperature
    
- Usually a liquid-vapor mixture
    

The room air is warmer than the refrigerant.

Therefore heat naturally flows:

**Room air → refrigerant**

The indoor fan forces room air across the evaporator coil, increasing the rate of heat transfer.

The absorbed heat causes the refrigerant to evaporate:

**Liquid → Vapor**

This is similar to the intuition of ice melting:

**Ice + heat → water**

except the refrigerant uses:

**Liquid + heat → vapor**

The important point is that the refrigerant is not simply "cold because it is liquid". It is cold because, at the low pressure created by the cycle, its equilibrium temperature is low.

As the refrigerant absorbs heat, its enthalpy increases.

See:

- [[Phase Equilibrium & Stability]]
    
- [[Saturation, Quality & Superheat]]
    
- [[Enthalpy]]
    
- [[Latent Heat & Phase Change]]
    

---

## 2. Compressor — Restoring High Pressure

The refrigerant leaves the evaporator as low-pressure vapor.

The compressor takes this vapor and compresses it.

The compressor does **not directly turn gas into liquid**.

Instead:

**Low-pressure vapor → High-pressure, high-temperature vapor**

External work from the motor enters the refrigerant.

This raises its thermodynamic energy/enthalpy and also raises its temperature.

The hot gas is now ready to reject heat to the outside.

---

## 3. Condenser — Rejecting Heat Outside

The hot, high-pressure refrigerant enters the outdoor condenser coil.

The outdoor air is cooler than the refrigerant, so heat flows:

**Refrigerant → outside atmosphere**

The outdoor fan forces atmospheric air across the condenser, increasing heat transfer.

As the refrigerant rejects heat, it condenses:

**Vapor → Liquid**

Therefore:

**Compressor:** gas → high-pressure hot gas

**Condenser:** hot gas → high-pressure liquid + heat rejected outside

The compressor therefore does not "make the liquid"; the condenser is where condensation happens.

---

## 4. Expansion Valve — Creating the Low-Pressure State

Now we have high-pressure liquid refrigerant coming from the condenser.

The expansion valve restricts its flow and creates a large pressure drop.

For example, conceptually:

**Before valve:**

16 bar, 35°C, high-pressure liquid

**Valve imposes:**

16 bar → 2 bar

The important question is:

> If the valve directly changes pressure, why does temperature also change?

The answer is the central idea of throttling.

The valve directly imposes the new pressure.

At the same time, the throttling process approximately preserves enthalpy.

Therefore the refrigerant leaving the valve has:

- A new pressure
    
- Approximately the same enthalpy
    

These two conditions determine the new thermodynamic state.

In other words:

**New pressure + conserved enthalpy → new state**

From that new state, nature determines:

- temperature
    
- phase
    
- liquid/vapor fraction
    
- other thermodynamic properties
    

See:

- [[Valve Throttling Losses]]
    
- [[Thermodynamic State & Degrees of Freedom]]
    
- [[Enthalpy]]
    

---

## 5. Why Does the Refrigerant Become Cold After the Expansion Valve?

Suppose the new pressure is so low that the refrigerant's liquid-vapor equilibrium temperature is only around 5°C.

The original high-pressure liquid state is no longer the equilibrium state at the new pressure.

The refrigerant therefore moves toward the new stable equilibrium state.

Some of the liquid immediately flashes into vapor.

This is called **flash evaporation**.

For example, purely as an illustration:

**1 kg liquid → 0.8 kg liquid + 0.2 kg vapor**

The 20% is not a fixed value; the actual amount depends on the refrigerant, inlet state and final pressure.

The energy needed for part of the liquid to evaporate comes from the refrigerant's own thermodynamic state.

The valve itself is not acting as a heat sink.

It is not:

**Refrigerant heat → valve → atmosphere**

Instead:

**Pressure drops → old state is no longer the equilibrium state → some liquid flashes into vapor → refrigerant reaches a cold low-pressure equilibrium state**

---

## 6. Why Does Pressure Determine the Temperature in the Two-Phase Region?

Once liquid and vapor coexist in equilibrium, their pressure and temperature cannot be chosen independently.

At a given pressure, there is one corresponding saturation temperature.

Therefore:

**Pressure → saturation temperature**

For example, conceptually:

**2 bar → around 5°C saturation temperature**

The exact value depends on the refrigerant.

But pressure alone still does not tell us how much of the refrigerant is liquid and how much is vapor.

That requires another property such as enthalpy or quality.

Therefore, after throttling:

**Pressure + enthalpy → complete thermodynamic state**

and, if the state lies inside the saturation dome:

**Pressure → temperature**

while:

**Enthalpy → liquid/vapor fraction**

See:

- [[Phase Equilibrium & Stability]]
    
- [[Saturation, Quality & Superheat]]
    
- [[Thermodynamic State & Degrees of Freedom]]
    
- [[P-H Diagram]]
    

---

## 7. Evaporator Completes the Process

The cold liquid-vapor mixture enters the indoor evaporator.

The room is warmer, so room heat enters the refrigerant.

That added heat evaporates more of the remaining liquid.

Thus:

**Cold two-phase refrigerant + room heat → vapor**

The refrigerant leaves the evaporator as vapor and returns to the compressor.

The cycle repeats.

---

# The Complete Physical Story

The AC can therefore be understood as:

**1. Condenser**

Get refrigerant back into a high-pressure liquid state while rejecting heat outside.

↓

**2. Expansion Valve**

Force the pressure down.

The new pressure creates a new equilibrium condition.

The refrigerant flashes partly into vapor and becomes cold.

↓

**3. Evaporator**

Put this cold refrigerant next to the warm room.

It absorbs room heat and evaporates.

↓

**4. Compressor**

Compress the resulting vapor back to high pressure and high temperature.

↓

**5. Condenser**

Reject the room heat plus compressor input energy outside.

And repeat.

---

# The Energy Picture

The room supplies heat to the refrigerant.

The compressor supplies additional energy.

The condenser ultimately rejects both to the outside:

**Room heat + compressor work → outside**

Therefore the outdoor unit must reject **more heat than the indoor unit removes from the room**.

This is why the air coming from the outdoor unit can be hotter than the surrounding atmosphere.

---

# Most Important Mental Model

Do not think:

> "Expansion valve makes the refrigerant cold."

Think:

> **The expansion valve changes the pressure. The throttling condition keeps enthalpy approximately constant. The refrigerant must then find the equilibrium state corresponding to the new pressure and enthalpy. That new state may be a cold liquid-vapor mixture, which is then used in the evaporator to absorb room heat.**

The valve therefore **creates the conditions necessary for refrigeration**; the evaporator performs the actual heat absorption from the room.

See:

- [[Valve Throttling Losses]]
    
- [[Phase Equilibrium & Stability]]
    
- [[Enthalpy]]
    
- [[P-H Diagram]]