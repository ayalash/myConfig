#!/usr/bin/env python3

"""
This script sets the configuration files for fast setup.
The script should depend on buildin modules only, so no venv will be needed.
"""

import os
import platform
import sys
import argparse
from typing import NamedTuple
from pathlib import Path

class ConfigurationInfo(NamedTuple):
    config_path: str
    link_path: str
    should_ensure_dir: bool = False
    create_by_default: bool = True


_OS_TYPE_NAME = platform.system().lower()
_SCRIPT_DIR = os.path.dirname(__file__)

_CONFIGURATION_INFO_LIST = [
    ConfigurationInfo(f"{_SCRIPT_DIR}/gitCfg/gitconfig", "~/.gitconfig"),
    ConfigurationInfo(f"{_SCRIPT_DIR}/gitCfg/gitignore", "~/.gitignore"),
    ConfigurationInfo(f"{_SCRIPT_DIR}/topgrade.toml", "~/.config/topgrade.toml", should_ensure_dir=True),
    ConfigurationInfo(f"{_SCRIPT_DIR}/bat.conf", "~/.config/bat/config", should_ensure_dir=True),
    ConfigurationInfo(f"{_SCRIPT_DIR}/karabiner.json", "~/.config/karabiner/karabiner.json", should_ensure_dir=True),
    ConfigurationInfo(f"{_SCRIPT_DIR}/zsh/zshrc", "~/.zshrc"),
    ConfigurationInfo(f"{_SCRIPT_DIR}/zsh/{_OS_TYPE_NAME}-zshrc", f"~/.{_OS_TYPE_NAME}-zshrc"),
    ConfigurationInfo(f"{_SCRIPT_DIR}/tmux/tmux.conf", "~/.tmux.conf"),
    ConfigurationInfo(f"{_SCRIPT_DIR}/vim/vimrc", "~/.vimrc"),
    ConfigurationInfo(f"{_SCRIPT_DIR}/vim/vim", "~/.vim"),
    ConfigurationInfo(f"{_SCRIPT_DIR}/pylintrc", "~/.pylintrc", create_by_default=False),
    ConfigurationInfo(f"{_SCRIPT_DIR}/screenrc", "~/.screenrc", create_by_default=False),
]

def convert_to_path(path_str: str, /) -> Path:
    return Path(path_str).expanduser().absolute()


def show_error(err_msg: str):
    print(f"\tERROR: {err_msg}\n")

class ScriptError(Exception):
    pass

def raise_error(err_msg: str):
    raise ScriptError(err_msg)


def main():
    parser = argparse.ArgumentParser(description="Set my configuration files")
    parser.add_argument("--all", action="store_true", dest="create_all", default=False)
    parser.add_argument("-n", "--dry-run", action="store_true", dest="dry_run", default=False)
    args = parser.parse_args()


    if _OS_TYPE_NAME not in ("darwin", "link"):
        raise ScriptError(f"OS {_OS_TYPE_NAME.title()} is not supported")
    handle_err = show_error if args.dry_run else raise_error

    for cfg_info in _CONFIGURATION_INFO_LIST:
        config_path = convert_to_path(cfg_info.config_path)
        link_path = convert_to_path(cfg_info.link_path)

        if (not cfg_info.create_by_default) and (not args.create_all):
            # Should skip this link because it should be created only when '--all' flag is passed
            continue

        print(f"Creating link (ensure-dir: {cfg_info.should_ensure_dir}): {link_path} -> {config_path}")
        if not os.path.exists(config_path):
            handle_err(f"{config_path} does not exist")

        if link_path.exists():
            if not link_path.is_symlink():
                handle_err("Cannot create symlink, Regular file exists")
            else:
                curr_linked_path = os.readlink(link_path)
                if curr_linked_path != config_path:
                    handle_err(f"link exists, but not as expected ({curr_linked_path} != {config_path}")
                else:
                    print("\tLink already exists. skipping...")
        else:
            if not args.dry_run:
                print("Creating symlink!!!!!!!")
                if cfg_info.should_ensure_dir:
                    dir_path = os.path.dirname(link_path)
                    print(f"\tEnsuring directory path: {dir_path}")
                    os.makedirs(dir_path, exist_ok=True)
                os.symlink(config_path, link_path)


if __name__ == '__main__':
    try:
        sys.exit(main())
    except ScriptError as e:
        show_error(str(e))
        sys.exit(1)
