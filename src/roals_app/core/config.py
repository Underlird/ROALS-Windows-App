from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from pathlib import Path
import tomllib

LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class AppConfig:
    schema_version: str
    data_root: str
    logs_dir: str
    config_path: str


def load_config() -> AppConfig:
    env_config_path = os.environ.get("ROALS_DESKTOP_CONFIG")
    if env_config_path:
        config_file = Path(env_config_path)
        if config_file.is_file():
            return _load_from_file(config_file)
        LOGGER.warning("ROALS_DESKTOP_CONFIG points to missing file: %s", config_file)

    project_config = Path.cwd() / "roals_desktop.toml"
    if project_config.is_file():
        return _load_from_file(project_config)

    return AppConfig(
        schema_version="1.0",
        data_root="",
        logs_dir="",
        config_path="(default)",
    )


def _load_from_file(config_file: Path) -> AppConfig:
    try:
        with config_file.open("rb") as fp:
            raw_config = tomllib.load(fp)
    except (OSError, tomllib.TOMLDecodeError) as err:
        LOGGER.warning("Failed to read config file %s: %s", config_file, err)
        return AppConfig(
            schema_version="1.0",
            data_root="",
            logs_dir="",
            config_path="(default)",
        )

    paths = raw_config.get("paths", {})
    schema_version = str(raw_config.get("schema_version", "1.0"))
    data_root = str(paths.get("data_root", ""))
    logs_dir = str(paths.get("logs_dir", ""))

    return AppConfig(
        schema_version=schema_version,
        data_root=data_root,
        logs_dir=logs_dir,
        config_path=str(config_file),
    )
