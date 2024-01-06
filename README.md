# Aplicación de Distribución de Bote

Esta es una aplicación web simple construida con Flet para administrar y calcular la distribución de un bote de dinero entre varios perfiles basada en el número de servicios proporcionados por cada uno.

## Características

- **Añadir Perfiles**: Los usuarios pueden añadir perfiles proporcionando un nombre y un número de servicios.
- **Calcular Distribución**: Los usuarios pueden calcular cómo se distribuirá el bote total entre los perfiles añadidos.
- **Resetear Lista**: Los usuarios pueden limpiar la lista de perfiles.
- **Visualización de Resultados**: Los resultados de la distribución del bote se muestran en la interfaz de usuario.

## Estructura del Código

- **Clase `Profile`**: Representa a un perfil con nombre, número de servicio y dinero a recibir.
- **Función `distribute_money`**: Calcula la distribución del bote entre los perfiles.
- **Función `main`**: Contiene la lógica de la interfaz de usuario y la interacción.

### Requisitos Previos

- Python 3.x
- Flet: Puedes instalarlo con `pip install flet`.

### Ejecución

Para ejecutar la aplicación, simplemente ejecuta el script Python en tu terminal:

```bash
python main.py
