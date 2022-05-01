from typing import Any


class AccountInfo:
    """ Account information of Google Firebase-auth.
    """
    class UserInfo:
        def __init__(self, rawdata: Any) -> None:
            self.localId = rawdata["localId"]
            self.email = rawdata["email"]
            self.displayName = rawdata["displayName"]
            self.photoUrl = rawdata["photoUrl"]
            self.emailVerified = rawdata["emailVerified"]
            self.validSince = rawdata["validSince"]
            self.lastLoginAt = rawdata["lastLoginAt"]
            self.createdAt = rawdata["createdAt"]
            self.lastRefreshAt = rawdata["lastRefreshAt"]
            pass
        localId: str
        email: str
        displayName: str
        photoUrl: str
        emailVerified: bool
        validSince: str
        lastLoginAt: str
        createdAt: str
        lastRefreshAt: str
    kind: str
    user: UserInfo

    def __init__(self, rawdata: Any) -> None:
        self.kind = rawdata["kind"]
        self.user = AccountInfo.UserInfo(rawdata["users"][0])
        pass
