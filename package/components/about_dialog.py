from flet import *


class AboutDialog(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page: Page = page
        self.dlg = AlertDialog(
            title = Row(
                controls = [
                    Icon(icons.INFO),
                    Text("About")
                ]
            ),
            content = Container(
                width = 360,
                height = 60,
                content = Column(
                    controls = [
                        Row(
                            controls = [
                                Text("Author:"),
                                Text("Niko", weight=FontWeight.BOLD)
                            ]
                        ),
                        Row(
                            controls = [
                                Text("Version:"),
                                Text("Alpha-0.7.11", weight=FontWeight.BOLD)
                            ]
                        )
                    ]
                )
            ),
            actions = [
                Column(
                    controls = [
                        Text("Find me on"),
                        Row(
                            alignment = MainAxisAlignment.SPACE_EVENLY,
                            controls = [
                                IconButton(
                                    content = Image(
                                        width = 20,
                                        height = 20,
                                        src = "package/assets/github.png",
                                        tooltip = "GitHub"
                                    )
                                ),
                                IconButton(
                                    content = Image(
                                        width = 20,
                                        height = 20,
                                        src = "package/assets/instagram.png",
                                        tooltip = "Instagram"
                                    )
                                ),
                                IconButton(
                                    content = Image(
                                        width = 20,
                                        height = 20,
                                        src = "package/assets/facebook.png",
                                        tooltip = "Facebook"
                                    )
                                ),
                                IconButton(
                                    content = Image(
                                        width = 20,
                                        height = 20,
                                        src = "package/assets/discord.png",
                                        tooltip = "Discord"
                                    )
                                ),
                            ]
                        )
                    ]
                )
            ]
        )

    def open_dlg(self, e):
        self.page.dialog = self.dlg
        self.dlg.open = True
        self.page.update()

    def build(self):
        return self.dlg