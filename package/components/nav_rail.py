from flet import *
from package.components.about_dialog import AboutDialog


class NavRail(UserControl):
    def __init__(self, page: Page, body_change, state: dict):
        super().__init__()
        self.body_change = body_change
        self.page: Page = page
        self.state = state
        self.about_dialog = AboutDialog(page)

    def about_detail(self, e):
        self.about_dialog.open_dlg(e)

    def build(self):
        return Column(
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                NavigationRail(
                    selected_index = self.state['selected_index'],
                    bgcolor=colors.BACKGROUND,
                    label_type = NavigationRailLabelType.SELECTED,
                    destinations = [
                        NavigationRailDestination(
                            icon = icons.HOME_OUTLINED,
                            selected_icon = icons.HOME,
                            label = "Home"
                        ),
                        NavigationRailDestination(
                            icon = icons.RECOMMEND_OUTLINED,
                            selected_icon = icons.RECOMMEND,
                            label = "Rekom"
                        ),
                    ],
                    on_change = self.body_change,
                    expand = True
                ),
                ElevatedButton(
                    icon = icons.INFO,
                    text = "About",
                    on_click = self.about_detail
                )
            ]
        )
