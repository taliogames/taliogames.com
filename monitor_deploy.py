import requests
import time
import winsound  # Específico para Windows
import sys
from datetime import datetime

# --- CONFIGURACIÓN ---
USER = "taliogames"
REPO = "taliogames.com"
BRANCH = "main" 
CHECK_INTERVAL = 15 # Segundos entre cada chequeo

API_URL = f"https://api.github.com/repos/{USER}/{REPO}/actions/runs"

def play_success_alarm():
    """Sonido de victoria 🎵"""
    try:
        winsound.Beep(1000, 200)
        winsound.Beep(1500, 200)
        winsound.Beep(1000, 200)
        winsound.Beep(2000, 600)
    except:
        pass

def play_failure_alarm():
    """Sonido de error ❌"""
    try:
        winsound.Beep(500, 800)
        winsound.Beep(400, 800)
    except:
        pass

def monitor_continuously():
    print(f"\n📡 --- MONITOR ACTIVO para {USER}/{REPO} ---")
    print("ℹ️  El script se ejecutará indefinidamente.")
    print("ℹ️  Te avisará cada vez que un NUEVO despliegue termine.")
    print("------------------------------------------------------")

    # Variables de estado para rastrear el último run conocido
    last_known_id = None
    last_known_status = None
    
    # Primera llamada para establecer una línea base (para no sonar por cosas viejas)
    try:
        response = requests.get(API_URL, params={"per_page": 1, "branch": BRANCH})
        if response.status_code == 200:
            data = response.json()
            if "workflow_runs" in data and len(data["workflow_runs"]) > 0:
                initial_run = data["workflow_runs"][0]
                last_known_id = initial_run["id"]
                last_known_status = initial_run["status"]
                
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Estado inicial: {last_known_status.upper()} (ID: {last_known_id})")
                
                # Si ya estaba completado al abrir el script, no hacemos ruido, solo esperamos el siguiente
                if last_known_status == "completed":
                    print("--> El último despliegue ya estaba finalizado. Esperando nuevos commits...")
            else:
                print("No se encontró historial previo. Esperando primer commit...")
    except Exception as e:
        print(f"Error inicial: {e}")

    # Bucle infinito
    while True:
        try:
            time.sleep(CHECK_INTERVAL) # Esperar antes de consultar
            
            response = requests.get(API_URL, params={"per_page": 1, "branch": BRANCH})
            
            if response.status_code == 200:
                data = response.json()
                
                if "workflow_runs" in data and len(data["workflow_runs"]) > 0:
                    latest_run = data["workflow_runs"][0]
                    current_id = latest_run["id"]
                    current_status = latest_run["status"]       # queued, in_progress, completed
                    conclusion = latest_run["conclusion"]       # success, failure
                    run_name = latest_run["name"]
                    timestamp = datetime.now().strftime("%H:%M:%S")

                    # CASO 1: Detectamos un NUEVO commit/run que no habíamos visto antes
                    if current_id != last_known_id:
                        print(f"\n[{timestamp}] 🚀 NUEVO DESPLIEGUE DETECTADO: '{run_name}'")
                        print(f"[{timestamp}] Estado: {current_status.upper()}")
                        last_known_id = current_id
                        last_known_status = current_status

                    # CASO 2: Es el mismo run que estábamos mirando, pero cambió su estado
                    elif current_status != last_known_status:
                        print(f"[{timestamp}] 🔄 Cambio de estado: {last_known_status} -> {current_status.upper()}")
                        last_known_status = current_status
                        
                        # Si acaba de terminar, notificamos
                        if current_status == "completed":
                            if conclusion == "success":
                                print(f"[{timestamp}] ✅ ¡LISTO! Cambios publicados con éxito.")
                                play_success_alarm()
                            else:
                                print(f"[{timestamp}] ❌ FALLÓ. Algo salió mal en el build.")
                                play_failure_alarm()
                            
                            print("--> Volviendo a vigilar por futuros cambios...")

                    # CASO 3: Sigue en progreso (feedback visual pequeño)
                    elif current_status in ["queued", "in_progress"]:
                        sys.stdout.write(".")
                        sys.stdout.flush()

        except Exception as e:
            print(f"\nError de conexión momentáneo: {e}")
            # No cerramos el script, solo reintentamos en el siguiente ciclo

if __name__ == "__main__":
    try:
        monitor_continuously()
    except KeyboardInterrupt:
        print("\n\n👋 Monitor detenido por el usuario.")