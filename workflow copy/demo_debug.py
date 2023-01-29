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
import asyncio
import time


async def pipeline():
    image = image_from_s3("peekingduck", "heart.jpg")
    image.save("heart.jpg")

    debug_node = debug.Node(pkd_base_dir=Path.cwd() / "src" / "custom_run")
    # visual_node = visual.Node(source=image) 

    visual_node = visual.Node(source=str(Path.cwd() / "heart.jpg")) 
    yolo_node = yolo.Node(detect=["cup", "cat", "laptop", "keyboard", "mouse"]) 
    bbox_node = bbox.Node(show_labels=True)
    fps_node = fps.Node()
    legend_node = legend.Node(show=["fps"])
    screen_node = screen.Node()

    # output_location = "https://peekingduck.s3.amazonaws.com/results/"
    # media_writer_node = media_writer.Node(output_dir=output_location)

    #media_writer_node = media_writer.Node(output_dir=str(Path.cwd() / "results"))
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


async def main():
    await pipeline()
    # time.sleep()

    prediction = ""

    # Read lastest casting predictions csv file
    result = getResult()
    if result:
        prediction = result[2]
    return prediction


if __name__ == "__main__": asyncio.run(main())