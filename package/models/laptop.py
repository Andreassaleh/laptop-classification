class Laptop:
    def __init__(self, data):
        self.index = data["index"]
        self.link = data["link"]
        self.name = data["name"]
        self.user_rating = data["user_rating"]
        self.price = data["price"]
        self.type = data["type"]
        self.graphic_memory_capacity = data["graphic_memory_capacity"]
        self.processor_brand = data["processor_brand"]
        self.ssd = data["ssd"]
        self.ram = data["ram"]
        self.ram_type = data["ram_type"]
        self.expandable_memory = data["expandable_memory"]
        self.operating_system = data["operating_system"]
        self.touchscreen = data["touchscreen"]
        self.screen_size = data["screen_size"]
        self.weight = data["weight"]
        self.refresh_rate = data["refresh_rate"]
        self.screen_resolution = data["screen_resolution"]
        self.company = data["company"]
        self.storage = data["storage"]
        self.processor_name = data["processor_name"]
        self.cpu_ranking = data["cpu_ranking"]
        self.battery_backup = data["battery_backup"]
        self.gpu_name = data["gpu_name"]
        self.gpu_benchmark = data["gpu_benchmark"]
        self.ram_type_tokenized = data["ram_type_tokenized"]
        self.gpu_processor_tokenized = data["gpu_processor tokenized"]