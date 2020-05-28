from argparse import ArgumentParser

class ParserKey():
    def __init__(self):
        parser = ArgumentParser(description="Obtain the Claps prediction of your Medium article.")
        parser.add_argument("--url", help="Url of the article", type=str, default=None)
        parser.add_argument("--days", help="Number of days your article has been published", type=int, default=0)
        parser.add_argument("--temp", help="Days range in which you want to make the prediction", type=int, default=15)
        parser.add_argument("--publication", help="Introduce the publication you will use for your article", type=str, default=None)
        self.args = parser.parse_args()