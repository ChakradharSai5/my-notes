---
dg-publish: true
draft: false
---
Here's a detailed breakdown of the normal scheduling of power from a generator's perspective and how RRAS gets activated in real-time in relation to it:

### Normal Power Scheduling (Day-Ahead)
Power scheduling follows a standardized process as laid out by the Indian Electricity Grid Code (IEGC) for day-ahead scheduling. Here are the time details:
- Before 10:00 AM: 
	- Power generators submit their declared capacity (DC) to the respective Regional Load Dispatch Centers (RLDCs) for the next day. This includes the available generation capacity they can provide for each 15-minute time block.
- Before 11:00 AM: 
	- The distribution utilities (DISCOMs), which are the buyers of power, submit their demand forecasts to the RLDCs, indicating how much power they will need for the next day.
- By 12:00 Noon: 
	- RLDCs start preparing the day-ahead schedule based on the information provided by generators and buyers (DISCOMs).
- By 3:00 PM: 
	- The initial day-ahead generation and consumption schedule for the next day (split into 96 time blocks, each of 15 minutes) is finalized by the RLDCs. This is sent back to generators and DISCOMs.
- By 6:00 PM: 
	- The National Load Dispatch Centre (NLDC) prepares a merit order stack of generators for Reserves Regulation Ancillary Services (RRAS) for the next day. This stack is sorted by:
- Up Regulation: Generators with the lowest variable cost.
- Down Regulation: Generators with the highest variable cost.
- Post 6:00 PM: 
	- Minor adjustments or revisions in scheduling can happen until midnight before the schedule becomes operational from 0000 hours (start of the next day).
### Real-Time Operations and How RRAS Gets Affected
While day-ahead scheduling provides a stable framework for power generation, real-time grid conditions can vary due to factors like demand surges, transmission line trips, or frequency deviations. This is where RRAS comes into play.

#### RRAS Activation in Real-Time
RRAS is triggered in real time to manage grid stability and congestion based on specific triggers. Here’s how it works:

#### Monitoring in Real-Time:
The NLDC and RLDC continuously monitor grid parameters like frequency (should ideally be around 50 Hz), line loadings, and demand-supply balance.

- Triggering Criteria:
	- If the frequency drops below 49.90 Hz, there is a shortfall of power in the system, and Up Regulation is triggered.
	- If the frequency rises above 50.05 Hz, there is an excess of power, and Down Regulation is triggered.
#### Real-Time Dispatch of RRAS:
- Up Regulation (Increasing Generation): NLDC selects generators from the day-ahead merit order stack (with the lowest cost first) and asks them to increase power generation. This is typically done when there's a power shortage in the system.
- Down Regulation (Decreasing Generation): If there is excess power, NLDC instructs generators (from the highest cost downwards) to reduce power generation.
#### RRAS Scheduling in Real-Time:
- Once RRAS is triggered, RLDCs revise the schedule of the affected RRAS provider. The revision comes into effect within 15 minutes of the instruction, ensuring rapid adjustment.
- This means RRAS dispatches are incorporated directly into the revised schedules, ensuring quick responses to deviations from the day-ahead plan.
#### Summary of Real-Time RRAS Activation in Normal Scheduling
- Normal scheduling is a planned, day-ahead process that sets the base power generation for the grid.
- RRAS is triggered in real-time when unexpected deviations (like frequency drops or surges) occur, and generators need to adjust their output within 15 minutes of being instructed.
- The day-ahead merit order stack ensures that cost-efficient generators are picked first for Up Regulation and high-cost generators for Down Regulation, optimizing cost and response time.
- This dual system of planned scheduling and real-time regulation keeps the grid balanced and stable, ensuring continuous, reliable power supply.
