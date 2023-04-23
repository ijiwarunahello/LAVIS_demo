import torch
from lavis.models import load_model_and_preprocess
from PIL import Image

from common import (
    show_result,
)

import argparse


def blip_captioning(raw_image):
    # setup device to use
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # load BLIP VQA model finetuned on VQAv2
    model, vis_processors, _ = load_model_and_preprocess(
        name="blip_caption", model_type="base_coco", is_eval=True, device=device
    )

    # preprocess the image
    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)

    # キャプション生成
    caption = model.generate({"image": image})

    show_result(raw_image, caption)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", help="Target image", type=str)

    args = parser.parse_args()
    image_path = args.image_path

    raw_image = Image.open(image_path).convert("RGB")

    blip_captioning(raw_image)
