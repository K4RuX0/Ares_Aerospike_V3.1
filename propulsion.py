# -*- coding: utf-8 -*-
"""
ARES-SPACE TRANSPORT V4.0 — Aerospace Aerospike Thrust Dynamics
Author: Ranyellson Quintão
"""
import math

class SolarThermalEngine:
    def __init__(self):
        self.total_engines = 2
        self.active_engines = 2
        self.g0 = 9.80665                         
        self.r_methane = 518.3                    # Methane molecular gas constant
        self.gamma_methane = 1.32                 # Superheated ratio
        self.chamber_coating = "Iridium / Ta4HfC5"
        
    def calculate_nozzle_kinetics(self, distance_au, mass_flow_rate_kg_s=15.0):
        if self.active_engines == 0:
            return {"thrust_kn": 0.0, "isp_seconds": 0.0, "chamber_temp_k": 0.0}

        solar_constant_earth = 1361.0
        available_flux = solar_constant_earth / (distance_au ** 2)
        mirror_area = 1250.0 * self.active_engines
        
        thermal_power_w = available_flux * mirror_area * 0.85 * 0.78
        
        cp_methane = 3500.0
        chamber_temp_k = 112.0 + (thermal_power_w / (mass_flow_rate_kg_s * cp_methane))
        
        if chamber_temp_k > 3200.0:
            chamber_temp_k = 3200.0

        v_exhaust = math.sqrt((2 * self.gamma_methane / (self.gamma_methane - 1)) * self.r_methane * chamber_temp_k)
        real_isp = v_exhaust / self.g0
        thrust_kn = (mass_flow_rate_kg_s * v_exhaust) / 1000.0
        
        return {
            "thrust_kn": round(thrust_kn, 2),
            "isp_seconds": round(real_isp, 1),
            "chamber_temp_k": round(chamber_temp_k, 1),
            "coating_status": "INTEGRATED_NO_DEGRADATION"
        }
