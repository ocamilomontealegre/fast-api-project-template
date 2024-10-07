from os import path
from subprocess import CalledProcessError, check_call, run


def get_poetry_python_path() -> str:
    """Get the Python executable path from the Poetry virtual environment."""
    result = run(
        ["poetry", "env", "info", "--path"], capture_output=True, text=True, check=True
    )
    poetry_env_path = result.stdout.strip()

    return path.join(poetry_env_path, "Scripts", "python.exe")


def start() -> None:
    """Start uvicorn server."""
    try:
        python_path = get_poetry_python_path()
        print(python_path)
        check_call([python_path, "src/main.py"])
    except KeyboardInterrupt:
        print("\nServer stopped manually.")
        exit(0)
    except CalledProcessError as e:
        print(f"Server start failed: {e}")
        exit(1)


def lint() -> None:
    """Run flake8 linter on the src directory"""
    try:
        check_call(["flake8", "src/"])
    except Exception as e:
        print(f"Linting failed: {e}")


def format() -> None:
    """Format using black"""
    try:
        check_call(["black", "src/"])
    except Exception as e:
        print(f"Formatting failed: {e}")
