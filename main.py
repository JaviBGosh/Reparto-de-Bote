import flet as ft

class Profile:
    def __init__(self, name, service_number):
        self.name = name
        self.service_number = service_number
        self.money_to_receive = 0

    def __repr__(self):
        return f"{self.name} - Servicios: {self.service_number}"

def distribute_money(profiles, total_money):
    total_services = sum(int(profile.service_number) for profile in profiles)
    for profile in profiles:
        if total_services > 0:
            profile.money_to_receive = (int(profile.service_number) / total_services) * total_money

def main(page):
    profiles = []
    
    profile_listbox = ft.ListView(height=200)
    name_entry = ft.TextField(label="Nombre:", width=300)
    service_entry = ft.TextField(label="Servicio:", width=300)
    money_entry = ft.TextField(label="Bote:", width=300)
    results_text = ft.Text("")  # Control para mostrar los resultados

    def update_listbox():
        profile_listbox.controls.clear()  # Vaciar la lista actual
        for profile in profiles:
            profile_listbox.controls.append(ft.ListTile(title=ft.Text(value=profile.__repr__())))
        profile_listbox.update()

    def add_profile(e):
        try:
            name = name_entry.value.strip()
            service_number = service_entry.value.strip()
            if name and service_number:
                profile = Profile(name, service_number)
                profiles.append(profile)
                update_listbox()
                # Limpiar los campos
                name_entry.value = ''
                service_entry.value = ''
                # Asegurarse de que la interfaz de usuario refleje los campos limpios
                page.update()
        except ValueError:
            show_message("Error", "Por favor, introduzca un número válido de servicio.")

    def show_message(title, message):
        # Crear una ventana emergente simple para mensajes
        dialog = ft.Dialog(title=title, width=300, height=200)
        dialog.controls.append(ft.Text(value=message))
        dialog.open = True
        page.overlay.append(dialog)
        page.update()

    def reset_profiles(e):
        profiles.clear()  # Limpiar la lista de perfiles
        update_listbox()  # Actualizar la lista en la interfaz de usuario
        results_text.value = ""  # Limpiar los resultados
        page.update()  # Actualizar la página

    def calculate_distribution(e):
        try:
            total_money = float(money_entry.value)
            distribute_money(profiles, total_money)
            message = "\n".join([f"{profile.name} recibe: €{profile.money_to_receive:.2f}" for profile in profiles])
            results_text.value = message  # Mostrar los resultados en el control de texto
            page.update()
        except ValueError:
            show_message("Error", "Por favor, introduzca un número válido para el bote.")

    add_btn = ft.ElevatedButton(text="Añadir", on_click=add_profile)
    reset_btn = ft.ElevatedButton(text="Resetear", on_click=reset_profiles)  # Botón para resetear
    calc_btn = ft.ElevatedButton(text="Calcular", on_click=calculate_distribution)

    page.add(
        profile_listbox,
        name_entry,
        service_entry,
        ft.Row([add_btn, reset_btn]),
        money_entry,
        calc_btn,
        results_text  # Agregar el control de texto para los resultados
    )
    
    update_listbox()

ft.app(target=main)
