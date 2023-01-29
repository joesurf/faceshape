from typing import Any, Dict
import numpy as np
from peekingduck.pipeline.nodes.abstract_node import AbstractNode


class Node(AbstractNode):
    def __init__(self, config: Dict[str, Any] = None, **kwargs: Any) -> None:
        super().__init__(config, node_path=__name__, **kwargs)
        self.frame = 0

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]: # type: ignore if "cat" in inputs["bbox_labels"]:
        print(
            f"{self.frame} {inputs['bbox_scores'][np.where(inputs['bbox_labels'] == 'cat')]}"
        )
        self.frame += 1 
        return {}