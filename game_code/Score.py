from game_code.DBProxy import DBProxy


class Score:
    def __init__(self):
        pass

    @staticmethod
    def save(score, score_round):
        db_proxy = DBProxy('DBScore')
        db_proxy.save({'score': score, 'score_round': score_round})

    @staticmethod
    def show_round():
        db_proxy = DBProxy('DBScore')
        score_round = db_proxy.show_round()
        db_proxy.close()
        return score_round

    @staticmethod
    def show():
        db_proxy = DBProxy('DBScore')
        score = db_proxy.show()
        db_proxy.close()
        return score