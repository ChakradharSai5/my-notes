# 1. Does a pressure gradient accelerate steam in a nozzle and in a throttling valve?

## First: yes, a pressure gradient can accelerate fluid

Take a tiny fluid element:

       P high                         P low

          →                             →

        ┌─────┐

        │ fluid│

        └─────┘

          ───────────────→

Pressure on the upstream side pushes harder than pressure on the downstream side.

So the net force is:

F=(P1​−P2​)A

and therefore the fluid accelerates.

This is the basic mechanism in a **nozzle**.

---

## But what about a throttling valve?

Here's the subtlety:

### There absolutely can be a very large local acceleration inside a valve.

Fluid approaching the narrow opening can accelerate dramatically:

        valve

  

───────\       /───────

        \     /

         \   /

          \ /

           ↓

          jet

So your instinct was correct:

> **A throttling valve can produce a high-velocity jet locally.**

The difference is **what happens to that kinetic energy afterward**.

A nozzle is designed to **use the pressure drop to create and preserve useful kinetic energy**.

A throttling valve is designed to **destroy pressure availability without extracting useful work**.

That distinction is crucial.

---

# 2. So what actually happens through a throttling valve?

Let's take a simple valve.

POINT 1                 POINT 2

  

High P                  Low P

                       ────────

───────●───[ VALVE ]──────●────→

The governing steady-flow energy equation is:

h1​+2V12​​=h2​+2V22​​

if we neglect heat transfer, shaft work and potential-energy change.

For a normal throttling valve, the useful approximation is:

h1​≈h2​​

Why?

Because the valve does **not extract shaft work**.

And the kinetic energy generated in the narrow restriction is largely dissipated as turbulence and viscous losses after the restriction.

So you can imagine:

Valve interior:

  

pressure energy

      ↓

temporary high velocity

      ↓

turbulence + friction

      ↓

random molecular energy

  

Net result:

  

P ↓↓↓

h ≈ constant

s ↑

That temporary velocity does **not** become useful turbine shaft power.

---

# 3. Nozzle vs throttling valve

This is perhaps the cleanest distinction:

### Nozzle

The purpose is:

pressure/enthalpy energy → directed kinetic energy​

### Throttling valve

The purpose is:

pressure reduction → without useful work​

So physically they can look similar:

       narrowing passage

  

───────\       /───────

        \_____/

but thermodynamically they are very different devices.

---

# 4. Here is a very useful comparison

Suppose upstream enthalpy is 3000 kJ/kg.

### Ideal nozzle

Perhaps:

h1​=3000 h2​=2800

The missing:

200kJ/kg

has largely become kinetic energy.

So:

2V22​−V12​​≈200kJ/kg

That is **useful directed velocity**.

---

### Throttling valve

Instead:

h1​≈h2​≈3000

Even though fluid may briefly become very fast inside the valve.

The velocity energy is subsequently dissipated.

So there is no useful net conversion:

pressure drop without corresponding enthalpy drop​

This is why throttling is called **isenthalpic** rather than isentropic.

---

# 5. Now your enthalpy question — this is VERY important

You said:

> Enthalpy is internal energy + pressure × volume, right?

Exactly.

Per unit mass:

h=u+Pv​

Now you asked:

> If stator decreases enthalpy, while energy is converted to velocity, how come?

This is where we need to distinguish **static enthalpy** from **total/stagnation enthalpy**.

This is the missing piece.

---

# 6. Think of total energy per kg

For flowing fluid:

E=u+Pv+2V2​+gz​

Since:

h=u+Pv

we get:

E=h+2V2​+gz​

Usually in a turbine/nozzle we can ignore elevation:

E=h+2V2​​

Now everything becomes intuitive.

Suppose initially:

h=3000

and:

V=100m/s

Then kinetic energy is:

2V2​=5kJ/kg

approximately.

So total:

3005kJ/kg

After the stator:

h=2800

and perhaps:

V=630m/s

Then:

2V2​≈198kJ/kg

Total:

2800+198≈2998

approximately the same apart from losses.

### So what happened?

The **static enthalpy decreased**.

The **kinetic energy increased**.

The total energy stayed approximately constant.

That's the answer.

---

# 7. So is kinetic energy "inside enthalpy"?

No.

This is the important distinction.

h=u+Pv​

does **not** contain macroscopic flow kinetic energy.

Kinetic energy is a separate term:

2V2​​

So:

TOTAL ENERGY

│

├── Internal energy       u

├── Flow work             Pv

│     └── together = h

│

├── Kinetic energy        V²/2

│

└── Potential energy      gz

Thus:

h+2V2​+gz​

is the complete mechanical/thermodynamic energy expression for the flowing fluid.

---

# 8. Then why do engineers often say "enthalpy converts to kinetic energy"?

Because in a nozzle:

h1​+2V12​​=h2​+2V22​​

Therefore:

h1​−h2​=2V22​−V12​​​

So it's convenient shorthand to say:

> "Enthalpy is converted into velocity."

But more precisely:

> **A decrease in static enthalpy accompanies an increase in macroscopic kinetic energy while total enthalpy remains approximately constant.**

That's the rigorous statement.

---

# 9. And now the stator question

You asked:

> Is the stator also like rotor but stagnant?

**Yes, physically the stator is a stationary blade passage, while the rotor is the same sort of flow passage attached to a rotating structure.**

But their jobs differ because one is stationary and one is rotating.

Think:

STATOR

  

fixed blades

||||||||||||

  

ROTOR

  

rotating blades

///////////

↻ ↻ ↻ ↻ ↻

The stator can redirect and accelerate the flow, but because it isn't rotating:

no shaft work is produced by the stator​

The rotor can exchange energy with the flow and therefore produce shaft work.

---

# 10. But you made a brilliant objection:

> "If steam hits a stationary blade, shouldn't it lose energy, like a ball hitting a wall?"

**Yes. It does lose some useful energy.**

Your intuition is correct.

The stator is absolutely **not lossless in reality**.

Steam flowing through it encounters:

- viscosity
- boundary-layer friction
- turbulence
- separation
- shock losses in some situations
- surface friction

Therefore:

s2​>s1​​

and the actual exit velocity is lower than the ideal velocity.

# Do all thermodynamic diagrams have domes?

**No.**

This is important.

You will see saturation domes on many common diagrams for water and refrigerants, such as:

T−v P−v T−s h−s

and refrigerant P−h charts.

But the exact appearance is different.

And some diagrams don't show a dome at all in the form you're used to.

# So which diagrams should YOU know for mechanical equipment?

For power plant work, I would organize them like this.

## 1. P−h diagram

Very useful for:

- refrigeration
- compressors
- expansion valves
- condensers
- evaporators

Especially useful when thinking:

P↔h​

Your expansion-valve discussion used this.

---

## 2. T−s diagram

Extremely useful for:

- Rankine cycle
- turbines
- compressors
- heat addition
- heat rejection
- entropy generation

Because:

δqrev​=Tds​

So heat-transfer processes become visually intuitive.

For the ideal Rankine cycle, for example:

T

↑

│           3

│           │

│           │

│      2────┘

│      │

│      │

│      1────────4

│

└────────────────→ s

---

## 3. h−s diagram — Mollier diagram

This is probably **the most useful diagram for you for steam turbines**.

Why?

Because turbine work is strongly tied to enthalpy drop:

Wt​≈hin​−hout​​

and entropy tells you how much irreversibility exists.

So:

h

↑

│

│  turbine expansion

│       ↓

│       ●

│       │\

│       │ \

│       │  ●

│

└────────────────→ s

This is why turbine engineers love Mollier charts.

---

# 21. 4. P−v diagram

Useful when thinking about:

- compression/expansion
- piston-cylinder systems
- boundary work

Because:

W=∫Pdv​

The area under the curve represents work for a closed system.

For turbines it's generally less convenient than h−s.

---

# 22. 5. T−v diagram

Useful mainly for:

- phase-change behaviour
- critical point
- liquid/vapour behaviour

Less common in day-to-day power-plant equipment analysis.

---

# 23. 6. Psychrometric chart

For:

- air conditioning
- cooling towers sometimes indirectly
- humid air
- HVAC

It tracks things like:

Tdb​,Twb​,RH,ω,h

For your AC/refrigeration understanding, this becomes useful once we move from **pure refrigerant** to **air + water vapour**.

---

# 24. So there isn't one universal "best" diagram

This is the rule I would use:

|Problem|Usually useful diagram|
|---|---|
|Steam turbine|**h-s**|
|Rankine cycle|**T-s / h-s**|
|Compressor|**h-s / P-h**|
|Refrigeration cycle|**P-h**|
|Expansion valve|**P-h**|
|Condenser/boiler|**T-s / h-s**|
|Piston engine|**P-v**|
|Phase behaviour|**P-v / T-v / T-s**|
|HVAC air|**Psychrometric chart**|

But don't treat this as a rigid law. Engineers often use several simultaneously.

---

# 25. And now we can answer your whole chain of questions with one energy diagram

This is the most fundamental picture:

                 FLOW ENERGY

  

       ┌───────────────────────────────┐

       │                               │

       │   h = u + Pv                  │

       │                               │

       │   +                           │

       │                               │

       │   V²/2                        │

       │                               │

       └───────────────────────────────┘

                       │

                       ↓

                 TOTAL ENERGY

  

  

STATOR:

  

h ↓↓↓

   │

   └────────→ V²/2 ↑↑↑

                  +

                losses

  

  

ROTOR:

  

V²/2 + pressure/enthalpy

          │

          ↓

      shaft work

  

          +

        losses

And in a real turbine:

total energy in=shaft work+total energy out+losses​

---

## One correction to keep firmly in your head

The phrase **"enthalpy converts into kinetic energy"** is useful but potentially misleading.

The more precise statement is:

h+2V2​=approximately constant through an ideal stationary nozzle​

Therefore, when:

V↑

then:

h↓

The energy has not mysteriously come out of enthalpy. **The total energy is simply being redistributed between the thermodynamic state energy represented by h and macroscopic flow kinetic energy.**