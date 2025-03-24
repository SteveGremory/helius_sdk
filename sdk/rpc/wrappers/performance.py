from typing import Dict
from .base import HeliusAPIBase


class PerformanceAPI(HeliusAPIBase):
    """Performance monitoring methods"""

    def get_recent_performance_samples(self, limit: int = None) -> Dict:
        """
        Returns a list of recent performance samples, in reverse slot order.

        Args:
            limit (int, optional): Number of samples to return (maximum 720)

        Returns:
            Dict: Recent performance samples
        """
        params = []

        if limit is not None:
            params.append(limit)

        return self._make_request(
            "getRecentPerformanceSamples", params if params else None
        )
