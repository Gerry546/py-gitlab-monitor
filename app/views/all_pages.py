from nicegui import ui


def create() -> None:
    ui.page("/test1")
    ui.page("/test2")


if __name__ == "__main__":
    create()
