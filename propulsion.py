# -*- coding: utf-8 -*-
"""
ARES-SPACE TRANSPORT V4.0 — Solar Thermal Propulsion (STP) Module
Author: Ranyellson Quintão
Horizon: 2030 Target | Launch Site: Alcantara, Brazil
"""
import math

class SolarThermalPropulsion:
    def __init__(self):
        self.total_engines = 2
        self.active_engines = 2
        self.g0 = 9.80665                         # Standard gravity (m/s²)
        self.r_methane = 518.3                    # Specific gas constant for Methane (J/kg·K)
        self.gamma_methane = 1.32                 # Heat capacity ratio (Cp/Cv) for superheated LCH4
        self.chamber_coating = "Iridium / Ta4HfC5" # Zero-corrosion thermal barrier
        
    def calculate_performance(self, distance_au, mass_flow_rate_kg_s=15.0):
        if self.active_engines == 0:
            return {"thrust_kn": 0.0, "thermal_power_mw": 0.0, "isp_seconds": 0.0, "chamber_temp_k": 0.0}

        # 1. Solar Concentrator Thermal Balance
        solar_constant_earth = 1361.0
        available_flux = solar_constant_earth / (distance_au ** 2)
        mirror_area = 1250.0 * self.active_engines
        optical_efficiency = 0.85
        absorber_efficiency = 0.78  
        
        thermal_power_w = available_flux * mirror_area * optical_efficiency * absorber_efficiency
        
        # 2. Dynamic Chamber Temperature (Gas Physics)
        cp_methane = 3500.0
        t_initial = 112.0  # Liquid methane storage temperature (K)
        delta_t = thermal_power_w / (mass_flow_rate_kg_s * cp_methane)
        chamber_temp_k = t_initial + delta_t
        
        # Material structural thermal limit
        if chamber_temp_k > 3200.0:
            chamber_temp_k = 3200.0

        # 3. Isentropic Nozzle Expansion Equations
        v_exhaust = math.sqrt((2 * self.gamma_methane / (self.gamma_methane - 1)) * self.r_methane * chamber_temp_k)
        isp_seconds = v_exhaust / self.g0
        thrust_kn = (mass_flow_rate_kg_s * v_exhaust) / 1000.0
        
        return {
            "thrust_kn": round(thrust_kn, 2),
            "thermal_power_mw": round(thermal_power_w / 1e6, 2),
            "isp_seconds": round(isp_seconds, 1),
            "chamber_temp_k": round(chamber_temp_k, 1),
            "corrosion_protection": "ACTIVE (Atomic Iridium Layer Intact)"
        }
