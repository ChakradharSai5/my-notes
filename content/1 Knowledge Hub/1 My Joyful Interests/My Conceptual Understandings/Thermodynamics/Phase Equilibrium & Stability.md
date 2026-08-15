- This is one of those concepts, that has different understanding than conventional.
- This can be understood best with an example
- At Expansion valve in [[AC working mechanism]], as you may notice, the pressure before the valve is say 10ksc, 40DegC, what expansion valve does is, it simply has a nozzle that allows to drop the pressure drastically, which results in phase change.
- Here comes the crazy part, upstream to Expansion valve in [[AC working mechanism]], the Freon - General term for all AC refrigerants  - shall be in liquid state, once it passes through Expansion valve it changes to vapor form, and temperature drops drastically to say 5DegC.
- refer [[1 Thermodynamic State & Degrees of Freedom]], from that you realize, for non flowing single phase fluid we can have 
- Now this happens because, that any particular fluid has a fixed stable phase at a certain pressure and temperature. Now here, what we are doing is, we are making a fluid, which has stable fluid state of liquid at a certain pressure and temperature, and suddenly using Expansion valve, we are forcing it to enter a low pressure state, it is bound to enter at least partial conversion to vapor, and this conversion requires energy and this energy it takes from heat energy from the fluid itself and so the fluid temperature drops from 40DegC to 5DegC in our example
# Here's a beautiful way to visualize it
refer [[0 My Take on Thermodynamics]]
Imagine your thermodynamic state space.

Before:

```
P = 16 bar
T = 35°C
h = h₁
100% liquid
```

The valve imposes:

```
P = 2 bar
```

But throttling imposes:

```
h ≈ h₁
```

So now nature searches for the state satisfying both:

```
P = 2 bar
h = h₁
```

That intersection gives you the actual:

```
T = ?
phase = ?
```

And suppose that intersection lies inside the saturation dome.

Then:

```
P = 2 bar
T ≈ 5°C
some liquid + some vapor
```

That is why **temperature has become tied to pressure** in the two-phase region.
The important idea is:

> **The pressure determines the temperature at which liquid and vapor can coexist in equilibrium.**

So "boiling point" is really just a convenient name for a particular **liquid-vapor equilibrium temperature at a specified pressure**.

Change the pressure → the equilibrium temperature changes.

This is why thinking in terms of "stability" is useful for understanding refrigeration and steam systems.

Instead of thinking:

> "The expansion valve lowers the boiling point."

Think:

> "The expansion valve lowers the pressure, so the refrigerant now has a different equilibrium condition. The old liquid state is no longer the stable state, so the refrigerant moves toward the new equilibrium state."
- [[Thermodynamic State & Degrees of Freedom]]
- [[Saturation, Quality & Superheat]]
- [[Valve Throttling Losses]]
- [[Enthalpy]]
- [[Vapor Compression Refrigeration]]