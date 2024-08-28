from django.db import models


class Player(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return f'Player {self.username}'


class Game(models.Model):
    STATUS_CHOICES = [
        ('ONGOING', 'Ongoing'),
        ('DRAW', 'Draw'),
        ('WHITE_WON', 'White Won'),
        ('BLACK_WON', 'Black Won')
    ]

    player_white = models.ForeignKey(Player, related_name='white_games', on_delete=models.CASCADE)
    player_black = models.ForeignKey(Player, related_name='black_games', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    fen = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_move_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Game between {self.player_white} (White) and {self.player_black} (Black)'
