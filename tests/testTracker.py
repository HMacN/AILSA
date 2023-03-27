import unittest

from model.Tracker import Tracker
from util.BoundingBoxCollection import BoundingBoxCollection
from util.Box import Box


class ModelTests(unittest.TestCase):

    def test_track_new_items(self):
        tracker = Tracker()

        box_collection = BoundingBoxCollection()
        box_0 = Box(0.2, 0.3, 0.2, 0.6, 0.5, "test1")
        box_1 = Box(0.1, 0.4, 0.1, 0.6, 0.5, "test2")
        box_2 = Box(0.0, 0.3, 0.2, 0.3, 0.7, "test3")

        box_collection.add(box_0)
        box_collection.add(box_1)
        box_collection.add(box_2)

        tracker.detect(box_collection)

        current_tracks = tracker.get_current_tracks()

        self.assertEqual(box_collection, current_tracks)

    def test_track_existing_items(self):
        tracker = Tracker()

        box_collection = BoundingBoxCollection()
        box_0 = Box(0.2, 0.3, 0.2, 0.6, 0.5, "test1")
        box_1 = Box(0.1, 0.4, 0.1, 0.6, 0.5, "test2")
        box_2 = Box(0.0, 0.3, 0.2, 0.3, 0.7, "test3")

        box_collection.add(box_0)
        box_collection.add(box_1)
        box_collection.add(box_2)

        tracker.detect(box_collection)

        current_tracks = tracker.get_current_tracks()

        self.assertEqual(box_collection, current_tracks)
