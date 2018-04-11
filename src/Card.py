class Card:
    class Rank:
        Nine = "9"
        Ten = "10"
        Jack = "J"
        Queen = "Q"
        King = "K"
        Ace = "A"
        NineTrump = "9T"
        TenTrump = "10T"
        QueenTrump = "QT"
        KingTrump = "KT"
        AceTrump = "AT"
        LeftBower = "LB"
        RightBower = "RB"

        Enum = [Nine, Ten, Jack, Queen, King, Ace, NineTrump, TenTrump, QueenTrump, KingTrump, AceTrump, LeftBower,
                RightBower]
        Value = {Nine: 1, Ten: 2, Jack: 3, Queen: 4, King: 5, Ace: 10, NineTrump: 12, TenTrump: 15, QueenTrump: 20,
                 KingTrump: 25, AceTrump: 30, LeftBower: 31, RightBower: 35}

    class Suit:
        Club = "♣"
        Diamond = "♦"
        Heart = "♥"
        Spade = "♠"
        Color = {Club: "Black", Spade: "Black", Diamond: "Red", Heart: "Red"}
        Enum = [Club, Diamond, Heart, Spade]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return Card.Rank.Value[self.rank] < Card.Rank.Value[other.rank]
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return Card.Rank.Value[self.rank] <= Card.Rank.Value[other.rank]
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rank == other.rank and self.suit == other.suit
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @staticmethod
    def get_card_value(current_card, trump_suit):
        current_card_color = Card.Suit.Color[current_card.suit]
        trump_color = Card.Suit.Color[trump_suit]
        your_card_suit = current_card.suit

        if current_card_color == trump_color:
            if your_card_suit == trump_suit:
                cur_rank = current_card.rank
                if cur_rank != "J":
                    return Card.Rank.Value[str(current_card.rank + "T")]
                else:
                    return Card.Rank.Value["RB"]
            elif current_card.rank == "J":
                return Card.Rank.Value["LB"]
        return Card.Rank.Value[current_card.rank]


Card.TenOfSpades = Card(Card.Rank.Ten, Card.Suit.Spade)

if __name__ == "__main__":
    test = Card(Card.Rank.Jack, Card.Suit.Spade)
    cur_suit = Card.Suit.Spade
    print(Card.get_card_value(test, cur_suit))
