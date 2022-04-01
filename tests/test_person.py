from logging.handlers import WatchedFileHandler
import pytest
from viewing_party.person import Person

def test_person():
    # Arrange
    name = "Ada"
    watched = ["Euphoria"]
    friends = []
    subscriptions = ["hulu", "HBO max"]

    # Act
    ada = Person(name, watched, friends, subscriptions)

    # Assert
    assert ada.name == name
    assert len(ada.watched) == 1
    assert ada.watched == ["Euphoria"]
    assert "Euphoria" in ada.watched
    assert len(ada.friends) == 0
    assert len(ada.subscriptions) == 2
    assert ada.subscriptions[0] == "hulu"
    assert ada.subscriptions[1] == "HBO max"