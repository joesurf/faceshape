"""
Node template for creating custom nodes.
"""

from typing import Any, Dict

import cv2
import numpy as np
import tensorflow as tf

from peekingduck.pipeline.nodes.abstract_node import AbstractNode

IMG_WIDTH = 180
IMG_HEIGHT = 180

class Node(AbstractNode):
    """This is a template class of how to write a node for PeekingDuck.

    Args:
        config (:obj:`Dict[str, Any]` | :obj:`None`): Node configuration.
    """

    def __init__(self, config: Dict[str, Any] = None, **kwargs: Any) -> None:
        super().__init__(config, node_path=__name__, **kwargs)
        self.model = tf.keras.models.load_model(self.weights_parent_dir)
        # initialize/load any configs and models here
        # configs can be called by self.<config_name> e.g. self.filepath
        # self.logger.info(f"model loaded with configs: config")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:  # type: ignore
        """This node does Reads the image input and returns the predicted class label and confidence score.

        Args:
            inputs (dict): Dictionary with keys "bboxes".

        Returns:
            outputs (dict): Dictionary with keys "pred_label" and "pred_Score".
        """
        #Regular pre-processing of images
        img = cv2.cvtColor(inputs["bboxes"], cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
        img = np.expand_dims(img, axis=0)
        
        predictions = self.model.predict(img)
        score = tf.nn.softmax(predictions[0])
        
        return {
            "pred_label": self.class_label_map[np.argmax(score)],
            "pred_score": 100.0 * np.max(score),
        }
        
        # result = do_something(inputs["in1"], inputs["in2"])
        # outputs = {"out1": result}
        # return outputs
