from fastapi import UploadFile
import uuid
from PIL import Image
import torch
import numpy as np
from ultralytics import YOLO


class Analyser:

    def __init__(self, model):
        self.model = YOLO(model)

    async def recieve_image(self, image: UploadFile):
        filename = str(uuid.uuid4())
        f = open(f"imgs/{filename}.jpg", "wb")
        f.write(image.file.read())
        return f"imgs/{filename}.jpg"

    async def analyse_image(self, path: str):
        img = Image.open(path).convert("RGB")
        img = img.resize((640, 640))
        img_tensor = torch.tensor(
            np.array(img) / 255.0).permute(2, 0, 1).unsqueeze(0)

        res = self.model(img_tensor)

        pred_probs = res[0].probs
        if pred_probs is not None:
            top1_idx = pred_probs.top1
            top1_conf = pred_probs.top1conf
            class_name = res[0].names[top1_idx]

            return {
                'class': int(class_name),
                'confidence': float(top1_conf)
            }
        else:
            return {'error': 'No predictions'}
