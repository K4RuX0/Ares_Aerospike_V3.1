# Changelog - ARES-SPACE TRANSPORT

All notable changes to the conceptual architecture of the transport vehicle and its integrated logistics missions will be documented in this file.

## [4.0.0-commercial] - 2030-05-24

### Added
- **Low-Cost Green Architecture (Horizon 2030)**: Complete replacement of the nuclear thermal propulsion (NTR) system with highly cost-effective Solar Thermal Propulsion (STP), eliminating regulatory bureaucracy, excessive insurance costs, and radiological hazards at Alcantara.
- **Liquid Methane ($LCH_4$) Migration**: Propellant shifted from molecular hydrogen to liquid methane. Methane is 6 times denser, reducing structural tank volume within the 9-meter fuselage and lowering logistical supply costs.
- **Two-Phase Modular Logistics**:
  * **Phase I (Lunar Mission)**: Autonomous cislunar round-trip with zero refueling, carrying up to **55 metric tons** of net payload.
  * **Phase II (Mars Mission - Project Prometheus I)**: High-energy Trans-Mars Injection (TMI) maneuver carrying **71 metric tons** of pure payload.
- **Zero-Corrosion Engineering**: Expansion chamber built from refractory **Tantalum-Hafnium Carbide ($Ta_4HfC_5$)** ceramic alloy, shielded internally with an atomic thin-film of **Iridium** to eliminate chemical fatigue under ultra-high temperatures.
- **Active Zero Boil-Off (ZBO) Technology**: Integration of Multi-Layer Insulation (MLI) and active helium-looped pulse tube cryocoolers to cancel out cryogenic methane evaporation in deep-space environments.

### Changed
- **Engine Count**: 4 nuclear fission reactors → Dynamic redundant cluster of **2 Solar Thermal Propulsion (STP) units**.
- **Combined Thrust (LEO)**: 740 kN → **370 kN** (calibrated dynamically based on inverse-square law solar flux at 1.0 AU).
- **Real Specific Impulse ($I_{sp}$)**: 920s (theoretical hydrogen fission target) → **620s** (calculated via real isentropic thermodynamic expansion of superheated methane at 3200 K).
- **Airframe Dry Mass**: 185.0t → **120.0t** (drastic mass reduction by completely eliminating heavy radiation shielding and reactor core dead weights).
- **Tank Structural Mass**: 95.0t → **75.0t** (compacted Al-Li alloy tanks due to the higher volumetric density of liquid methane).
- **Propellant Capacity**: 1127.0t ($LH_2$) → **1130.0t** ($LCH_4$).
- **Total LEO Gross Weight**: 1407.0t → **1325.0t** (significantly lighter and more agile vehicle profile).

### Fixed
- **Gas Expansion Physics**: The algorithm now correctly processes real fluid behavior utilizing the specific molecular thermal properties of superheated methane ($\gamma = 1.32$, $R = 518.3 \text{ J/kg·K}$).
- **Thermal Leakage Modeling**: Replaced generic approximations with heat transfer calculations based on real $0.001$ MLI transmittance and active cryocooler Coefficient of Performance (COP) at 110 K.
- **Front-End Rendering Artifacts**: Removed broken external badge images from the README and replaced them with stable native Markdown tables.

---

## [3.1.0-heavy] - 2026-05-22

### Added
- **740kN Heavy Configuration**: 4x 185kN NTR cluster array (upgraded from 680kN baseline).
- **Alcantara Launch Interface**: Integration of the +463 m/s equatorial Earth rotation bonus and preliminary CNEN/AEB regulatory compliance frameworks.
- **Engine-Out Safety Analytics**: Explicit `e_out_tw = 0.31` reporting for 3-engine active abort profiles.

### Changed
- **Dry Mass**: Adjusted to 185.0t following a 25.8t structural density calculation correction inside the Carbon-Carbon aerospike assembly (8190 → 1950 kg/m³).
- **Core Working Temperature**: Elevated to 3100 K inside the UC-ZrC-NbC fuel matrix to sustain the theoretical 920s specific impulse target.

---

## - 2026-05-15

### Added
- Initial V3.0 conceptual baseline: 4x 170kN chemical/nuclear engines, 680kN total thrust, linear 780s Isp.
- ATHENA habitat module providing 380m³ internal volume for a 6-crew life support architecture over a 776-day profile.
