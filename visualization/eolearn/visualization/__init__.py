"""
A collection of visualization utilities
"""

from .eoworkflow_visualization import EOWorkflowVisualization
from .eoexecutor_visualization import EOExecutorVisualization

try:
    from .eopatch_visualization import EOPatchVisualization
except ImportError:
    pass

__version__ = '1.0.0'
