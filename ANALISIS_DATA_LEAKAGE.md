# 🚨 Análisis de Data Leakage - Dataset Phishing Emails

**Fecha**: 17 de Noviembre, 2025  
**Analista**: GitHub Copilot  
**Dataset**: `phishing_legit_dataset_KD_10000.csv`

---

## 📊 Resumen Ejecutivo

El modelo actual alcanza **~100% de precisión** debido a **data leakage crítico** en las features. El modelo no está aprendiendo patrones reales de phishing del texto, sino usando metadatos que no estarían disponibles en un escenario de producción.

---

## 🔍 Problemas Identificados

### 1. **Data Leakage Crítico: `phishing_type`**

**Gravedad**: ⚠️ CRÍTICA

```python
# Valores únicos por clase:
label=0 → phishing_type='legitimate'      # TODOS los legítimos
label=1 → phishing_type=credential_harvesting, financial_scam, authority_scam, urgency, etc.
```

**Problema**: Esta variable es **100% predictiva del label**. En producción, no sabríamos el tipo de phishing antes de clasificarlo.

**Impacto**: El modelo aprende a clasificar mirando esta feature en lugar del texto.

---

### 2. **Data Leakage Moderado: `confidence`**

**Gravedad**: ⚠️ ALTA

```
Estadísticas de confidence por clase:
label=0 (legítimo):  mean=0.975, std=0.015
label=1 (phishing):  mean=0.848, std=0.071
```

**Problema**: Hay una separación clara entre clases (~0.975 vs ~0.848). Esta "confidence" probablemente fue generada por otro modelo, no es una feature real del email.

**Impacto**: El modelo puede usar esta diferencia para clasificar sin analizar el texto.

---

### 3. **Keywords Explícitas en Texto**

**Gravedad**: ⚠️ MEDIA

Los emails phishing incluyen literalmente:
```
"Keywords: pin update password sign in settings password"
```

**Problema**: En emails de phishing reales, estas keywords no aparecen explícitamente etiquetadas. Esto facilita artificialmente la clasificación.

---

### 4. **Balance de Clases Moderado**

```
Clase 0 (legítimo): 4,000 (40%)
Clase 1 (phishing): 6,000 (60%)
```

**Problema Menor**: Hay un desbalance de 60/40, pero es manejable. Sin embargo, debe considerarse al evaluar el modelo.

---

## ✅ Recomendaciones

### 1. **Eliminar Features con Leakage**
- ❌ **NO usar** `phishing_type` como feature para clasificación binaria (label)
- ⚠️ **Usar con precaución** `confidence` (idealmente remover)
- ⚠️ **Considerar** remover la línea "Keywords:" del texto durante limpieza

### 2. **Preprocesamiento Correcto**
```python
# Features VÁLIDAS para clasificación binaria (phishing vs legítimo):
X = text_features_only  # Solo TF-IDF del texto limpio
y = df['label']

# NO incluir:
# - phishing_type (es el target de otro problema)
# - confidence (probable leakage)
# - severity (también es leakage)
```

### 3. **División de Datos Apropiada**
```python
# Usar stratified split para mantener proporciones
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.4, stratify=y, random_state=42
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42
)
```

### 4. **Métricas Apropiadas**
Dado el desbalance 60/40:
- Reportar **Precision, Recall, F1-Score** (no solo Accuracy)
- Analizar **matriz de confusión** detalladamente
- **ROC-AUC** es buena métrica para este caso
- Considerar **costo de FP vs FN** (¿qué es peor: marcar legítimo como phishing o viceversa?)

---

## 📋 Plan de Acción

### Fase 1: Clasificación Binaria Correcta (Notebook 1)
**Objetivo**: Clasificar `label` (phishing vs legítimo) usando **solo el texto**

**Features**:
- ✅ TF-IDF del texto (sin "Keywords:")
- ✅ Longitud del texto
- ✅ Cantidad de palabras
- ❌ NO usar phishing_type, confidence, severity

**Modelos a probar**:
1. Regresión Logística (con regularización L2)
2. Naive Bayes (baseline)
3. SVM con kernel lineal
4. Random Forest (comparativa)

**Métrica objetivo**: F1-Score > 0.85 con ROC-AUC > 0.90

---

### Fase 2: Clasificación Multi-Clase (Notebook 2)
**Objetivo**: Clasificar `phishing_type` **solo para emails phishing** (label=1)

```python
# Filtrar solo emails phishing
df_phishing = df[df['label'] == 1]
X = text_features
y = df_phishing['phishing_type']  # credential_harvesting, financial_scam, etc.
```

**Modelos**:
- Random Forest
- Gradient Boosting (XGBoost/LightGBM)
- Multinomial Logistic Regression

---

### Fase 3: Análisis Avanzado (Notebook 3)
- Feature engineering con n-gramas, embeddings
- Análisis de palabras más importantes por clase
- Ensembles y voting classifiers
- Detección de overfitting y técnicas de regularización

---

## 📖 Referencias

- **Curso base**: https://jdariasl.github.io/Intro_ML_2025
- **Scikit-learn**: https://scikit-learn.org/stable/
- **Paper sobre Data Leakage**: Kaufman et al. (2012) "Leakage in Data Mining"

---

## 🎯 Expectativas Realistas

Con **solo texto (sin leakage)**:
- Accuracy esperado: **85-92%** (no 100%)
- F1-Score esperado: **0.83-0.90**
- ROC-AUC esperado: **0.88-0.95**

Estos valores son **realistas y demuestran aprendizaje genuino** de patrones lingüísticos de phishing.

---

**Conclusión**: El modelo actual no es válido para producción. Necesita reentrenamiento eliminando features con leakage.
