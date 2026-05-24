# Assumptions — ARES-SPACE TRANSPORT V4.0

`VERSION: 4.0 | DATE: 2030-05-24 | AUTHOR: Ranyellson Quintão`
`STATUS: GREEN SOLAR THERMAL TRANSITION | HORIZON 2030`

## 1. Operações e Lançamento (Launch and Operations)

| ID | Premissa (Assumption) | Valor Nominal (Value) | Justificativa de Engenharia |
| --- | --- | --- | --- |
| L-01 | Base de Lançamento | Centro de Lançamento de Alcântara, 2.3°S | Otimização de inclinação e redução de perdas por manobra. |
| L-02 | Bônus de Rotação da Terra | +463 m/s | Ganho cinético injetado diretamente no balanço de órbita. |
| L-03 | Altitude de Ignição STP | Órbita Baixa da Terra (LEO) @ ~400 km | Acionamento seguro após abertura dos espelhos infláveis. |
| L-04 | Arquitetura de Logística | Lançamento Único de Carga + Reabastecimento | Tanques de 9m cheios via voos comerciais de metano em LEO. |

## 2. Subsistema de Propulsão STP (Propulsion)

| ID | Premissa (Assumption) | Valor Nominal (Value) | Justificativa de Engenharia |
| --- | --- | --- | --- |
| P-01 | Configuração do Cluster | 2 × 185 kN STP Aerospike Arrays | Redundância ativa 1/2 com isolamento de bocal integrado. |
| P-02 | Impulso Específico (Isp) | 620.0 s (Vácuo) | Expansão isentrópica calculada para Metano a 3200 K. |
| P-03 | Temperatura de Câmara ($T_c$) | 3200 K (Teto Operacional) | Equilíbrio térmico da liga $Ta_4HfC_5$ com revestimento de Irídio. |
| P-04 | Propelente Criogênico | Metano Líquido ($LCH_4$), 1.130.000 kg | Combustível estável de alta densidade (422.6 kg/m³). |
| P-05 | Proteção de Combustível | Active Zero Boil-Off (ZBO) Ativo | Crio-resfriadores de 2.5 kW travando a taxa de evaporação. |

## 3. Orçamento de Massa Otimizado (Mass Budget)

| ID | Premissa (Assumption) | Valor Nominal (Value) | Correção Física Aplicada |
| --- | --- | --- | --- |
| M-01 | Massa Seca (Dry Mass) | 120.000 kg (120.0 t) | Aliviada em 65t pela remoção total de chumbo e urânio. |
| M-02 | Massa de Estrutura/Tanques | 75.000 kg (75.0 t) | Tanques de Al-Li compactados devido ao tamanho do metano. |
| M-03 | Propelente Máximo ($M_p$) | 1.130.000 kg (1.130.0 t) | Carga máxima volumétrica para a fuselagem de 9 metros. |
| M-04 | Massa Total de Lançamento | 1.325.000 kg (1.325.0 t) | Peso bruto estabilizado e balanceado em LEO. |
## 4. Orçamento de Delta-V e Viabilidade Cinética (Delta-V Budgets)

### FASE I: Missão Logística Lunar (Ida e Volta Cislunar Sem Reabastecer)

| ID | Parâmetro Orbital | Valor Requerido | Status do Modelo Físico |
| --- | --- | --- | --- |
| D-01 | Delta-V Requerido da Fase I | 8.400 m/s | Inclui 5% de margem extra para perdas por gravidade em STP. |
| D-02 | Consumo de Combustível Estendido | 1.042.800 kg (1.042.8 t) | Fração de massa consumida ao longo dos 28 dias de voo. |
| D-03 | Margem de Sobra nos Tanques | +87.200 kg (+87.2 t) | Combustível remanescente seguro para correções em órbita. |
| D-04 | Avaliação Cinética Lunar | **APROVADO (TRL-7)** | Veículo cumpre o circuito completo de forma 100% autônoma. |

### FASE II: Missão Interplanetária Prometheus I (Escape LEO para Marte)

| ID | Parâmetro Orbital | Valor Requerido | Status do Modelo Físico |
| --- | --- | --- | --- |
| D-05 | Delta-V Requerido da Fase II | 4.200 m/s | Queima de alta energia para a manobra de Injeção Trans-Marte (TMI). |
| D-06 | Consumo de Ignição de Escape | 693.100 kg (693.1 t) | Massa ejetada para atingir a trajetória elíptica de transferência. |
| D-07 | Combustível Retido pós-TMI | +436.900 kg (+436.9 t) | Reserva líquida para crio-refrigeração e inserção em Marte. |
| D-08 | Avaliação Cinética Marciana | **APROVADO (2030 TARGET)**| Logística de alta eficiência competitiva com o mercado global. |
