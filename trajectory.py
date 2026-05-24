# -*- coding: utf-8 -*-
"""
ARES-SPACE TRANSPORT V4.0 — Kinetic Trajectory Mission Evaluator
Author: Ranyellson Quintão
"""
import math
from propulsion import SolarThermalEngine

class MissionKinematicsSolver:
    def __init__(self):
        self.dry_mass_tons = 120.0  
        self.tanks_mass_tons = 75.0
        self.max_propellant_tons = 1130.0
        self.g0 = 9.80665
        self.engine = SolarThermalEngine()
        
    def evaluate_target_profile(self, payload_tons, delta_v_target, round_trip=True):
        perf = self.engine.calculate_nozzle_kinetics(distance_au=1.0)
        v_e = perf["isp_seconds"] * self.g0
        
        mass_initial = self.dry_mass_tons + self.tanks_mass_tons + self.max_propellant_tons + payload_tons
        mass_final_required = mass_initial / math.exp(delta_v_target / v_e)
        
        fuel_needed_tons = mass_initial - mass_final_required
        margin_tons = self.max_propellant_tons - fuel_needed_tons
        
        return {
            "viable": fuel_needed_kg <= self.max_propellant_tons if 'fuel_needed_kg' in locals() else fuel_needed_tons <= self.max_propellant_tons,
            "fuel_needed_tons": round(fuel_needed_tons, 1),
            "margin_tons": round(margin_tons, 1),
            "profile_type": "CISLUNAR_LOOP" if round_trip else "INTERPLANETARY_BURST"
        }
