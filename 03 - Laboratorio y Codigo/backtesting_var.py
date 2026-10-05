# -*- coding: utf-8 -*-
"""
Simulacion y Backtesting Cuantitativo de Modelos VaR
Master de Riesgos - Demostracion Antigravity AI
"""

import sys
import numpy as np

# Configurar stdout para evitar problemas con la codificacion de la consola de Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_var_backtest(portfolio_value=1000000, days=250, alpha=0.99):
    print("=" * 65)
    print("   [+] MASTER DE RIESGOS: AUDITORIA Y BACKTESTING DE MODELO VaR")
    print("   Inspirado en el principio de Fefinans: 'Conocete a ti mismo'")
    print("=" * 65)
    print("\n[+] Configuracion:")
    print(f"    - Valor de la Cartera:       {portfolio_value:,.2f} EUR")
    print(f"    - Horizonte Temporal:        {days} dias de mercado (1 ano)")
    print(f"    - Nivel de Confianza:        {alpha * 100:.1f}%\n")

    np.random.seed(42)
    daily_vol = 0.015
    returns = np.random.normal(loc=0.0002, scale=daily_vol, size=days)
    pnl = portfolio_value * returns

    # VaR diario al 99% (paramétrico: Z = 2.326)
    z_score = 2.326
    daily_var = portfolio_value * z_score * daily_vol

    breaches = int(np.sum(pnl < -daily_var))
    expected_breaches = days * (1 - alpha)

    print("-" * 65)
    print("                   RESULTADOS DE LA AUDITORIA")
    print("-" * 65)
    print(f"  * VaR Diario Estimado (99%):      {daily_var:,.2f} EUR")
    print(f"  * Peor Perdida Simulada:          {abs(np.min(pnl)):,.2f} EUR")
    print(f"  * Numero de Excepciones Reales:   {breaches}")
    print(f"  * Excepciones Esperadas:          {expected_breaches:.1f}")
    print("-" * 65)

    print("\n[+] DICTAMEN TECNICO REGULATORIO (Semaforo de Basilea):")
    if breaches <= 4:
        print("  [OK] ZONA VERDE: El modelo esta perfectamente calibrado.")
        print("       No se requieren recargos de capital adicional.")
    elif breaches <= 9:
        print("  [!]  ZONA AMARILLA: Se detecta subestimacion moderada del riesgo.")
        print("       Se recomienda revision de supuestos de volatilidad.")
    else:
        print("  [X]  ZONA ROJA: El modelo infravalora gravemente el riesgo del mercado.")
        print("       Exige recalibracion inmediata y recargos de capital.")

    print("=" * 65)

if __name__ == "__main__":
    run_var_backtest()
    print("\nPresiona ENTER para salir...")
    try:
        input()
    except EOFError:
        pass
