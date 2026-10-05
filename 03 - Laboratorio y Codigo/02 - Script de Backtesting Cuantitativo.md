# 🧮 Artefacto 2: Script Automatizado de Backtesting de Modelos VaR

Este artefacto demuestra cómo Antigravity puede generar scripts de análisis y automatización en **Python** para auditar carteras en riesgo.

```python
import numpy as np

def run_var_backtest(portfolio_value=1000000, days=250, alpha=0.99):
    """
    Simulación de Backtesting Kupiec POF Test para un modelo VaR.
    """
    np.random.seed(42)
    # Generar retornos sintéticos diarios
    returns = np.random.normal(loc=0.0002, scale=0.015, size=days)
    pnl = portfolio_value * returns
    
    # VaR estimado diario al 99%
    var_threshold = -portfolio_value * (2.326 * 0.015)
    
    # Excepciones (veces que la pérdida superó el VaR)
    breaches = np.sum(pnl < var_threshold)
    expected_breaches = days * (1 - alpha)
    
    print("=" * 50)
    print("           RESULTADOS DEL TEST DE KUPIEC           ")
    print("=" * 50)
    print(f"Días evaluados:             {days}")
    print(f"Pérdidas que superan el VaR: {breaches}")
    print(f"Excepciones esperadas:       {expected_breaches:.1f}")
    
    if breaches <= expected_breaches + 2:
        print("✅ Estado del Modelo: ZONA VERDE (Modelo Calibrado)")
    else:
        print("🚨 Estado del Modelo: ZONA ROJA (Requiere Recalibración)")
    print("=" * 50)

if __name__ == "__main__":
    run_var_backtest()
```

---
- Volver al [[Índice Principal]]
