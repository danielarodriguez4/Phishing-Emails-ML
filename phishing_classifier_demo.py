#!/usr/bin/env python3
"""
Script de Ejemplo: Clasificador de Phishing Emails

Este script demuestra cómo usar el modelo entrenado para clasificar nuevos emails.

Uso:
    python phishing_classifier_demo.py

Autor: Daniela Rodríguez & Estiven Ospina
Fecha: 17 de Noviembre, 2025
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import re
import string


# ========== FUNCIONES DE PREPROCESAMIENTO ==========

def clean_text(text):
    """
    Limpia el texto de un email removiendo elementos no útiles.
    
    Args:
        text (str): Texto original del email
    
    Returns:
        str: Texto limpio
    """
    text = str(text).lower()
    
    # Remover línea de keywords (leakage artificial)
    text = re.sub(r'keywords?:.*', '', text, flags=re.IGNORECASE)
    
    # Remover URLs y emails
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remover números y puntuación
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remover espacios múltiples
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


# ========== ENTRENAMIENTO DEL MODELO ==========

def train_phishing_classifier(dataset_path):
    """
    Entrena un clasificador de phishing usando el dataset.
    
    Args:
        dataset_path (str): Ruta al archivo CSV del dataset
    
    Returns:
        Pipeline: Modelo entrenado
        dict: Métricas de evaluación
    """
    print("="*70)
    print("ENTRENAMIENTO DE CLASIFICADOR DE PHISHING")
    print("="*70)
    
    # Cargar datos
    print("\n📂 Cargando dataset...")
    df = pd.read_csv(dataset_path, encoding="utf-8")
    print(f"✅ Dataset cargado: {len(df):,} emails")
    
    # Limpiar texto
    print("\n🧹 Limpiando textos...")
    df['text_clean'] = df['text'].apply(clean_text)
    
    # Preparar X e y (SOLO TEXTO - sin data leakage)
    X = df['text_clean'].values
    y = df['label'].values
    
    print(f"✅ Distribución de clases:")
    print(f"   Legítimos (0): {(y==0).sum():,} ({(y==0).sum()/len(y)*100:.1f}%)")
    print(f"   Phishing (1):  {(y==1).sum():,} ({(y==1).sum()/len(y)*100:.1f}%)")
    
    # División de datos
    print("\n📊 Dividiendo datos...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    print(f"✅ Train: {len(y_train):,} | Test: {len(y_test):,}")
    
    # Crear pipeline
    print("\n🤖 Creando pipeline de ML...")
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(
            max_features=3000,
            ngram_range=(1, 2),
            max_df=0.85,
            min_df=5,
            stop_words='english',
            sublinear_tf=True
        )),
        ('clf', LogisticRegression(
            C=1.0,
            max_iter=1000,
            random_state=42,
            solver='saga',
            n_jobs=-1
        ))
    ])
    
    # Entrenar
    print("\n🔄 Entrenando modelo...")
    pipeline.fit(X_train, y_train)
    print("✅ Modelo entrenado exitosamente")
    
    # Evaluar
    from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
    
    y_pred = pipeline.predict(X_test)
    
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1_score': f1_score(y_test, y_pred)
    }
    
    print("\n" + "="*70)
    print("MÉTRICAS EN TEST SET")
    print("="*70)
    for metric, value in metrics.items():
        print(f"{metric:12s}: {value:.4f}")
    
    return pipeline, metrics


# ========== FUNCIÓN DE PREDICCIÓN ==========

def predict_email(model, email_text, show_probability=True):
    """
    Clasifica un email como phishing o legítimo.
    
    Args:
        model (Pipeline): Modelo entrenado
        email_text (str): Texto del email a clasificar
        show_probability (bool): Si mostrar probabilidades
    
    Returns:
        dict: Resultado de la clasificación
    """
    # Limpiar texto
    text_clean = clean_text(email_text)
    
    # Predecir
    prediction = model.predict([text_clean])[0]
    
    result = {
        'text': email_text[:100] + "..." if len(email_text) > 100 else email_text,
        'prediction': 'PHISHING' if prediction == 1 else 'LEGÍTIMO',
        'label': int(prediction)
    }
    
    if show_probability:
        proba = model.predict_proba([text_clean])[0]
        result['prob_legit'] = proba[0]
        result['prob_phishing'] = proba[1]
    
    return result


# ========== EJEMPLOS DE USO ==========

def demo_predictions(model):
    """
    Muestra ejemplos de predicciones con el modelo.
    """
    print("\n" + "="*70)
    print("EJEMPLOS DE PREDICCIONES")
    print("="*70)
    
    # Ejemplos de emails (sintéticos)
    test_emails = [
        {
            'text': """Subject: Project Update
            
            Hi team, I've finished the analysis and pushed the changes to the repo. 
            Please review when you have time.
            
            Best regards,
            John""",
            'expected': 'LEGÍTIMO'
        },
        {
            'text': """URGENT: Your account has been suspended!
            
            Click here immediately to verify your identity and restore access.
            You must act now or your account will be permanently deleted.
            
            Security Team""",
            'expected': 'PHISHING'
        },
        {
            'text': """Congratulations! You've won $10,000!
            
            To claim your prize, please provide your credit card information.
            This offer expires in 24 hours.
            
            Click here now!""",
            'expected': 'PHISHING'
        },
        {
            'text': """Subject: Meeting notes
            
            Thanks for attending today's meeting. I've attached the notes and action items.
            Let me know if I missed anything.
            
            Cheers,
            Sarah""",
            'expected': 'LEGÍTIMO'
        }
    ]
    
    for i, email in enumerate(test_emails, 1):
        print(f"\n{'='*70}")
        print(f"EJEMPLO {i} (Esperado: {email['expected']})")
        print(f"{'='*70}")
        
        result = predict_email(model, email['text'])
        
        print(f"Texto: {result['text']}")
        print(f"\n🤖 PREDICCIÓN: {result['prediction']}")
        print(f"📊 Probabilidades:")
        print(f"   Legítimo: {result['prob_legit']*100:.2f}%")
        print(f"   Phishing: {result['prob_phishing']*100:.2f}%")
        
        # Verificar si es correcto
        if result['prediction'] == email['expected']:
            print("✅ CORRECTO")
        else:
            print("❌ INCORRECTO")


# ========== MAIN ==========

def main():
    """Función principal."""
    print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║        CLASIFICADOR DE PHISHING EMAILS - DEMOSTRACIÓN           ║
    ║                                                                  ║
    ║  Autores: Daniela Rodríguez & Estiven Ospina                   ║
    ║  Fecha: 17 de Noviembre, 2025                                   ║
    ╚══════════════════════════════════════════════════════════════════╝
    """)
    
    # Ruta al dataset
    dataset_path = "Dataset/phishing_legit_dataset_KD_10000.csv"
    
    try:
        # Entrenar modelo
        model, metrics = train_phishing_classifier(dataset_path)
        
        # Demostrar predicciones
        demo_predictions(model)
        
        print("\n" + "="*70)
        print("✅ DEMOSTRACIÓN COMPLETADA")
        print("="*70)
        print("\nPara usar el modelo en tus propios emails:")
        print("  result = predict_email(model, 'tu texto aquí')")
        print("\nPara entrenar con mejores hiperparámetros:")
        print("  Ver notebook: 01_clasificacion_binaria_sklearn.ipynb")
        
    except FileNotFoundError:
        print(f"\n❌ ERROR: No se encontró el dataset en '{dataset_path}'")
        print("   Asegúrate de ejecutar desde la raíz del proyecto")
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")


if __name__ == "__main__":
    main()
