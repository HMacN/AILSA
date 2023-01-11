class IdentifiedObject:
    horizontal_distance_to_origin: int = None
    vertical_distance_to_origin: int = None
    bounding_box_width: int = None
    bounding_box_height: int = None
    object_name: str = None

    def __init__(self,
                 horizontal_distance_to_origin: int,
                 vertical_distance_to_origin: int,
                 bounding_box_width: int,
                 bounding_box_height: int,
                 object_name: str):
        self.horizontal_distance_to_origin = horizontal_distance_to_origin
        self.vertical_distance_to_origin = vertical_distance_to_origin
        self.bounding_box_width = bounding_box_width
        self.bounding_box_height = bounding_box_height
        self.object_name = object_name

    def get_horizontal_distance_to_origin(self):
        return self.horizontal_distance_to_origin

    def get_vertical_distance_to_origin(self):
        return self.vertical_distance_to_origin

    def get_bounding_box_width(self):
        return self.bounding_box_width

    def get_bounding_box_height(self):
        return self.bounding_box_height

    def get_object_name(self):
        return self.object_name
