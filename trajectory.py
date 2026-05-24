# -*- coding: utf-8 -*-
"""
ARES-SPACE TRANSPORT V4.0 — Kinetic Trajectory Solver
Author: Ranyellson Quintão
"""
import math
from src.propulsion import SolarThermalPropulsion

class LunarMissionSolver:
    def __init__(self):
        self.dry_mass_ship_tons = 120.0  
        self.engine_subsystem = SolarThermalPropulsion()
        
    def evaluate_mission(self, payload_tons, round_trip=True, distance_au=1.0):
        engine_perf = self.engine_subsystem.calculate_performance(distance_au)
        isp = engine_perf["isp_seconds"]
        g0 = self.engine_subsystem.g0
        
        # Delta-V budget including 5% gravity loss margin
        delta_v_required = 8400.0 if round_trip else 4200.0
        v_e = isp * g0
        
        mass_initial = self.dry_mass_ship_tons + 1130.0 + payload_tons
        mass_final_allowed = mass_initial / math.exp(delta_v_required / v_e)
        fuel_required_tons = mass_initial - mass_final_allowed
        margin_tons = 1130.0 - fuel_required_tons
        
        if fuel_required_tons <= 1130.0 and isp > 0:
            status = f"SUCCESS: Mission approved with real Isp of {isp}s."
            viable = True
        else:
            status = "REJECTED: Kinetic depletion failure."
            viable = False
            
        return {
            "mission_type": "Lunar Round-Trip (Cislunar)" if round_trip else "Lunar Logistics (One-Way)",
            "payload_carried_tons": payload_tons,
            "fuel_needed_tons": round(fuel_required_tons, 2),
            "fuel_margin_tons": round(margin_tons, 2),
            "mission_viable": viable,
            "architecture_status": status
        }