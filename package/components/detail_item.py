from flet import *
from package.models.laptop import Laptop


class DetailItem(UserControl):
    def __init__(self, page: Page, item: Laptop, image: str):
        super().__init__()
        self.page: Page = page
        self.data: Laptop = item
        self.image = image
        self.dlg = AlertDialog(
        title = Text("Detail Item"),
        content = Container(
            width = 600,
            height = 200,
            content = Row(
                controls = [
                    Image(
                        src = self.image,
                        fit=ImageFit.COVER,
                    ),
                    ListView(
                        spacing=5,
                        auto_scroll = True,
                        controls = [
                            Column([
                                Container(
                                    width=330,
                                    content = Text(
                                        self.data.name,
                                        overflow = TextOverflow.FADE,
                                        text_align = TextAlign.JUSTIFY
                                    )
                                ),
                                Container(height = 0.5, width = 350, bgcolor = colors.WHITE),
                            ]),
                            Text(f"Processor {self.data.processor_name}"),
                            Text(f"GPU {self.data.gpu_name}"),
                            Text(f"RAM {self.data.ram} GB {self.data.ram_type}"),
                            Text(f"Storage {self.data.storage} GB"),
                            Text(f"Screen Size {self.data.screen_size} Inch"),
                            Text(f"Screen Resolution {self.data.screen_resolution}p"),
                            Text(f"Refresh Rate {self.data.refresh_rate} hz"),
                            Text(f"Weight : {self.data.weight} Kg"),
                            Text("Rp. " + "{:,.0f}".format(self.data.price).replace(",", ".") + ",-")
                        ]
                    )
                ]
            )
        )
    )

    def open_dlg(self, e):
        print(self.data.index)
        self.page.dialog = self.dlg
        self.dlg.open = True
        self.page.update()

    def build(self):
        return self.dlg
