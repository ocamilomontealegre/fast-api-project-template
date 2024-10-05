from subprocess import check_call, CalledProcessError


def start() -> None:
    """ Start uvicorn server """
    try:
        check_call(["python", "src/main.py"])
    except CalledProcessError as e:
        print(f"Server start failed: {e}")


def lint() -> None:
    """ Run flake8 linter on the src directory """
    try:
        check_call(["flake8", "src/"])
    except Exception as e:
        print(f"Linting failed: {e}")

# def lint() -> None:
#     """ Run flake8 linter on the src directory """
#     try:
#         check_call(["ruff", "check", "src/"])
#     except Exception as e:
#         print(f"Linting failed: {e}")

# def fix() -> None:
#     """ Fix issues using autopep8 """
#     try:
#         check_call(["ruff", "check", "--fix", "src/"])
#     except Exception as e:
#         print(f"Fixing failed: {e}")


def format() -> None:
    """ Format using black """
    try:
        check_call(["black", "src/"])
    except Exception as e:
        print(f"Formatting failed: {e}")
