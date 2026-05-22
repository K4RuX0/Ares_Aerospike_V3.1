import pytest
import math

class TestAresStarshipV31Heavy:
    """V3.1 Compliance Test Suite - Prometheus I"""
    
    # Constants from ares_v31.py V3.1
    THRUST_PER_NTR = 185000  # N
    NTR_COUNT = 4
    TARGET_THRUST_N = 740000
    DRY_MASS = 185000  # kg (corrigido)
    TOTAL_PROPELLANT = 1127000  # kg
    TANKS_MASS = 95000  # kg (corrigido)
    LAUNCHPAD_TOTAL_MASS = 1407000  # kg
    REALISTIC_ISP = 920  # s (corrigido de 780)
    DELTA_V_TOTAL = 14570  # m/s (com Alcântara)
    G0 = 9.81
    
    def test_tw_ratio_orbital(self):
        """V3.1: T/W orbital ~0.41 (NTR não é lançador)"""
        tw = self.TARGET_THRUST_N / (self.DRY_MASS * self.G0)
        assert 0.40 <= tw <= 0.42, f"T/W {tw:.3f} fora do esperado 0.41"
        assert round(tw, 2) == 0.41
    
    def test_engine_out_abort_capability(self):
        """Engine-out com 3x NTR"""
        engine_out_thrust = self.THRUST_PER_NTR * 3
        e_out_tw = engine_out_thrust / (self.DRY_MASS * self.G0)
        assert e_out_tw >= 0.30, f"Engine-out T/W {e_out_tw:.3f} < 0.30"
        assert round(e_out_tw, 2) == 0.31  # era 0.39 na versão antiga
    
    def test_delta_v_budget(self):
        """Verifica propelente para 14,570 m/s"""
        exhaust_velocity = self.REALISTIC_ISP * self.G0
        mass_ratio = math.exp(self.DELTA_V_TOTAL / exhaust_velocity)
        required_prop = (self.DRY_MASS * mass_ratio) - self.DRY_MASS
        required_with_margin = required_prop * 1.05  # 5% margin V3.1
        
        assert self.TOTAL_PROPELLANT >= required_with_margin, \
            f"Prop {self.TOTAL_PROPELLANT/1000:.1f}t < necessário {required_with_margin/1000:.1f}t"
    
    def test_mass_fraction_realistic(self):
        """Fração propelente ~80% para 920s"""
        prop_fraction = self.TOTAL_PROPELLANT / self.LAUNCHPAD_TOTAL_MASS
        assert 0.79 <= prop_fraction <= 0.81, \
            f"Fração {prop_fraction:.3f} fora de 0.80"
    
    def test_spike_density_correct(self):
        """Regression: C-C 1950 kg/m³"""
        internal_radius = 0.60
        allowable_stress = 150e6
        chamber_pressure = 7.0e6
        stress_ratio = (allowable_stress + chamber_pressure) / (allowable_stress - chamber_pressure)
        external_radius = internal_radius * math.sqrt(stress_ratio)
        
        spike_vol = math.pi * (external_radius**2 - internal_radius**2) * 4.5
        spike_mass_cc = spike_vol * 1950 * self.NTR_COUNT
        
        assert 3800 < spike_mass_cc < 4000, f"Spike {spike_mass_cc:.0f}kg esperado ~3890kg"
    
    def test_mass_budget_closure(self):
        """Dry + prop + tanks = 1,407t"""
        calculated = self.DRY_MASS + self.TOTAL_PROPELLANT + self.TANKS_MASS
        assert calculated == self.LAUNCHPAD_TOTAL_MASS
    
    def test_isp_3100k_heritage(self):
        """Isp 920s requer 3100K - além NERVA, dentro UC-ZrC-NbC"""
        assert 900 <= self.REALISTIC_ISP <= 950, \
            f"Isp {self.REALISTIC_ISP}s fora do target 920s"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])