from src.Model.Enemy.Enemy import EnemyStyle
from src.Model.UserHero import CharacterStatus
from src.Model.Enemy.AggressiveEnemy import AggressiveEnemy
from src.Model.Map.Map import GridCell
from src.Model.Enemy.NeutralEnemy import NeutralEnemy
from src.Model.Enemy.Mold import Mold

def test_Enemy1():
    enemy = AggressiveEnemy(10, 5, EnemyStyle.FANTASY)

    assert enemy.status == CharacterStatus.ALIVE
    assert enemy.attack == 5
    assert enemy.health == 10

    enemy.defence(10)
    assert enemy.health == 0
    assert enemy.status == CharacterStatus.DEAD
    assert enemy.get_type() == GridCell.AGGRESSIVE_ENEMY

def test_Enemy2():
    enemy = NeutralEnemy(10, 5, EnemyStyle.FANTASY)

    assert enemy.status == CharacterStatus.ALIVE
    assert enemy.attack == 5
    assert enemy.health == 10

    enemy.defence(10)
    assert enemy.health == 0
    assert enemy.status == CharacterStatus.DEAD
    assert enemy.get_type() == GridCell.NEUTRAL_ENEMY

def test_Mold1():
    enemy = Mold(10, 5, EnemyStyle.FANTASY, 0.01)

    assert enemy.status == CharacterStatus.ALIVE
    assert enemy.attack == 5
    assert enemy.health == 10

    cop = enemy.clone()

    enemy.defence(10)
    assert enemy.health == 0
    assert enemy.status == CharacterStatus.DEAD
    assert enemy.get_type() == GridCell.MOLD
    assert cop.health == 10
    assert cop.status == CharacterStatus.ALIVE
