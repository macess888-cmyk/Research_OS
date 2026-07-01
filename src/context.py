from dataclasses import dataclass

from src.kernel import ResearchKernel
from src.config import (
    APP_NAME,
    APP_VERSION,
    APP_AUTHOR,
)


@dataclass
class ApplicationContext:
    kernel: ResearchKernel
    app_name: str = APP_NAME
    version: str = APP_VERSION
    author: str = APP_AUTHOR


context = ApplicationContext(
    kernel=ResearchKernel()
)