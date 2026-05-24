# Aerocapture and Atmospheric Entry Subsystem — ARES V4.0

`CLASSIFICATION: Systems Engineering Design Specification`
`TARGET: Martian entry and Earth re-entry velocity management for 2030 flight envelope`

## 1. Thermodynamic Profile and Ablative Aerothermal Shielding

To maximize payload mass fractions, ARES V4.0 bypasses chemical propulsion brake cycles at Mars and Earth, utilizing atmospheric friction (**Aerocapture**) to enter stable parking orbits.

*   **Entry Velocity Profile ($v_e$):** Peak entry at Mars interface begins at **$7.2 \text{ km/s}$**. Earth re-entry profile scales to **$11.2 \text{ km/s}$**.
*   **Peak Heat Flux Generation:** Extreme kinetic compression impacts the 9-meter hull, scaling aerothermal heat generation to **$450 \text{ W/cm}^2$** at Mars entry corridor.
*   **Thermal Protection System (TPS) Matrix:** 
    *   **Primary Nose Cap and Leeward Ribs:** Rigid Carbon-Carbon (C-C) tiled arrays matrix providing multi-use structural integrity up to 2200 K.
    *   **Windward Hull Surface:** Phenolic-Impregnated Carbon Ablator (**PICA-X standard**) advanced layer. This ablatible matrix dissipates thermal load smoothly via chemical pyrolysis, scaling structural safety factors to 1.5.
## 2. Dynamic Mechanical Stowage: Mirror Protection Protocol

The 2x Solar Thermal Propulsion (STP) inflatable parabolic mirror assemblies are highly vulnerable to hypersonic aerodynamic loads. 

[Deep Space Cruise Mode] -> Mirrors Deployed (2500 m² total exposure area)
|
[Atmospheric Entry Ingress T-6 Hours] -> Active Helium venting initiated by ODIN AI
|
[Mechanical Desegregation] -> Rigid support masts telescoped back into central bulkhead
|
[Hermetic Hull Closure] -> Reinforced PICA-coated mechanical doors locked and sealed
## 3. Martian Atmosphere Trajectory Corrections

Due to the extreme volatility and low density of the Martian CO₂ atmosphere, ARES V4.0 features mid-entry guidance using **Reaction Control System (RCS) gas thruster blocks**:

*   **Hypersonic Lifting Body Dynamics:** The nose profile of the 9m hull is asymmetric, generating a lifting ratio ($L/D \sim 0.24$). By rotating the ship along its roll axis, the ODIN flight guidance vector modulates lift to stay strictly within the entry corridor corridor window, eliminating skip-out risks.
