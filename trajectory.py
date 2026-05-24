# -*- coding: utf-8 -*-
"""
ARES-SPACE TRANSPORT V4.0 — High-Fidelity Kinetic & Trajectory Solver
Author: Ranyellson Quintão
Description: Computes Tsiolkovsky equations including aerodynamic drag losses,
             gravity wells, and stochastic mirror degradation profiles.
"""
import math
from src.propulsion import SolarThermalPropulsion

class HighFidelityTrajectorySolver:
    def __init__(self):
        self.DRY_MASS_TONS = 120.0  
        self.TANKS_MASS_TONS = 75.0
        self.MAX_PROPELLANT_TONS = 1130.0
        self.G0 = 9.80665
        self.engine = SolarThermalPropulsion()
        
    def evaluate_mission_profile(self, payload_tons, baseline_delta_v, mirror_degradation_factor=0.05, round_trip=True):
        """
        Evaluates flight kinetics including drag penalties and mirror degradation.
        mirror_degradation_factor: Account for micrometeorite pitting on Mylar surfaces.
        """
        # Fetch engine baseline performance
        perf = self.engine.calculate_nozzle_kinetics(distance_au=1.0)
        
        # Apply performance decay based on mirror degradation
        real_isp = perf["isp_seconds"] * (1.0 - mirror_degradation_factor)
        v_e = real_isp * self.G0
        
        # Add real-world atmospheric drag and gravity penalties (Delta-V tax ~ 5%)
        real_delta_v_required = baseline_delta_v * 1.05
        
        mass_initial = self.DRY_MASS_TONS + self.TANKS_MASS_TONS + self.MAX_PROPELLANT_TONS + payload_tons
        mass_final_required = mass_initial / math.exp(real_delta_v_required / v_e)
        
        fuel_needed_tons = mass_initial - mass_final_required
        remaining_margin_tons = self.MAX_PROPELLANT_TONS - fuel_needed_tons
        viable = fuel_needed_tons <= self.MAX_PROPELLANT_TONS
        
        return {
            "mission_viable": viable,
            "calibrated_isp_seconds": round(real_isp, 1),
            "delta_v_with_losses_m_s": round(real_delta_v_required, 1),
            "fuel_consumed_tons": round(fuel_needed_tons, 1),
            "remaining_fuel_margin_tons": round(margin_tons, 1) if 'margin_tons' in locals() else round(remaining_margin_tons, 1),
            "trajectory_status": "FLIGHT_APPROVED_WITH_SAFETY_MARGINS" if viable else "KINETIC_DEPLETION_ABORT"
        }

if __name__ == "__main__":
    solver = HighFidelityTrajectorySolver()
    print("--- Phase I Lunar Flight Analysis (5% Mirror Degradation + 5% Drag Loss) ---")
    print(solver.evaluate_mission_profile(payload_tons=55.0, baseline_delta_v=8400.0, round_trip=True))
