from abc import ABC, abstractmethod
from typing import Dict, Any, List
from tracking.tracklet import Tracklet
from tracking.tracking_config import TrackingConfig


class TrackletTracker(ABC):
    """
    Interface for tracklet tracking implementations.
    """

    @abstractmethod
    def build_tracklets(
        self,
        estimation_results: Dict[str, Dict[str, Any]],
        config: TrackingConfig
    ) -> List[Tracklet]:
        raise NotImplementedError
