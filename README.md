# 📧 Phishing-Emails-ML - Detección de Phishing con Machine Learning

## 👥 Desarrolladores:
- **Daniela Rodríguez Chacón**
- **Estiven Ospina González**

## 📖 Descripción

Este proyecto implementa técnicas de **Machine Learning** para la detección de emails de phishing utilizando el dataset "Phishing and Legitimate Emails" (10,000 muestras).

### 🎯 Objetivos:
1. **Clasificación Binaria**: Distinguir emails phishing de legítimos usando **solo texto** (sin data leakage)
2. **Clasificación Multi-Clase**: Categorizar emails phishing por tipo (credential_harvesting, financial_scam, etc.)
3. **Análisis de Patrones**: Identificar características lingüísticas distintivas del phishing

### ⚠️ Importante: Corrección de Data Leakage

El análisis original contenía **data leakage crítico** que producía 100% de precisión:
- ❌ Uso de `phishing_type` como feature (100% predictivo del label)
- ❌ Uso de `confidence` (diferencias artificiales entre clases)
- ❌ Keywords explícitas en el texto

**Solución implementada**: Notebooks refactorizados usando **solo features del texto** con métricas realistas (F1 ~0.85-0.92).

---

## 📂 Estructura del Proyecto

```
Phishing-Emails-ML/
│
├── Dataset/
│   └── phishing_legit_dataset_KD_10000.csv  # Dataset original (10k emails)
│
├── notebook/
│   ├── phishing_email.ipynb                 # ⚠️ Notebook original (con data leakage)
│   ├── 01_clasificacion_binaria_sklearn.ipynb  # ✅ Clasificación binaria correcta
│   └── 02_clasificacion_multiclase.ipynb      # ✅ Clasificación de tipos de phishing
│
├── imgs/                                     # Imágenes y visualizaciones
├── Paper/                                    # Documentación académica
│
├── ANALISIS_DATA_LEAKAGE.md                 # 🚨 Documentación del problema detectado
└── README.md                                 # Este archivo
```

---

## 🚀 Notebooks Disponibles

### 1️⃣ **01_clasificacion_binaria_sklearn.ipynb** ✅
**Objetivo**: Clasificar emails como phishing (1) o legítimo (0) usando **solo texto**

**Características**:
- ❌ NO usa `phishing_type`, `confidence`, ni `severity` (data leakage)
- ✅ Solo usa TF-IDF + features del texto (longitud, palabras)
- ✅ Implementación con **pipelines de scikit-learn**
- ✅ Optimización de hiperparámetros con **GridSearchCV**
- ✅ Evaluación en Train/Validation/Test con métricas apropiadas

**Modelos implementados**:
1. Regresión Logística (L2 regularization)
2. Naive Bayes (baseline)
3. SVM Lineal
4. Random Forest

**Métricas objetivo**:
- Accuracy: 85-92%
- F1-Score: 0.83-0.90
- ROC-AUC: 0.88-0.95

---

### 2️⃣ **02_clasificacion_multiclase.ipynb** ✅
**Objetivo**: Clasificar emails **phishing** por tipo específico

**Características**:
- Filtra solo emails phishing (label=1)
- Clasifica entre múltiples tipos: credential_harvesting, financial_scam, authority_scam, urgency, etc.
- Manejo de desbalance con `class_weight='balanced'`
- Métricas multi-clase: F1-Macro, F1-Weighted

**Modelos implementados**:
1. Random Forest
2. Gradient Boosting
3. Logistic Regression Multinomial

**Análisis incluido**:
- Matriz de confusión multi-clase
- Reporte detallado por clase
- Análisis de confusiones más comunes
- Feature importance

---

### ⚠️ **phishing_email.ipynb** (Original - CON DATA LEAKAGE)
**Estado**: Mantenido como referencia histórica

**Problemas**:
- Usa `phishing_type` como feature → 100% predictivo
- Usa `confidence` → diferencias artificiales
- Resultados no válidos para producción

**Nota**: Ver documentación en `ANALISIS_DATA_LEAKAGE.md`

---

## 📊 Resultados Esperados (Sin Data Leakage)

### Clasificación Binaria:
| Modelo | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|----------|-----------|--------|----------|---------|
| Logistic Regression | ~0.89 | ~0.88 | ~0.90 | ~0.89 | ~0.93 |
| SVM | ~0.90 | ~0.89 | ~0.91 | ~0.90 | ~0.94 |
| Random Forest | ~0.88 | ~0.87 | ~0.89 | ~0.88 | ~0.92 |

### Clasificación Multi-Clase:
| Modelo | Accuracy | F1-Macro | F1-Weighted |
|--------|----------|----------|-------------|
| Random Forest | ~0.82 | ~0.79 | ~0.83 |
| Gradient Boosting | ~0.84 | ~0.81 | ~0.85 |
| LR Multinomial | ~0.80 | ~0.77 | ~0.81 |

**Nota**: Estos valores son **realistas** y demuestran aprendizaje genuino de patrones lingüísticos.

---

## 🛠️ Instalación y Uso

### Requisitos:
```bash
python >= 3.8
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter
```

### Instalación:
```bash
# Clonar repositorio
git clone https://github.com/danielarodriguez4/Phishing-Emails-ML.git
cd Phishing-Emails-ML

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### Ejecución:
```bash
# Iniciar Jupyter
jupyter notebook

# Abrir notebooks en orden:
# 1. notebook/01_clasificacion_binaria_sklearn.ipynb
# 2. notebook/02_clasificacion_multiclase.ipynb
```

---

## 📖 Referencias

### Curso Base:
- **Introducción al Machine Learning 2025**: https://jdariasl.github.io/Intro_ML_2025

### Documentación Oficial:
- **Scikit-learn**: https://scikit-learn.org/stable/
- **TF-IDF**: https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting
- **GridSearchCV**: https://scikit-learn.org/stable/modules/grid_search.html

### Papers de Referencia:
- Kaufman et al. (2012) - "Leakage in Data Mining: Formulation, Detection, and Avoidance"
- Pedregosa et al. (2011) - "Scikit-learn: Machine Learning in Python"

---

## 🔍 Metodología

### 1. **Análisis Exploratorio (EDA)**
- Distribución de clases
- Análisis de texto (longitud, palabras)
- Detección de valores nulos
- **Identificación de data leakage**

### 2. **Preprocesamiento**
- Limpieza de texto (URLs, emails, puntuación)
- Remoción de keywords artificiales
- TF-IDF vectorization (unigrams + bigrams)
- División estratificada: 60% train, 20% val, 20% test

### 3. **Modelado**
- Pipelines de scikit-learn
- GridSearchCV para optimización
- Validación cruzada (5-fold)
- Regularización (L2 para Logistic Regression)

### 4. **Evaluación**
- Métricas apropiadas: Precision, Recall, F1-Score, ROC-AUC
- Matrices de confusión
- Curvas de aprendizaje
- Análisis de errores (FP, FN)

---

## 💡 Hallazgos Clave

### ✅ Mejores Prácticas Aplicadas:
1. **Eliminación de data leakage**: Solo features del texto
2. **Pipelines**: Preprocesamiento reproducible
3. **GridSearchCV**: Optimización sistemática
4. **Métricas apropiadas**: No solo accuracy
5. **Análisis de errores**: Identificación de FP/FN críticos

### 📊 Insights del Análisis:
- **Patrones lingüísticos**: Phishing usa más urgencia ("act now", "expires", "urgent")
- **Longitud**: Emails phishing tienden a ser más cortos
- **Bigramas**: Secuencias como "click here", "verify account" son altamente predictivas
- **Confusiones comunes**: Algunos tipos de phishing son difíciles de distinguir (urgency vs authority_scam)

---

## ⚠️ Limitaciones

1. **Dataset sintético**: No refleja 100% el phishing real
2. **Keywords artificiales**: Algunos patrones pueden ser demasiado obvios
3. **Concept drift**: Phishing evoluciona constantemente
4. **Idioma**: Solo inglés

### Recomendaciones para Producción:
- Reentrenamiento periódico con nuevos datos
- Combinación con otras señales (sender, headers, links)
- Monitoreo de performance en tiempo real
- Ajuste de umbral según costo de FP vs FN

---

## 📄 Licencia

Este proyecto es parte de un trabajo académico. El dataset utilizado es de dominio público (sintético).

---

## 🤝 Contribuciones

Para reportar problemas o sugerir mejoras:
1. Crear un **Issue** en GitHub
2. Fork del repositorio
3. Pull Request con descripción detallada

---

## 📞 Contacto

- **Daniela Rodríguez Chacón**: [GitHub](https://github.com/danielarodriguez4)
- **Estiven Ospina González**: [GitHub](https://github.com/eospgonz10)

---

## 🎓 Agradecimientos

- Prof. Julian Arias (Curso Intro ML 2025)
- Scikit-learn community
- Dataset creators (synthetic phishing emails)
