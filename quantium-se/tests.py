from app import dash_app

def test_header(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_graph(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#salesGraph", timeout=10)


def test_regionpicker(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region", timeout=10)