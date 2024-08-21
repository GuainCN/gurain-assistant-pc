import os
import shutil


def get_rust_target(dir_path: str) -> list:
    target_list = []

    if not os.path.isdir(dir_path):
        return target_list

    dir_path = os.path.abspath(dir_path)

    cargo_toml = os.path.join(dir_path, "Cargo.toml")
    if os.path.exists(cargo_toml):
        target_path = os.path.join(dir_path, "target")
        if os.path.exists(target_path) and os.path.isdir(target_path):
            target_list.append(target_path)

    for sub_dir in os.listdir(dir_path):
        target_list.extend(
            get_rust_target(
                os.path.join(dir_path, sub_dir)
            )
        )

    return target_list


def rm_dir_list(dir_path_list: list):
    for dir_path in dir_path_list:
        try:
            shutil.rmtree(dir_path)
            print(f"Deleted directory: {dir_path}")
        except FileNotFoundError:
            print(f"Directory not found: {dir_path}")


if __name__ == "__main__":
    dir_list = [
        "./node_modules",
    ]

    dir_list.extend(get_rust_target("./src-tauri"))

    rm_dir_list(dir_list)
