from classes.enums import getEnumByName, Token


class BoardState:
    def __init__(self, board_dict):
        self.board_dict = board_dict

    def update(self):

        # First remove empty
        for i in self.board_dict.copy():
            # use copy to avoid "dictionary changed size during iteration"
            if len(self.board_dict[i]) == 0:
                del self.board_dict[i]

        # Check each hex, if they battle
        for i in self.board_dict.copy():

            if len(self.board_dict[i]) > 1:
                # Start battle
                pieces = set()
                for piece in self.board_dict[i]:
                    pieces.add(piece[1])

                if len(pieces) == 3:
                    del self.board_dict[i]
                elif len(pieces) == 2:
                    pieces = list(pieces)
                    if getEnumByName(pieces[0], Token).battle(getEnumByName(pieces[1], Token)):
                        for token in self.board_dict[i].copy():
                            if token == pieces[1]:
                                self.board_dict[i].remove(token)
                    else:
                        for token in self.board_dict[i].copy():
                            if token == pieces[0]:
                                self.board_dict[i].remove(token)
