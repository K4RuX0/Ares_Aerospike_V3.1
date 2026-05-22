# ARES-STARSHIP V3.1 - PROMETHEUS I TECHNICAL ROADMAP
**Path to Flight: TRL-4 → TRL-9 | 10 Years | $18B Program**

> Philosophy: Hardware-rich, test-to-fail, NASA-STD-5017 compliant. No paper rockets.

## 1. TRL GATE SUMMARY

| TRL | Milestone | Duration | CAPEX | Key Deliverable | Exit Criteria / Gate |
| --- | --- | --- | --- | --- | --- |
| **TRL-4** | **170kN Lab Demo** | 0-18 mo | **$20M** | Subscale NTR UC-ZrC 50kN hot-fire 30s LH2 @ 2800K + Aerospike cold-flow | NASA/DOE validate Isp ≥750s. **Seed → Series A** |
| **TRL-5** | **Full-Scale Engine** | 18-36 mo | **$150M** | Flight-like NTR 170kN + Turbopump 67kg/s LH2 @ 125bar. 300s hot-fire w/ gimbal | Component qualification complete. **Series A → B** |
| **TRL-6** | **Integrated Stage Test** | 36-54 mo | **$800M** | 3x NTR cluster 510kN on 9mD tank. 600s ground test Nevada simulating TMI | Stage fires without RUD. Data for NASA CDR. **Series B → C** |
| **TRL-7** | **Orbital Demo** | 54-72 mo | **$2.5B** | Prometheus-0: Uncrewed LEO. 6 burns, 14200 m/s total. Reactor re-entry demo | System operates in space. **Series C → Gov Contract** |
| **TRL-8** | **Crew Certification** | 72-96 mo | **$6B** | 10CFR52 + FAA Part 460. ATHENA 776-day ground test. Escape/abort validated | NASA Human Rating achieved. **Gov Contract Signed** |
| **TRL-9** | **Prometheus I Mars** | 96-120 mo | **$8.5B** | 6 crew Mars round-trip. 125-day transit + 500-day surface. ISRU demo | **Mission Success. Operational Program.** |

**Total Program Cost: $18B | Timeline: 10 Years**

## 2. SEED ROUND: $20M TRL-4 BREAKDOWN - 18 MONTHS

| Category | USD | Description |
| --- | --- | --- |
| **Team 15 FTE x 18mo** | $6.5M | 4 Nuclear, 3 Propulsion, 2 GNC, 2 ECLSS, 2 Software, 2 PM/QA |
| **UC-ZrC Fuel R&D** | $4.0M | 3200K furnace, sintering, ORNL testing, rad-hard validation |
| **Subscale NTR 50kN** | $3.5M | Pressure vessels, piping, rad-hard instrumentation |
| **Aerospike Demo** | $2.0M | Inconel-718 AM, cold-flow tests, short-duration hot-fire |
| **Test Stand Lease** | $2.0M | Stennis or equivalent. LH2 infrastructure + safety |
| **10CFR52 + Legal** | $1.0M | Nuclear attorneys, NRC preliminary submittal |
| **Contingency 10%** | $1.0M | Hardware programs always overrun |
| **TOTAL** | **$20M** | **Deliverable: 30s hot-fire of 50kN NTR @ 750s Isp** |

## 3. CRITICAL TECHNICAL GATES

Program-ending risks that must be retired:

1. **Materials**: UC-ZrC cracking >2800K = program death. Mitigation: C-C/NbC backup fuel.
2. **Regulatory**: NRC denies HALEU flight waiver = program death. Mitigation: DOD sponsorship + lobbying.
3. **LH2 Storage**: Boil-off >2%/day over 776 days = mission failure. Mitigation: ZBO + Mars shadow transit.
4. **Radiation**: Crew dose >50 rem = NASA human rating denied. Mitigation: 20g/cm² PE+H2O + storm shelter.
5. **Clustering**: 3x NTR combustion instability = RUD. Mitigation: Full-scale cluster ground test TRL-6.

## 4. GO-TO-MARKET & FUNDING STRATEGY

| Phase | Years | Funding Source | Amount | Purpose |
| --- | --- | --- | --- | --- |
| **1-3** | 0-3 | NASA NIAC + DOD DIU | $50M Non-dilutive | TRL-4/5 de-risk, retain equity |
| **3-5** | 3-5 | Space Force Launch Contract | $500M | Fund Prometheus-0 orbital demo |
| **5-10** | 5-10 | NASA Artemis Mars Transport | $4B/mission x 10 | $40B revenue pipeline. TRL-9 ops |

## 5. PROGRAM TIMELINE

```mermaid
gantt
    title Ares-Starship Prometheus I - 10 Year Path to Mars
    dateFormat  YYYY-MM
    section TRL-4 Seed
    Lab Demo 50kN NTR           :a1, 2026-01, 18mo
    section TRL-5 Series A
    Full-Scale 170kN Engine     :a2, after a1, 18mo
    section TRL-6 Series B
    Stage Cluster Test 510kN    :a3, after a2, 18mo
    section TRL-7 Series C
    Prometheus-0 Orbital Demo   :a4, after a3, 18mo
    section TRL-8 Gov
    Human Rating + Cert         :a5, after a4, 24mo
    section TRL-9 Ops
    Prometheus I Mars Mission   :a6, after a5, 24mo