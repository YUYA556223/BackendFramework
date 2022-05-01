from api.auth.account_info import AccountInfo


class Certificate:
    __uinfo: AccountInfo
    __isvalid = False

    def __init__(self, uinfo: AccountInfo) -> None:
        self.__uinfo = uinfo
        self.__isvalid = uinfo is not None
        pass

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Certificate):
            return self.__uinfo.user.localId == o.__uinfo.user.localId
        return False

    @property
    def uid(self):
        return self.__uinfo.user.localId

    @property
    def user_info(self):
        return self.__uinfo

    @property
    def is_valid_user(self):
        return self.__isvalid
