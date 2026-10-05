# 📝 Manual Extendido y Práctico de Formato Markdown

Markdown es el lenguaje estándar de texto plano utilizado por Obsidian para dar formato visual de manera instantánea, sin necesidad de usar el ratón ni menús complejos.

En esta guía verás **primero el código Markdown en bruto** (tal cual lo escribes en tu teclado) y **justo debajo el resultado renderizado** (tal como lo ves en el editor visual o en la vista de lectura).

---

## 1. Encabezados y Jerarquía de Contenido

### 💻 Código Markdown (En bruto)
```markdown
# 1. Gestión de Riesgos Global (Título Principal - H1)
## 1.1. Riesgos Financieros (Sección Principal - H2)
### 1.1.1. Riesgo de Crédito y Impago (Subsección - H3)
#### 1.1.1.1. Análisis de Probabilidad de Default (Detalle - H4)
```

### 👁️ Resultado Renderizado
# 1. Gestión de Riesgos Global (Título Principal - H1)
## 1.1. Riesgos Financieros (Sección Principal - H2)
### 1.1.1. Riesgo de Crédito y Impago (Subsección - H3)
#### 1.1.1.1. Análisis de Probabilidad de Default (Detalle - H4)

---

## 2. Formato de Texto y Énfasis

### 💻 Código Markdown (En bruto)
```markdown
- Texto normal para redacción de informes estándar.
- **Texto en negrita para resaltar conceptos críticos o alertas.**
- *Texto en cursiva para términos en latín como VaR o aforismos.*
- ***Texto en negrita y cursiva para máximas de vital importancia.***
- ~~Texto tachado para normativas derogadas o modelos obsoletos.~~
- ==Texto resaltado en amarillo para atención inmediata en Obsidian.==
```

### 👁️ Resultado Renderizado
- Texto normal para redacción de informes estándar.
- **Texto en negrita para resaltar conceptos críticos o alertas.**
- *Texto en cursiva para términos en latín como VaR o aforismos.*
- ***Texto en negrita y cursiva para máximas de vital importancia.***
- ~~Texto tachado para normativas derogadas o modelos obsoletos.~~
- ==Texto resaltado en amarillo para atención inmediata en Obsidian.==

---

## 3. Listas Organizadas y Checklists de Auditoría

### 💻 Código Markdown (En bruto)
```markdown
### Lista de Verificación para Auditoría de Riesgos (Checklist)
- [x] Auditar la calidad de los datos de entrada (Coñécete a ti mesmo).
- [x] Calcular el Valor en Riesgo (VaR) al 99% de confianza.
- [ ] Ejecutar el Conxuro de Stress Testing para escenarios macroeconómicos adversos.
- [ ] Presentar la matriz de mitigación al Comité de Dirección.

### Pasos Secuenciales (Lista Ordenada)
1. Identificación de la amenaza operativa.
2. Estimación de frecuencia e impacto cuantitativo.
3. Definición de controles y mitigadores.
4. Evaluación del riesgo residual.
```

### 👁️ Resultado Renderizado
### Lista de Verificación para Auditoría de Riesgos (Checklist)
- [x] Auditar la calidad de los datos de entrada (Coñécete a ti mesmo).
- [x] Calcular el Valor en Riesgo (VaR) al 99% de confianza.
- [ ] Ejecutar el Conxuro de Stress Testing para escenarios macroeconómicos adversos.
- [ ] Presentar la matriz de mitigación al Comité de Dirección.

### Pasos Secuenciales (Lista Ordenada)
1. Identificación de la amenaza operativa.
2. Estimación de frecuencia e impacto cuantitativo.
3. Definición de controles y mitigadores.
4. Evaluación del riesgo residual.

---

## 4. Tablas Estructuradas de Evaluación de Riesgos

### 💻 Código Markdown (En bruto)
```markdown
| ID Riesgo | Categoria | Probabilidad | Impacto | Nivel de Riesgo | Estrategia de Mitigación |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **R-001** | Financiero | Alta | Crítico | 🔴 Severo | Cobertura mediante derivados (Swaps) |
| **R-002** | Ciberseguridad | Media | Alto | 🟠 Alto | Autenticación multifactor y Backups |
| **R-003** | Operacional | Baja | Medio | 🟡 Moderado | Rediseño del proceso interno |
| **R-004** | Reputacional | Muy Baja | Bajo | 🟢 Tolerable | Aceptación y monitorización |
```

### 👁️ Resultado Renderizado
| ID Riesgo | Categoria | Probabilidad | Impacto | Nivel de Riesgo | Estrategia de Mitigación |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **R-001** | Financiero | Alta | Crítico | 🔴 Severo | Cobertura mediante derivados (Swaps) |
| **R-002** | Ciberseguridad | Media | Alto | 🟠 Alto | Autenticación multifactor y Backups |
| **R-003** | Operacional | Baja | Medio | 🟡 Moderado | Rediseño del proceso interno |
| **R-004** | Reputacional | Muy Baja | Bajo | 🟢 Tolerable | Aceptación y monitorización |

---

## 5. Bloques de Citas (Blockquotes) e Inscripciones

### 💻 Código Markdown (En bruto)
```markdown
> "Conócete a ti mismo. Por semejanza a Dios procede como hechura de su mano. 
> Huye del vicio. Busca la virtud. Aborrece el ocio. Ama el trabajo. 
> No seas soberbio, antes humilde. No mientas porque es la mayor vileza de los viles. 
> Procura los amigos mejores que tú, pues con esto y verdad, secreto y limpieza de alma, 
> nos sucede bien."
> 
> — **Inscripción histórica de la Torre del Homenaje del Pazo de Fefiñáns (Cambados, s. XVI)**  
> *En gallego: "Coñécete a ti mesmo... fuxe do vicio, busca a virtude, aborrece o ocio e ama o traballo..."*  
> *Aplicado a la gestión de riesgos: Audita y conoce tu propio balance antes de juzgar los mercados.*
```

### 👁️ Resultado Renderizado
> "Conócete a ti mismo. Por semejanza a Dios procede como hechura de su mano. 
> Huye del vicio. Busca la virtud. Aborrece el ocio. Ama el trabajo. 
> No seas soberbio, antes humilde. No mientas porque es la mayor vileza de los viles. 
> Procura los amigos mejores que tú, pues con esto y verdad, secreto y limpieza de alma, 
> nos sucede bien."
> 
> — **Inscripción histórica de la Torre del Homenaje del Pazo de Fefiñáns (Cambados, s. XVI)**  
> *En gallego: "Coñécete a ti mesmo... fuxe do vicio, busca a virtude, aborrece o ocio e ama o traballo..."*  
> *Aplicado a la gestión de riesgos: Audita y conoce tu propio balance antes de juzgar los mercados.*

---

## 6. Enlaces Externos y Conexiones Internas (Wiki-Links)

### 💻 Código Markdown (En bruto)
```markdown
- Enlace web externo tradicional: [Normativa Basilea III](https://www.bis.org)
- Enlace interno a nota en Obsidian: [[02 - Conceptos Fundamentales del Riesgo/Riesgo de Crédito|Ver Ficha de Riesgo de Crédito]]
- Enlace directo al manual hermano: [[01 - Primeros Pasos/Manual de Obsidian|Consultar el Manual de Obsidian]]
```

### 👁️ Resultado Renderizado
- Enlace web externo tradicional: [Normativa Basilea III](https://www.bis.org)
- Enlace interno a nota en Obsidian: [[02 - Conceptos Fundamentales del Riesgo/Riesgo de Crédito|Ver Ficha de Riesgo de Crédito]]
- Enlace directo al manual hermano: [[01 - Primeros Pasos/Manual de Obsidian|Consultar el Manual de Obsidian]]

---

## 7. Snippets de Código e Fórmulas de Riesgo

### 💻 Código Markdown (En bruto)
```markdown
```python
# Script para el cálculo de la pérdida esperada (Expected Loss)
def calcular_perdida_esperada(pd, ead, lgd):
    """
    pd: Probabilidad de Default (0 a 1)
    ead: Exposición en el Momento del Default (en euros)
    lgd: Pérdida en Caso de Incumplimiento (0 a 1)
    """
    el = pd * ead * lgd
    return f"Pérdida Esperada: {el:,.2f} €"

print(calcular_perdida_esperada(pd=0.03, ead=1000000, lgd=0.45))
```
```

### 👁️ Resultado Renderizado
```python
# Script para el cálculo de la pérdida esperada (Expected Loss)
def calcular_perdida_esperada(pd, ead, lgd):
    """
    pd: Probabilidad de Default (0 a 1)
    ead: Exposición en el Momento del Default (en euros)
    lgd: Pérdida en Caso de Incumplimiento (0 a 1)
    """
    el = pd * ead * lgd
    return f"Pérdida Esperada: {el:,.2f} €"

print(calcular_perdida_esperada(pd=0.03, ead=1000000, lgd=0.45))
```

---
- Volver al [[Índice Principal]]
