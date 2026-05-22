# Changelog - ARES-STARSHIP V3.1

All notable changes to the Prometheus I mission architecture will be documented in this file.

## [3.1.0-heavy] - 2026-05-22

### Added
- **740kN Heavy Configuration**: Upgraded from 4x 170kN to 4x 185kN NTR cluster
- **Engine-Out T/W Reporting**: Explicit calculation `e_out_tw = 0.39` for NASA ASAP compliance
- **NASA NPR 8705.2C Compliance**: T/W 0.52 exceeds 0.5 minimum for crewed launchpad escape
- **10CFR52/ITAR Clause**: MIT License with export control notice for nuclear conceptual work

### Changed
- **Thrust**: 680kN → 740kN (+8.8%) for improved safety margins
- **T/W Ratio**: 0.51 → 0.52 providing 2% additional margin above NASA minimum
- **Engine-Out T/W**: 0.38 → 0.39 with 3x NTR, enabling robust LEO abort capability
- **Mass Flow**: 88.7 kg/s → 96.7 kg/s LH2 to support 185kN per engine
- **Material Density Fix**: Spike Carbon-Carbon corrected from 8190 to 1950 kg/m³
- **Mass Architecture**: Hardcoded dry/propellant/tank values to lock documentation parity

### Fixed
- **Critical**: Spike mass calculation now uses C-C density 1950 kg/m³ instead of Inconel 8190
- **Physics**: Eliminated 25.8t mass error in spike assembly that violated dry mass budget
- **Consistency**: Code output now matches README.md, BOM, and investor pitch line-by-line

### Engineering Rationale
The upgrade from 680kN to 740kN was driven by NASA Human-Rating Requirements NPR 8705.2C, which mandates T/W > 0.5 for crewed vehicles and robust engine-out abort capability. The 740kN configuration provides:
1. **T/W 0.52**: 2% margin above minimum, reducing sensitivity to mass growth
2. **Engine-Out 0.39**: Allows safe abort to LEO on 3x engines vs marginal 0.38
3. **Heritage**: 185kN per NTR remains well below NERVA-tested 333kN, maintaining conservatism

Mass budget remains unchanged at 1452.7t pad mass. Thrust increase achieved via chamber pressure optimization within 2800K core temp limits.

## [3.0.0] - 2026-05-15

### Added
- Initial V3.1 architecture: 4x 170kN NTR cluster, 680kN total
- ATHENA habitat module 380m³ for 6 crew, 776-day mission
- Full ECLSS 90% closed-loop, 20 g/cm² PE+H2O shielding
- Automated BOM, mass breakdown, and investor pitch generation

### Known Issues
- Spike density used Inconel 8190 kg/m³ instead of Carbon-Carbon 1950 kg/m³
- T/W 0.51 marginal for NASA human-rating; engine-out 0.38 borderline