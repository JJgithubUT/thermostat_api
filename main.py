import firebase_admin
from firebase_admin import credentials, firestore, db
import time
import threading
from datetime import datetime
import pytz

# Inicializar Firebase Admin
cred = credentials.Certificate("firebase_config.json")  # <-- Cambia esto por el path a tu JSON
firebase_admin.initialize_app(cred, {
    # Cambia esto por tu URL del Realtime DB
    'databaseURL': 'https://termostato-3ab33-default-rtdb.firebaseio.com/'
})

firestore_db = firestore.client()

# Variable global para tiempo de espera en minutos
TIEMPO_ESPERA_MIN = 1
LOCK = threading.Lock()

def lector_tiempo():
    global TIEMPO_ESPERA_MIN
    print("⏱️ Iniciando lector de tiempo de espera desde Firestore...")
    while True:
        try:
            docs = firestore_db.collection('globalconfig').limit(1).stream()
            for doc in docs:
                timestamp = doc.to_dict().get('tiempo_espera_his')
                if timestamp:
                    with LOCK:
                        nuevo_valor = int(timestamp.minute)
                        if nuevo_valor != TIEMPO_ESPERA_MIN:
                            print(f"🔄 Tiempo de espera actualizado: {nuevo_valor} minutos")
                        TIEMPO_ESPERA_MIN = nuevo_valor
        except Exception as e:
            print(f"⚠️ Error leyendo tiempo de espera: {e}")
        time.sleep(30)  # Checar cada 30 segundos si cambia el tiempo

def obtener_dispositivos_realtime():
    ref = db.reference('/')
    return ref.get() or {}

def guardar_en_historial(codigo_dis, datos):
    firestore_db.collection('historial').add({
        'codigo_his': codigo_dis,
        'fecha_his': firestore.SERVER_TIMESTAMP,
        'temp_actual_his': datos.get('temp_actual_dis'),
        'temp_objetivo_his': datos.get('temp_objetivo_dis')
    })

def ejecutor_historial():
    global TIEMPO_ESPERA_MIN
    print("📦 Iniciando ejecución periódica del guardado en historial...")
    while True:
        with LOCK:
            tiempo = TIEMPO_ESPERA_MIN

        print(f"[{datetime.now()}] Ejecutando recolección cada {tiempo} minutos...")
        try:
            dispositivos = obtener_dispositivos_realtime()
            for codigo_dis, datos in dispositivos.items():
                if 'temp_actual_dis' in datos and 'temp_objetivo_dis' in datos:
                    print(f"✅ Guardando historial de {codigo_dis}: {datos}")
                    guardar_en_historial(codigo_dis, datos)
        except Exception as e:
            print(f"⚠️ Error en recolección y guardado: {e}")

        time.sleep(tiempo * 60)

if __name__ == "__main__":
    print("🚀 API de Historial CLIMATIC iniciando...")

    # Crear hilos
    hilo_lector = threading.Thread(target=lector_tiempo, daemon=True)
    hilo_ejecutor = threading.Thread(target=ejecutor_historial, daemon=True)

    # Iniciar hilos
    hilo_lector.start()
    hilo_ejecutor.start()

    # Mantener vivo el proceso principal
    hilo_lector.join()
    hilo_ejecutor.join()