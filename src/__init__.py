from typing import Callable

from aqt import AnkiQt, mw
from aqt.qt import QAction
from aqt.utils import showInfo


class MainWindowUninitializedError(Exception):
    """
    Exception that represents error when imported main window is actually None.

    Should not be actually thrown; mostly exists to appease MyPy.
    """

    def __init__(self) -> None:
        super().__init__("Anki main window is uninitialized")


def card_count(mw: AnkiQt) -> Callable[[], None]:
    """
    Get total card count for collection and show it.

    :param mw: Main window object.
    """

    def _callback() -> None:
        count: int = mw.col.card_count()
        showInfo(f"Card count: {count}")

    return _callback


if mw is None:
    raise MainWindowUninitializedError
action = QAction("Show total card count", mw)
action.triggered.connect(card_count(mw))
mw.form.menuTools.addAction(action)
