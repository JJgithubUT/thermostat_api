---

```markdown
# ⚙️ Guía de Instalación — Thermostat API

Este documento te guía paso a paso para instalar y ejecutar el proyecto **Thermostat API** en un entorno local usando Python y Firebase.

---

## 🧩 Requisitos Previos

- ✅ Python 3.10+ instalado (descarga desde: [https://www.python.org/downloads/](https://www.python.org/downloads/))
- ✅ Acceso a un proyecto en Firebase con:
  - Firestore habilitado
  - Realtime Database habilitado
  - Obtener credenciales en PROYECTODEFIREBASE -> SDK de Firebase Admin -> Generar nueva clase privada y descargar
  - Credenciales del Admin SDK descargadas (`firebase_config.json`), debe llevar tal nomenclatura el archivo JSON descargado

---

## 🛠️ Paso a Paso

### 1. Clonar el repositorio

Abre una terminal y navega al directorio donde deseas instalar el proyecto:

```bash
git clone https://github.com/JJgithubUT/thermostat_api.git
cd thermostat_api
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

> Si recibes un error de que no se encuentra Python, asegúrate de que está en el **PATH** del sistema.

### 3. Activar el entorno virtual

En Windows (CMD o PowerShell):

```bash
venv\Scripts\activate
```

En Git Bash:

```bash
source venv/Scripts/activate
```

Verás algo como esto al principio de la línea:
```bash
(venv) C:\CLIMATICAPI\thermostat_api>
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Agregar archivo de configuración de Firebase

Coloca tu archivo `firebase_config.json` en la raíz del proyecto. Este archivo lo obtienes desde:

- Firebase Console → Configuración del Proyecto → Cuentas de servicio → Generar nueva clave privada

### 6. Ejecutar el proyecto

```bash
python main.py
```

---

## 🚀 Verificación

Si todo fue correcto, verás en consola algo como:

```
⏳ Esperando cada X minutos para guardar historial...
✅ Dispositivo esp32trycsrp133 registrado en historial.
```

Esto indica que se están leyendo correctamente los dispositivos desde Firestore y Realtime Database, y se está escribiendo en la colección `historial`.

---

## 🆘 Errores comunes

| Error | Solución |
|------|----------|
| `pip: command not found` | Agrega Python y Scripts al PATH del sistema |
| ejemplo de ruta para variable ne path de sistema: `C:\Users\TuUsuario\AppData\Local\Programs\Python\Python313\Scripts` |
| `firebase_admin` no se encuentra | Asegúrate de haber ejecutado `pip install -r requirements.txt` |
| No se encuentra `firebase_config.json` | Asegúrate de haberlo descargado desde Firebase y colocado correctamente |

---

## 📬 Soporte

Si tienes dudas sobre la instalación, puedes contactar al autor en:

**Correo:** juanjcbreton@gmail.com

---

```

¿Quieres que te lo deje en un archivo `.md` listo para guardar o copiar directamente en el proyecto?