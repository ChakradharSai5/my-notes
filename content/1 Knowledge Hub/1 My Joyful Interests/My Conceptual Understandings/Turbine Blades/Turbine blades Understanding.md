# 1. First, let's establish what we are going to track

For every point in the turbine, we want to know:
- P — pressure
- T — temperature
- h — specific enthalpy
- s — entropy
- V — steam velocity
- quality x, once we enter the wet region
The most useful graph for this is actually the **Mollier h−s diagram**.
Remember the basic idea:

          h

          ↑

          │

          │       ●  State 1

          │       │

          │       │

          │       ●  State 2

          │        \

          │         ● State 3

          │

          └────────────────→ s

For an ideal adiabatic turbine stage, the h−s diagram tells us something extremely useful.

---

# 2. Let's start with steam entering the turbine

Imagine your main steam coming from the boiler:

HP steam
P = very high

T = very high

h = very high

V = relatively moderate
  

        ↓

  

     STATOR

        ↓

     ROTOR

For your NTPC type of plant, the main steam might be around:

P≈170kg/cm2 T≈537∘C

Don't worry about exact values for now. The important thing is:

high P + high T + high h​

# 3. Now steam enters the STATOR

This is the first part where the physics becomes interesting.

The stator is essentially a row of carefully shaped passages.

Think of one passage:

             Stator passage

  

	Steam       /             \

	───────→   /               \   ─────→

           \               /

            \_____________/

  

             nozzle-like

The pressure upstream is higher than downstream:

P1​>P2​

Therefore there is a pressure gradient:

high pressure→low pressure​

That pressure gradient accelerates the steam.

---

# 4. What happens to the steam's energy?

This is the most important thing to understand.

Before the stator:

high enthalpy

After the stator:

lower enthalpy

But the missing enthalpy hasn't disappeared.

It has become **kinetic energy**.

The basic energy equation is:

h+2V2​=constant

for an ideal stationary, adiabatic nozzle.

So:

Δh=2ΔV2​​

Conceptually:

BEFORE STATOR

  

Pressure/enthalpy energy

████████████████████

        ↓

        ↓

     STATOR

        ↓

        ↓

Kinetic energy

████████████████████

So after the stator:

P↓ h↓ T↓ V↑↑

while ideally:

s≈constant

---

# 5. This is the first important difference from the expansion valve

Remember our expansion valve discussion.

Across an expansion valve:

h1​=h2​​

because throttling is approximately isenthalpic.

But there is **no useful conversion into jet velocity**.

For a turbine stator:

h1​>h2​​

and the difference becomes kinetic energy.

That's a huge conceptual distinction.

### Expansion valve

	High P

	  │

	  │  throttling

	  ↓

	Low P


	h = CONSTANT

	### Turbine stator
	
	High P
	
	  │
	
	  │  expansion
	
	  │
	
	  ↓
	
	Low P

  

	h ↓
	
	V ↑

So the stator is **not a throttling valve**.

It is much closer to a **nozzle**.

---

# 6. What does the h-s diagram look like?

For an ideal stator:

             h

             ↑

             │

             │     ● 1

             │     │

             │     │

             │     │

             │     ● 2

             │

             └────────────→ s

Almost vertical downward.

Why?

Because ideal expansion is approximately:

s1​=s2​

while:

h2​<h1​

Real stator:

             h

             ↑

             │       ● 1

             │       │

             │       │

             │        \

             │         ● 2

             │

             └────────────→ s

Entropy increases slightly because of losses.

---

# 7. Now something VERY important happens

After the stator, steam is moving extremely fast.

For example, conceptually:

Before stator:

  

V = 50 m/s

  

After stator:

  

V = 500 m/s

Don't take those as actual values for your turbine; they're just to visualize the magnitude.

So now we have:

                 STATOR

  

	P ↓
	
	h ↓
	
	T ↓
	
	V ↑↑↑
	
	s ≈ constant

  

                 ↓

  

          HIGH VELOCITY STEAM

  

                 ↓

  

                ROTOR

Now we have reached the rotating blade.

---

# 8. What does the ROTOR do?

This is where the energy finally reaches the shaft.

Imagine the steam velocity vector entering the rotor:

                 V₁

                ↗

               /

              /

             ●

The rotor blade changes the velocity vector:

             ●

              \

               \

                ↘

                 V₂

Therefore:

V1​→V2​

More importantly, its **tangential component** changes.

That means the steam loses angular momentum.

And that angular momentum goes into the rotor.

---

# 9. This is the deepest physical picture

Imagine throwing a ball at a paddle.

Before:

ball ─────────→ paddle

After the paddle:

             ↖

              ball

The ball's momentum changed.

Therefore the paddle experienced force.

Exactly the same principle applies to the turbine.

Steam:

momentum changes​

Blade:

experiences force​

Rotor:

experiences torque​

Shaft:

produces power​

---

# 10. But what happens to the steam's thermodynamic properties in the ROTOR?

This is where we need to be careful.

There are **two kinds of turbine stages**.

## Impulse stage

Approximately:

Pin​≈Pout​

through the rotor.

The stator does most of the pressure drop.

        STATOR              ROTOR

  

	P ↓↓↓↓↓↓↓↓↓               P ≈ constant
	
	h ↓↓↓↓↓                   h ↓
	
	V ↑↑↑↑↑                   V ↓

                          ↓

                       shaft work

The rotor extracts the kinetic energy.

---

# 11. Reaction stage

In a reaction stage, the rotor itself also has a pressure drop.

So:

       STATOR                    ROTOR

  
	
	P ↓↓↓                      P ↓↓↓
	
	h ↓↓                       h ↓↓
	
	V ↑↑                       V changes

                           ↓

                        shaft work

The rotor passage itself behaves somewhat like a nozzle.

So:

pressure energy is converted to velocity inside the rotor too​

and simultaneously:

momentum change produces shaft work​

This is important because **large modern steam turbines aren't simply a sequence of pure impulse stages**. Their stages can have significant reaction.

---

# 12. So let's follow ONE complete stage

This is probably the diagram you were looking for.

             ONE TURBINE STAGE

  

       STATOR                 ROTOR

    ┌──────────┐           ┌──────────┐

    │          │           │          │

	───→│   /////  │──────────→│   \\\\   │───→

    │          │           │          │

    └──────────┘           └──────────┘

  

       ↓                       ↓

  

   P decreases             momentum changes

   h decreases             torque produced

   T decreases             shaft work

   V increases             V usually decreases

   s increases slightly    P may decrease

And the energy picture:

STATOR:

  

        h

        ↓

        ↓

        ↓

        └────→ kinetic energy

  

  

ROTOR:

  

kinetic energy

      ↓

      ↓

shaft work

---

# 13. Now put two stages together

This is where the turbine animation starts making sense.

             STAGE 1

  

Steam → STATOR → ROTOR

          ↓        ↓

       P ↓, V ↑   work

                   ↓

  

             STAGE 2


       STATOR → ROTOR

          ↓        ↓

       P ↓, V ↑   work

                   ↓

  

             STAGE 3

  

       STATOR → ROTOR

          ↓        ↓

       P ↓, V ↑   work

                   ↓

                  ...

Notice something:

### Every stage progressively lowers the steam pressure.

Something like:

P

  

	│ ●

	│   \

	│    ●

	│      \

	│       ●

	│         \

	│          ●

	│            \

	│             ●

	└──────────────────→ turbine stages

Similarly, temperature generally falls.

And enthalpy falls.

---

# 14. But what happens to velocity?

This is a subtle point.

You might think:

> "If every stage converts enthalpy into velocity, shouldn't velocity continuously increase?"

No.

Because the rotor extracts energy.

Think of one stage:

              STATOR             ROTOR

  

	V             ↑↑↑↑↑              ↓↓↓

              │                   │

              │                   │

──────────────┴───────────────────┴────→

The stator accelerates the steam.

The rotor extracts energy and changes its velocity vector.

Then the next stator accelerates it again.

So approximately:

Velocity

  

       /\        /\        /\

      /  \      /  \      /  \

     /    \    /    \    /    \

____/      \__/      \__/      \____

   S  R     S  R     S  R

This is a **very useful mental picture**.

---

# 15. Now let's look at the thermodynamics instead

Suppose we plot **enthalpy h** against turbine stage number.

Conceptually:

	h

  

	│ ●
	
	│   \
	
	│    ●
	
	│      \
	
	│       ●
	
	│         \
	
	│          ●
	
	│            \
	
	│             ●
	
	└────────────────────→ stage number

Enthalpy keeps decreasing.

Why?

Because the turbine is continuously extracting energy.

The total enthalpy drop becomes shaft work plus losses.

---

# 16. Pressure behaves similarly

	P
	
	  
	
	│ ●
	
	│   \
	
	│    \
	
	│     ●
	
	│       \
	
	│        \
	
	│         ●
	
	│           \
	
	│            \
	
	│             ●
	
	└────────────────────→ stages

Pressure continuously decreases through the turbine.

But **not necessarily uniformly**.

The actual pressure distribution depends on turbine design.

---

# 17. Now put everything on an h-s diagram

This is where the turbine becomes beautiful.

Imagine the steam begins here:

             h

             ↑

             │

             │ ● 1

             │ │

             │ │  STATOR

             │ ● 2

             │  \

             │   \ ROTOR

             │    ● 3

             │    │

             │    │ STATOR

             │    ● 4

             │     \

             │      ● 5

             │

             └────────────────→ s

But there is an important correction to the simple picture:

- **Stator:** approximately vertical downward for ideal isentropic expansion.
- **Rotor:** total/stagnation enthalpy decreases because work is extracted.
- Real processes move somewhat to the right because entropy increases due to friction, turbulence, leakage, etc.

So the real turbine trajectory gradually moves **downward and rightward**.

---

# 18. What happens to entropy?

This is another useful thing to track.

For an ideal turbine:

s=constant​

But real turbine:

s2​>s1​​

Why?

Because steam experiences:

- blade friction
- turbulence
- leakage
- mixing
- aerodynamic losses
- wet-steam losses in LP stages

So your real turbine is not perfectly reversible.

Therefore:

             h

             ↑

  

             ● ideal

             │

             │

             ● real

              \

               → s increases

  

             └────────────→ s

The farther right the real process moves, the more entropy has been generated.

---

# 19. Eventually we reach the wet-steam region

This is particularly important in the **LP turbine**.

Initially:

	Superheated steam

        ↓

        ↓

        ↓

	As pressure and temperature fall:
	
	Superheated
	
	     ↓
	
	Saturated vapour
	
	     ↓
	
	Wet steam
	
	     ↓
	
	more moisture
	
	On the Mollier diagram, you eventually enter the saturation dome.
	
	Conceptually:

                 h

                 ↑

                 │          superheated

                 │              ●

                 │             /

                 │            /

                 │       ____/ 

                 │      /    \

                 │     / wet  \

                 │    / region \

                 │___/__________\________→ s

Once inside the dome:

0<x<1

where x is dryness fraction.

For example:

x=0.90

means approximately:

- 90% vapour by mass
- 10% liquid water by mass

---

# 20. And this is why LP turbine blades are a problem

Now you can understand something from your plant.

The HP turbine receives:

high P

high T

superheated steam

But by the time steam reaches the LP turbine:

P ↓↓↓↓↓

T ↓↓↓↓↓

h ↓↓↓↓↓

and eventually:

steam becomes wet​

Those tiny water droplets can hit blades at high velocity.

That's why LP turbine moisture is undesirable.

---

# 21. And now reheating makes sense

This is why your plant doesn't simply expand steam continuously from boiler to condenser.

Instead:
	
	BOILER
	
	  │
	
	  │ high P, high T
	
	  ↓
	
	HP TURBINE
	
	  │
	
	  │ pressure ↓↓↓
	
	  ↓
	
	REHEATER
	
	  │
	
	  │ temperature ↑
	
	  ↓
	
	IP TURBINE
	
	  │
	
	  │ pressure ↓↓↓
	
	  ↓
	
	LP TURBINE
	
	  │
	
	  │ pressure ↓↓↓
	
	  ↓
	
	CONDENSER

The reheater is essentially saying:

> "We've expanded the steam and cooled it considerably. Before we continue expanding it, let's heat it back up."

Why?

Primarily to improve efficiency and **reduce moisture toward the later turbine stages**.

---

# 22. Now compare the entire turbine with the expansion valve you already understand

This comparison should make the distinction very clear.

### Expansion valve

             THROTTLING

  
	
	P ────────────────→ P ↓
	
	  
	
	h ─────────────────→ CONSTANT
	
	  
	
	T ↓

  

No shaft work

No useful acceleration

Entropy ↑

### Turbine

             EXPANSION + WORK

  
	
	P ↓↓↓↓↓
	
	h ↓↓↓↓↓
	
	T ↓↓↓↓↓
	
	  

         ↓

     part of h

         ↓

     kinetic energy

         ↓

     momentum change

         ↓

       torque

         ↓

     shaft work

  

Entropy ↑ slightly

That is the fundamental difference.

# 24. So here's the mental movie I want you to have

Imagine following **one kilogram of steam** through your turbine.

### Point 1 — entering stator

P = high

T = high

h = high

V = moderate

↓

### Point 2 — leaving stator

P ↓

T ↓

h ↓

V ↑↑

s ≈ same

The steam has been **accelerated**.

↓

### Point 3 — leaving rotor

momentum changed

V changes

tangential velocity decreases

shaft gets energy

h0 decreases

The steam has **given energy to the shaft**.

↓

### Point 4 — next stator

Again:

P ↓

h ↓

T ↓

V ↑

↓

### Point 5 — next rotor

Again:

momentum changes

shaft work

h0 ↓

↓

### Point 6 — repeat dozens of times
	
	STATOR → ROTOR → STATOR → ROTOR → STATOR → ROTOR
	
	   ↓       ↓        ↓       ↓        ↓       ↓
	
	  h↓     work      h↓     work      h↓     work
	
	  P↓               P↓               P↓
	
	Eventually:
	
	HIGH PRESSURE
	
	HIGH TEMPERATURE
	
	SUPERHEATED STEAM
	
	  
	
	        ↓↓↓
	
	  
	
	HP TURBINE
	
	  
	
	        ↓↓↓
	
	  
	
	REHEATER
	
	  
	
	        ↓↓↓
	
	  
	
	IP TURBINE
	
	  
	
	        ↓↓↓
	
	  
	
	LP TURBINE
	
	  
	
	        ↓↓↓
	
	  
	
	LOW PRESSURE
	
	WET STEAM
	
	  
	
	        ↓
	
	  
	
	CONDENSER

---

## The one diagram I would keep in your notes

	If we reduce the entire turbine to the same "fluid property thinking" that we used for the expansion valve, it is this:
	
	                    TURBINE
	
	  
	
	       STATOR                         ROTOR
	
	   ┌────────────┐                ┌────────────┐
	
	   │            │                │            │
	
	──→│  pressure  │─── fast steam →│ momentum   │──→
	
	   │   drop     │                │   change   │
	
	   │            │                │            │
	
	   └────────────┘                └────────────┘
	
	        │                              │
	
	        ↓                              ↓
	
	      P ↓                            Torque
	
	      h ↓                              ↓
	
	      T ↓                         Shaft work
	
	      V ↑
	
	      s ≈ const
	
	  
	
	                ↓
	
	  
	
	       NEXT STATOR → NEXT ROTOR
	
	                ↓
	
	       NEXT STATOR → NEXT ROTOR
	
	                ↓
	
	                    ...

### And on the thermodynamic level:

Stator: P↓, h↓, V↑, s≈const​ Rotor: h0​↓ because shaft work is extracted​

and for a **reaction rotor**, additionally:

P↓, h↓, V changes​

Then the process repeats.

---
