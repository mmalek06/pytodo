from storage.on_disk_storage import OnDiskStorage
from ui.description_component import DescriptionComponent
from controller import Controller
from ui.list_component import ListComponent
from ui.layout_component import LayoutComponent


storage = OnDiskStorage()

storage.load_saved_data()

description_component = DescriptionComponent()
layout = LayoutComponent([
    DescriptionComponent(),
    ListComponent(storage)
])
layout_ctrl = Controller(layout, storage)

layout_ctrl.loop()
