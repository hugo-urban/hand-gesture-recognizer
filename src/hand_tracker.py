
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = '/models/gesture_recognizer.task'


base_options = BaseOptions(model_asset_path=model_path)