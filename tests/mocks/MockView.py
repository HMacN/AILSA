from controller import IControllerForView
from util import IdentifiedObject
from util.publisher_subscriber import Publisher
from src.view.IView import IView


class MockView(IView):
    def __init__(self, view_listener: IControllerForView):
        pass

    def detect(self, identified_objects: list):
        pass

    def set_publisher(self, publisher: Publisher):
        pass

    def get_publisher(self) -> Publisher:
        pass

    def get_controller(self) -> IControllerForView:
        pass
