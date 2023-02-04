from pathlib import Path
from peekingduck.pipeline.nodes.dabble import fps
from peekingduck.pipeline.nodes.draw import bbox, legend
from peekingduck.pipeline.nodes.input import visual
from peekingduck.pipeline.nodes.model import yolo
from peekingduck.pipeline.nodes.output import csv_writer, screen 
from peekingduck.runner import Runner
from src.custom_run.dabble import debug
from src.custom_nodes.model import casting_classifier
from getImageS3 import image_from_s3
from readCsv import getResult
from checkImageData import checkImageIntegrity
import asyncio
import time
import cv2
from PIL import Image


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.post("/infer/{file}")
async def infer(file):
    print(file)
    prediction = await run(file)
    return {"prediction": prediction}


async def pipeline(file):
    image = Image.open(file)
    image.save("random.jpg")


    try:
        checkImageIntegrity("./", "random.jpg")
    except Exception as e:
        print("Image corrupted")

    debug_node = debug.Node(pkd_base_dir=Path.cwd() / "src" / "custom_run")
    visual_node = visual.Node(source='random.jpg') 

    # visual_node = visual.Node(source=str(Path.cwd() / "heart.jpg")) 
    screen_node = screen.Node()
    csv_writer_node = csv_writer.Node(   
        stats_to_track=["filename", "pred_label", "pred_score"],
        file_path="casting_predictions.csv",
        logging_interval=0
    )

    custom_node = casting_classifier.Node(pkd_base_dir=Path.cwd() / "src" / "custom_nodes")

    runner = Runner(
        nodes=[
            visual_node,
            custom_node,
            screen_node,
            csv_writer_node,
            # visual_node,
            # yolo_node,
            # debug_node,
            # bbox_node,
            # fps_node,
            # legend_node,
            # screen_node,
            # media_writer_node,
    ] )
    runner.run()


async def run(file):
    await pipeline(file)
    # time.sleep()

    prediction = ""

    # Read lastest casting predictions csv file
    result = getResult()
    if result:
        prediction = result[2]

    print(prediction)
    return prediction


# if __name__ == "__main__": asyncio.run(main())