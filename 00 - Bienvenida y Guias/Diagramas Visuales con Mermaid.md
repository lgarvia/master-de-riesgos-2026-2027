# 📊 Diagramas Visuales con Mermaid en Obsidian

Obsidian admite de forma nativa la sintaxis **Mermaid**, lo que te permite crear diagramas de flujo, mapas conceptuales y esquemas de riesgo mediante texto.

---

## 1. Flujo de Trabajo en Análisis de Riesgos
```mermaid
flowchart TD
    A[Identificación del Riesgo] --> B[Evaluación de Impacto]
    B --> C{¿Supera el Umbral?}
    C -- Sí --> D[Plan de Mitigación]
    C -- No --> E[Aceptar Riesgo / Monitoreo]
    D --> F[Revisión por Comité]
```

## 2. Mapa de Conexión de Riesgos
```mermaid
graph LR
    RiesgoMercado[Riesgo de Mercado] --> VaR[Modelos VaR]
    RiesgoCredito[Riesgo de Crédito] --> VaR
    VaR --> StressTesting[Stress Testing]
    StressTesting --> Mitigacion[Matriz de Mitigación]
```

---
- Regresar al [[Índice Principal]]
