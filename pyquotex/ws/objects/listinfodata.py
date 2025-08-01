"""Module for Quotex Candles websocket object."""

from pyquotex.ws.objects.base import Base


class ListInfoData(Base):
    """Class for Quotex Candles websocket object."""

    def __init__(self):
        super(ListInfoData, self).__init__()
        self.__name = "listInfoData"
        self.listinfodata_dict = {}

    def set(self, game_state, percent_profit, id_number):
        self.listinfodata_dict[id_number] = {
            "game_state": game_state,
            "percent_profit": percent_profit
        }

    def delete(self, id_number):
        del self.listinfodata_dict[id_number]

    def get(self, id_number):
        return self.listinfodata_dict.get(id_number)
