from flet import *
from package.components.item_card import ItemCard


class Recommend(UserControl):
    def __init__(self, set_is_filtered, page: Page, data: list):
        super().__init__()
        self.set_is_filtered = set_is_filtered
        self.page: Page = page
        self.data = data

    def items(self):
        if len(self.r.controls) == 0:
            for i in range(0, 10):
                self.r.controls.append(
                    ItemCard(
                        self.page,
                        self.data[i],
                        image=self.data[i].link,
                        key=f"LAPTOP{i}"
                    )
                )

    r = Row(wrap=True, scroll=ScrollMode.AUTO, expand=True)

    def build(self):
        self.items()
        return Column(
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Text("Hasil Rekomendasi"),
                self.r,
                Row(
                    alignment = MainAxisAlignment.END,
                    controls = [
                        ElevatedButton(
                            text = "CLEAR",
                            on_click=lambda e: self.set_is_filtered(e, False)
                        )
                    ]
                )
            ]
        )
