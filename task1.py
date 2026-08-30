class ShoeModel:
    def __init__(self, gender, shoe_type, color, price, manufacturer, size):
        self.gender = gender
        self.shoe_type = shoe_type
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

class ShoeView:
    def show_shoe(self, shoe):
        print(f"тип: {shoe.gender}")
        print(f"вид: {shoe.shoe_type}")
        print(f"цвет: {shoe.color}")
        print(f"цена: {shoe.price}")
        print(f"производитель: {shoe.manufacturer}")
        print(f"размер: {shoe.size}")

class ShoeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_view(self):
        self.view.show_shoe(self.model)

model = ShoeModel("мужское", "кроссовки", "черный", 2500, "noskinice", 43)
view = ShoeView()
controller = ShoeController(model, view)
controller.update_view()