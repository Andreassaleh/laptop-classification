from flet import *
from package.components.detail_item import DetailItem
from package.models.laptop import Laptop


class ItemCard(UserControl):
    def __init__(self, page: Page, item: Laptop, image: str, key: str):
        super().__init__(key=key)
        self.key = key
        self.item = item
        self.image = image
        self.detail_item = DetailItem(page, item, self.image)

    def detail_check(self, event):
        self.detail_item.open_dlg(event)

    def build(self):
        return GestureDetector(
            content = Container(
                width = 250,
                height = 300,
                bgcolor = colors.SURFACE_VARIANT,
                border_radius = border_radius.all(10),
                content = Column(
                    alignment = MainAxisAlignment.CENTER,
                    horizontal_alignment = CrossAxisAlignment.CENTER,
                    controls = [
                        Image(
                            width=250,
                            height=200,
                            src = self.image,
                            fit=ImageFit.FILL,
                            border_radius = border_radius.all(10)
                        ),
                        Container(
                            width=180,
                            content=Text(
                                self.item.name.capitalize(),
                                weight=FontWeight.BOLD,
                                overflow=TextOverflow.ELLIPSIS
                            )
                        ),
                        Text("Rp. " + "{:,.0f}".format(self.item.price).replace(",", ".") + ",-")
                    ]
                )
            ),
            on_tap = self.detail_check
        )
