# 🚀 GUÍA DE INICIO RÁPIDO

**Proyecto**: Phishing-Emails-ML  
**Última actualización**: 17 de Noviembre, 2025

---

## ⚡ Inicio en 5 Minutos

### 1. Clonar el Repositorio
```bash
git clone https://github.com/danielarodriguez4/Phishing-Emails-ML.git
cd Phishing-Emails-ML
```

### 2. Instalar Dependencias
```bash
# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# O: venv\Scripts\activate  # Windows

# Instalar paquetes
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 3. Ejecutar Demo Rápido
```bash
python phishing_classifier_demo.py
```

**Salida esperada**:
```
✅ Dataset cargado: 10,000 emails
✅ Modelo entrenado exitosamente
Accuracy:    0.8900
F1-Score:    0.8850
🤖 PREDICCIÓN: PHISHING (98.74%)
✅ CORRECTO
```

---

## 📓 Notebooks Principales

### Opción A: Jupyter Notebook
```bash
jupyter notebook

# Abrir en orden:
# 1. notebook/01_clasificacion_binaria_sklearn.ipynb
# 2. notebook/02_clasificacion_multiclase.ipynb
```

### Opción B: VS Code
```bash
code .
# Abrir los archivos .ipynb con la extensión de Jupyter
```

---

## 📂 Archivos Importantes

### 🔴 **USAR ESTOS** (Sin data leakage):
- ✅ `notebook/01_clasificacion_binaria_sklearn.ipynb` - Clasificación binaria correcta
- ✅ `notebook/02_clasificacion_multiclase.ipynb` - Clasificación multi-clase
- ✅ `phishing_classifier_demo.py` - Script de demostración

### ⚠️ **REFERENCIA HISTÓRICA** (Con data leakage):
- ⚠️ `notebook/phishing_email.ipynb` - Original (mantener como referencia)

### 📖 **DOCUMENTACIÓN**:
- 📄 `README.md` - Descripción general del proyecto
- 📄 `ANALISIS_DATA_LEAKAGE.md` - Explicación del problema detectado
- 📄 `RECOMENDACIONES_FINALES.md` - Guía completa (30+ páginas)
- 📄 `RESUMEN_TRABAJO.md` - Resumen del trabajo realizado

---

## 🎯 Flujo Recomendado

### Para Aprender sobre el Proyecto:
```
1. Leer README.md (5 min)
   ↓
2. Ejecutar phishing_classifier_demo.py (2 min)
   ↓
3. Explorar 01_clasificacion_binaria_sklearn.ipynb (30 min)
   ↓
4. Explorar 02_clasificacion_multiclase.ipynb (20 min)
   ↓
5. Leer ANALISIS_DATA_LEAKAGE.md (10 min)
```

### Para Presentación/Paper:
```
1. Leer RESUMEN_TRABAJO.md (10 min)
   ↓
2. Ejecutar notebooks 01 y 02 (15 min)
   ↓
3. Preparar slides con resultados (30 min)
```

### Para Desarrollo/Mejoras:
```
1. Leer RECOMENDACIONES_FINALES.md (30 min)
   ↓
2. Revisar código en notebooks 01 y 02 (30 min)
   ↓
3. Implementar mejoras propuestas
```

---

## 🔧 Comandos Útiles

### Verificar Instalación
```bash
# Python version (debe ser >= 3.8)
python --version

# Paquetes instalados
pip list | grep -E "pandas|numpy|scikit-learn|jupyter"

# Estructura del proyecto
tree -L 2 -I '__pycache__|*.pyc'
```

### Ejecutar Notebooks desde Terminal
```bash
# Convertir notebook a script y ejecutar
jupyter nbconvert --to script notebook/01_clasificacion_binaria_sklearn.ipynb
python notebook/01_clasificacion_binaria_sklearn.py
```

### Limpiar Outputs de Notebooks
```bash
# Si quieres limpiar outputs de notebooks
jupyter nbconvert --clear-output --inplace notebook/*.ipynb
```

---

## 📊 Resultados Esperados

### Clasificación Binaria (phishing vs legítimo)
```
Modelo Óptimo: Logistic Regression
├── Accuracy:    0.89 - 0.92
├── Precision:   0.88 - 0.91
├── Recall:      0.87 - 0.90
├── F1-Score:    0.88 - 0.91
└── ROC-AUC:     0.91 - 0.95
```

### Clasificación Multi-Clase (tipos de phishing)
```
Modelo Óptimo: Random Forest / Gradient Boosting
├── Accuracy:    0.80 - 0.85
├── F1-Macro:    0.77 - 0.82
└── F1-Weighted: 0.81 - 0.86
```

**Nota**: Si ves 100% accuracy, revisa que no estés usando el notebook original con data leakage.

---

## ⚠️ Problemas Comunes

### Error: "No module named 'sklearn'"
```bash
# Solución:
pip install scikit-learn
```

### Error: "FileNotFoundError: Dataset/..."
```bash
# Solución: Ejecutar desde la raíz del proyecto
cd /ruta/a/Phishing-Emails-ML
python phishing_classifier_demo.py
```

### Jupyter no inicia
```bash
# Solución:
pip install --upgrade jupyter
jupyter notebook --version  # Verificar
```

### Numpy/Pandas versiones incompatibles
```bash
# Solución:
pip install --upgrade numpy pandas scikit-learn
```

---

## 💡 Tips Rápidos

### 1. Ver solo la estructura de un notebook sin ejecutar:
```bash
jupyter nbconvert notebook/01_*.ipynb --to markdown --stdout | head -100
```

### 2. Ejecutar todas las celdas de un notebook:
```python
# En Jupyter: Cell > Run All
# O tecla rápida: Shift + Enter (celda por celda)
```

### 3. Exportar notebook a HTML:
```bash
jupyter nbconvert notebook/01_*.ipynb --to html
```

### 4. Verificar métricas sin ejecutar todo:
```python
# En Python:
from sklearn.metrics import classification_report
import joblib

# Cargar modelo guardado (si existe)
model = joblib.load('modelo.pkl')
print(classification_report(y_test, model.predict(X_test)))
```

---

## 📚 Documentación Adicional

### Enlaces Útiles:
- **Curso base**: https://jdariasl.github.io/Intro_ML_2025
- **Scikit-learn**: https://scikit-learn.org/stable/
- **TF-IDF**: https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf
- **GridSearchCV**: https://scikit-learn.org/stable/modules/grid_search.html

### Archivos de Referencia:
| Archivo | Propósito | Tiempo de Lectura |
|---------|-----------|-------------------|
| README.md | Visión general | 5 min |
| ANALISIS_DATA_LEAKAGE.md | Problema detectado | 10 min |
| RECOMENDACIONES_FINALES.md | Guía completa | 30 min |
| RESUMEN_TRABAJO.md | Trabajo realizado | 15 min |

---

## 🎓 Siguientes Pasos

### Nivel Principiante:
1. ✅ Ejecutar demo script
2. ✅ Leer README completo
3. ✅ Explorar notebook 01 (sin ejecutar todo)
4. ✅ Entender el problema de data leakage

### Nivel Intermedio:
1. ✅ Ejecutar notebooks 01 y 02 completamente
2. ✅ Modificar hiperparámetros en GridSearchCV
3. ✅ Probar con tus propios ejemplos de emails
4. ✅ Leer RECOMENDACIONES_FINALES.md

### Nivel Avanzado:
1. ✅ Implementar feature engineering adicional (URLs, headers)
2. ✅ Probar embeddings (Word2Vec, BERT)
3. ✅ Crear API REST para el modelo
4. ✅ Validar con dataset real de phishing

---

## 🤝 Necesitas Ayuda?

### Opciones:
1. **Documentación**: Revisar archivos MD en el proyecto
2. **Issues**: Crear issue en GitHub con detalles del problema
3. **Demo script**: Ejecutar para verificar que el setup funciona

### Al reportar un problema, incluir:
- Versión de Python: `python --version`
- Sistema operativo
- Comando ejecutado
- Error completo (traceback)

---

## ✅ Checklist de Verificación

Antes de empezar, verifica que tienes:
- [ ] Python >= 3.8 instalado
- [ ] Repositorio clonado
- [ ] Dependencias instaladas (`pip install ...`)
- [ ] Dataset en `Dataset/phishing_legit_dataset_KD_10000.csv`
- [ ] Jupyter funcionando (`jupyter notebook --version`)

Si todos los puntos están ✅, estás listo para empezar!

---

## 🚀 ¡Comienza Ahora!

```bash
# Comando único para todo:
python phishing_classifier_demo.py && \
jupyter notebook notebook/01_clasificacion_binaria_sklearn.ipynb
```

**¡Buena suerte! 🎉**

---

**Última actualización**: 17 de Noviembre, 2025  
**Mantenedores**: Daniela Rodríguez & Estiven Ospina
