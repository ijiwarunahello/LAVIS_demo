import torch
from PIL import Image
from lavis.models import load_model_and_preprocess

from common import (
    show_result,
)

import argparse


def blip_vqa(raw_image, question):
    # setup device to use
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # load BLIP VQA model finetuned on VQAv2
    model, vis_processors, txt_processors = load_model_and_preprocess(
        name="blip_vqa", model_type="vqav2", is_eval=True, device=device
    )

    # use "eval" processors for inference
    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
    question = txt_processors["eval"](question)
    samples = {"image": image, "text_input": question}

    # 質疑応答
    answer = model.predict_answers(samples=samples, inference_method="generate")
    caption = f"Q: {question} -> A: {answer}"
    print(caption)

    show_result(raw_image, caption)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", help="Target image", type=str)
    parser.add_argument("question", help="question text", type=str)

    args = parser.parse_args()
    image_path = args.image_path
    question = args.question

    raw_image = Image.open(image_path).convert("RGB")

    blip_vqa(raw_image, question)
