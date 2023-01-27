import unittest

from mocks.MockController import MockController
from model.DetectedObjectRegister import DetectedObjectRegister
from model.Model import Model
from util.IdentifiedObject import IdentifiedObject


class ModelTests(unittest.TestCase):

    def test_get_set_controller(self):
        controller = MockController()
        model = Model(controller)

        self.assertEqual(controller, model.get_controller())

    def test_register_new_detected_objects_and_gets_all_detected_objects(self):
        controller = MockController()
        model = Model(controller)
        item_1 = IdentifiedObject(1, 1, 2, 2, "test")
        item_2 = IdentifiedObject(5, 5, 2, 2, "test")
        item_3 = IdentifiedObject(9, 9, 2, 2, "test")
        items = [item_1, item_2, item_3]

        model.detect(items)
        returned_items = model.get_detected_items()

        self.assertEqual(items, returned_items)
