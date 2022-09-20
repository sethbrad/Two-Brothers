class Spell:
    pass


def fireball(player, enemy):
    enemy.hp -= player.attributes["mp"]
