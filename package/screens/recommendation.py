from flet import *


class Recommendation(UserControl):
    def __init__(self, page: Page, set_is_filtered):
        super().__init__()
        self.page = page
        self.set_is_filtered = set_is_filtered
        self.dd_budget = Dropdown(
            hint_text = "Pilih budget anda",
            options = [
                dropdown.Option("Kurang dari 5 juta"),
                dropdown.Option("Kisaran 5 sampai 10 juta"),
                dropdown.Option("Kisaran 10 sampai 15 juta"),
                dropdown.Option("Diatas 15 juta")
            ]
        )
        self.dd_gpu_memory = Dropdown(
            hint_text = "Pilih GPU Memory yang anda inginkan",
            options = [
                dropdown.Option(key='0', text="0 Mb"),
                dropdown.Option(key='4', text="4 Mb"),
                dropdown.Option(key='6', text="6 Mb"),
                dropdown.Option(key='8', text="8 Mb")
            ]
        )
        self.dd_processor_brand = Dropdown(
            hint_text = "Pilih processor yang anda inginkan",
            options = [
                dropdown.Option(key='1', text="Intel"),
                dropdown.Option(key='2', text="AMD"),
                dropdown.Option(key='4', text="Apple")
            ]
        )
        self.dd_ssd = Dropdown(
            hint_text = "Apakah anda ingin menggunakan SSD",
            options = [
                dropdown.Option(key='1', text="Ya"),
                dropdown.Option(key='0', text="Tidak")
            ]
        )
        self.dd_ram = Dropdown(
            hint_text = "Pilih ukuran RAM yang anda inginkan",
            options = [
                dropdown.Option(key='4', text="4 GB"),
                dropdown.Option(key='8', text="8 GB"),
                dropdown.Option(key='16', text="16 GB"),
                dropdown.Option(key='32', text="32 GB")
            ]
        )
        self.dd_expandable_memory = Dropdown(
            hint_text = "Dapat menambah memory",
            options = [
                dropdown.Option(key='1', text="Ya"),
                dropdown.Option(key='0', text="Tidak")
            ]
        )
        self.dd_screen_resolution = Dropdown(
            hint_text = "Berapa resolusi layar yang anda inginkan",
            options = [
                dropdown.Option(key='720', text="720p"),
                dropdown.Option(key='1080', text="1080p"),
                dropdown.Option(key='1440', text="1440p")
            ]
        )
        self.dd_storage = Dropdown(
            hint_text = "Pilih ukuran penyimpanan yang anda inginkan",
            options = [
                dropdown.Option(key='128', text="128 GB"),
                dropdown.Option(key='256', text="256 GB"),
                dropdown.Option(key='512', text="512 GB"),
                dropdown.Option(key='1000', text="1 TB")
            ]
        )
        self.dd_battery_backup = Dropdown(
            hint_text = "Berapa lama daya baterai",
            options = [
                dropdown.Option(key='4', text="4 Jam"),
                dropdown.Option(key='4.5', text="4 Jam Setengah"),
                dropdown.Option(key='5', text="5 Jam")
            ]
        )

    def build(self):
        return Row(
            alignment = MainAxisAlignment.CENTER,
            controls = [
                Container (
                    width = 1100,
                    border = border.all(1, colors.TERTIARY),
                    border_radius = 10,
                    padding = 20,
                    content = Column(
                        controls = [
                            Text("Budget", weight = FontWeight.BOLD), #Price (in Rupiah)
                            self.dd_budget,
                            Text("GPU Memory", weight = FontWeight.BOLD), #Dedicated Graphic Memory Capacity
                            self.dd_gpu_memory,
                            Text("Processor", weight = FontWeight.BOLD), #Processor Brand
                            self.dd_processor_brand,
                            Text("SSD", weight = FontWeight.BOLD), #SSD
                            self.dd_ssd,
                            Text("RAM", weight = FontWeight.BOLD), #RAM (in GB)
                            self.dd_ram,
                            Text("Expand Memory", weight = FontWeight.BOLD), #Expandable Memory
                            self.dd_expandable_memory,
                            Text("Resolusi Layar", weight = FontWeight.BOLD), #screen_resolution
                            self.dd_screen_resolution,
                            Text("Storage", weight = FontWeight.BOLD), #Storage
                            self.dd_storage,
                            Text("Battery", weight = FontWeight.BOLD), #RAM (in GB)
                            self.dd_battery_backup,
                            Row(
                                alignment = MainAxisAlignment.END,
                                controls = [
                                    ElevatedButton(
                                        text = "SUBMIT",
                                        on_click = lambda e: self.set_is_filtered(e, True)
                                    )
                                ]
                            )
                        ],
                        scroll = ScrollMode.AUTO
                    )
                )
            ]
        )
