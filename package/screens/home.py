from flet import *
from package.components.item_card import ItemCard
from package.get_image import get_image
from package.models.laptop import Laptop
from typing import List


class Home(UserControl):
    def __init__(self, page: Page, data: List[Laptop], state):
        super().__init__()
        self.page: Page = page
        self.data = data
        self.state = state
        self.r = Row(wrap=True, scroll=ScrollMode.AUTO, expand=True)

    def item(self):
        if len(self.r.controls) == 0:
            for i in range(self.state['min'], self.state['max']):
                self.r.controls.append(
                    ItemCard(
                        self.page,
                        self.data[i],
                        image=self.data[i].link,
                        key=f"LAPTOP{i}"
                    )
                )

    def next_pagination(self, e):
        self.r.controls.clear()
        self.state['min'] += 50
        self.state['max'] += 50

    def build(self):
        self.item()
        return Column(
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Row(
                    alignment = MainAxisAlignment.END,
                    controls = [
                        TextField(
                            width = 280,
                            height = 30,
                            border = InputBorder.UNDERLINE,
                            prefix_icon = icons.SEARCH,
                            hint_text="Cari laptop ..."
                        )
                    ]
                ),
                self.r,
                Row(
                    controls = [
                        IconButton(
                            icon = icons.ARROW_BACK
                        ),
                        Text("1"),
                        IconButton(
                            icon = icons.ARROW_FORWARD,
                            on_click = self.next_pagination
                        )
                    ]
                )
            ]
        )
