import packaging_publishing_demo as demo


def test_greet():
    assert demo.greet("CI").startswith("Hello, CI!")


def test_version_is_set():
    # "0.1.devN+g<hash>" on ordinary CI runs, exactly "X.Y.Z" on a tag
    assert demo.__version__


def test_farewell():
    assert demo.farewell("CI").startswith("Goodbye, CI!")
