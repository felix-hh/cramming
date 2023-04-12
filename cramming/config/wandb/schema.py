from dataclasses import dataclass
from typing import Any, List


@dataclass
class WandbConfig:
    enabled: bool   # whether wandb is enabled or not
    entity: str     # wandb username
    project: str    # name of project where run will be logged
    tags: List[str] # any tags for the run

