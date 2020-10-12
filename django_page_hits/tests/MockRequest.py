class MockUser:
    """
    A class to act as a mock user.
    """

    def __init__(self, authenticated):
        self.authenticated = authenticated

    @property
    def is_authenticated(self):
        return self.authenticated


class MockRequest:
    """
    A mock request for homepage.
    """

    def __init__(self, url, authenticated):
        self.user = MockUser(authenticated)
        self.path = url
