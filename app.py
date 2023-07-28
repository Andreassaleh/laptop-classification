from flet import *
from package.screens.home import Home
from package.screens.recommendation import Recommendation
from package.screens.result import Recommend
from package.theme import CustomTheme
from package.components.nav_rail import NavRail
from package.models.laptop import Laptop
import json


def get_laptop_data(json_data):
    laptops  = []

    for data in json_data:
        laptops.append(Laptop(data))

    return laptops

def main(page: Page):
    def set_theme(e):
        if state['is_clicked']:
            theme_button.icon = icons.LIGHT_MODE
            page.theme_mode = ThemeMode.LIGHT
        else:
            theme_button.icon = icons.DARK_MODE
            page.theme_mode = ThemeMode.DARK
        state['is_clicked'] = not state['is_clicked']
        page.update()

    def body_change(e: ControlEvent):
        body.content = body_contents[e.control.selected_index]
        state['selected_index'] = e.control.selected_index
        page.update()

    def set_is_filtered(event, value):
        if not value:
            body.content = Home(page, laptops, state)
        else:
            body_contents[0] = Recommend(set_is_filtered, page, laptops)
            page.snack_bar = SnackBar(
                behavior=SnackBarBehavior.FLOATING,
                margin=50,
                width=550,
                content=Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Icon(
                            icons.CHECK,
                            color=colors.GREEN_600,
                            size=50
                        ),
                        Container(padding=5),
                        Text(
                            "Rekomendasi telah dibuat, silahkan lihat pada halaman Home !",
                            weight=FontWeight.BOLD
                        )
                    ]
                )
            )
            page.snack_bar.open = True
        page.update()

    def set_rail(e):
        if state['is_rail_expanded']:
            page_contents.controls = [
                NavRail(page, body_change, state),
                VerticalDivider(width = 1),
                body
            ]
        else:
            page_contents.controls = [body]
        state['is_rail_expanded'] = not state['is_rail_expanded']
        page.update()

    theme_button = IconButton(
        icons.DARK_MODE,
        on_click = set_theme
    )

    body_contents = [
        Home(page, laptops, state),
        Recommendation(page, set_is_filtered)
    ]

    body = Container(
        content = body_contents[0],
        expand = True
    )

    page_contents = Row(
        alignment = MainAxisAlignment.CENTER,
        controls = [
            NavRail(page, body_change, state),
            VerticalDivider(width = 1),
            body
        ],
        expand = True
    )

    page.dark_theme = CustomTheme.DARK_THEME
    page.theme = CustomTheme.LIGHT_THEME
    page.theme_mode = ThemeMode.DARK
    page.bgcolor = colors.BACKGROUND
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.appbar = AppBar(
        bgcolor = colors.SURFACE_VARIANT,
        leading = IconButton(
            icon = icons.MENU,
            on_click = set_rail
        ),
        title = Text("Sistem Pemilihan Laptop"),
        center_title = True,
        actions = [
            theme_button
        ]
    )
    page.add(
        page_contents
    )

if __name__ == '__main__':
    state = {
        'is_clicked': True,
        'is_rail_expanded': False,
        'selected_index': 0,
        'min': 0,
        'max': 10
    }

    laptops = []
    laptop_is_filtered = []

    with open("package/data/laptops.json", "r") as file:
        laptop_data = json.load(file)
        laptops = get_laptop_data(laptop_data)

    app(target=main, assets_dir="package/assets")
