"""
Node template for creating custom nodes.
"""

from typing import Any, Dict, List, Tuple

import cv2
import numpy as np
from PIL import Image
import csv
from peekingduck.pipeline.nodes.abstract_node import AbstractNode

#IMG_WIDTH = 180
#IMG_HEIGHT = 180
YELLOW = (0, 255, 255)  

def map_bbox_to_image_coords(
   bbox: List[float], image_size: Tuple[int, int]) -> List[int]:
   """This is a helper function to map bounding box coords (relative) to
   image coords (absolute).
   Bounding box coords ranges from 0 to 1
   where (0, 0) = image top-left, (1, 1) = image bottom-right.
   
   Args:
      bbox (List[float]): List of 4 floats x1, y1, x2, y2
      image_size (Tuple[int, int]): Width, Height of image

   Returns:
      List[int]: x1, y1, x2, y2 in integer image coords
   """
   width, height = image_size[0], image_size[1]
   x1, y1, x2, y2 = bbox
   x1 *= width
   x2 *= width
   y1 *= height
   y2 *= height
   return int(x1), int(y1), int(x2), int(y2)

class Node(AbstractNode):
    """This is a template class of how to write a node for PeekingDuck.

    Args:
        config (:obj:`Dict[str, Any]` | :obj:`None`): Node configuration.
    """

    def __init__(self, config: Dict[str, Any] = None, **kwargs: Any) -> None:
        super().__init__(config, node_path=__name__, **kwargs)

        # initialize/load any configs and models here
        # configs can be called by self.<config_name> e.g. self.filepath
        # self.logger.info(f"model loaded with configs: config")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:  # type: ignore
        """This node does ___.

        Args:
            inputs (dict): Dictionary with keys "__", "__".

        Returns:
            outputs (dict): Dictionary with keys "__".
        """
        
        img = inputs["img"]
        bboxes = inputs["bboxes"]
        filename = inputs["filename"]
        # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
        # print(filename)
        # print('#################################333')
        img_size = (img.shape[1], img.shape[0]) #width. height
        # header = ['filename', 'top', 'left', 'bottom', 'right']
        # temp_list = []
        # with open('test2.csv', 'w', encoding='UTF8', newline = '') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(header)
        for i, bbox in enumerate(bboxes):
            # for each bounding box:
            #   - compute (x1, y1) top-left, (x2, y2) bottom-right coordinates
            x1, y1, x2, y2 = map_bbox_to_image_coords(bbox, img_size)
            #     temp = [filename, x1, y1, x2, y2]
            #     temp_list.append(temp)
            # writer.writerow(temp_list)
                
            
            #test_image = Image(img)
            #test_image.crop(y1, x1, y2, x2)
            #outputs = {"img", test_image}
        
        return {
            'top' : y1,
            'left' : x1,
            'right': x2,
            'bottom': y2
        }
        # result = do_something(inputs["in1"], inputs["in2"])
        # outputs = {"out1": result}
        #return outputs
