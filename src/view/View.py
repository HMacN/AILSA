from util.IdentifiedObject import IdentifiedObject
from util.publisher_subscriber import Publisher
from controller.IControllerForView import IControllerForView
from src.view.IView import IView


class View(IView):

    def __init__(self, view_listener: IControllerForView):
        self.controller: IControllerForView = view_listener
        self.publisher: Publisher = None

    def get_controller(self) -> IControllerForView:
        return self.controller

    def set_publisher(self, publisher: Publisher):
        self.publisher = publisher

    def get_publisher(self) -> Publisher:
        return self.publisher

    def detect(self, detected_object: IdentifiedObject):
        self.controller.new_detected_object(detected_object)
