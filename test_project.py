from project import is_valid, is_top, is_bottom

def test_is_valid():
    assert is_valid("Arsenal") == True
    assert is_valid("Barcelona") == False
    assert is_valid("arsenal") == False
    assert is_valid("Arsenal ") == False
    assert is_valid("Man City") == False
    assert is_valid("Manchester City") == True

def test_is_top():
    stats = [{"Team": "Arsenal", "strength": 10}, {"Team": "Aston Villa", "strength": 7}, {"Team": "Bournemouth", "strength": 5}, {"Team": "Brentford", "strength": 4}, {"Team": "Brighton", "strength": 6}, {"Team": "Chelsea", "strength": 10}, {"Team": "Crystal Palace", "strength": 5}, {"Team": "Everton", "strength": 5}, {"Team": "Fulham", "strength": 5}, {"Team": "Ipswich Town", "strength": 2}, {"Team": "Leicester City", "strength": 5}, {"Team": "Liverpool", "strength": 10}, {"Team": "Manchester City", "strength": 11}, {"Team": "Manchester United", "strength": 10}, {"Team": "Newcastle", "strength": 7}, {"Team": "Nottingham Forest", "strength": 4}, {"Team": "Southampton", "strength": 4}, {"Team": "Tottenham Hotspur", "strength": 10}, {"Team": "West Ham", "strength": 6}, {"Team": "Wolves", "strength": 5}]
    assert is_top("Arsenal", stats) == True
    assert is_top("Wolves", stats) == False

def test_is_bottom():
    stats = [{"Team": "Arsenal", "strength": 10}, {"Team": "Aston Villa", "strength": 7}, {"Team": "Bournemouth", "strength": 5}, {"Team": "Brentford", "strength": 4}, {"Team": "Brighton", "strength": 6}, {"Team": "Chelsea", "strength": 10}, {"Team": "Crystal Palace", "strength": 5}, {"Team": "Everton", "strength": 5}, {"Team": "Fulham", "strength": 5}, {"Team": "Ipswich Town", "strength": 2}, {"Team": "Leicester City", "strength": 5}, {"Team": "Liverpool", "strength": 10}, {"Team": "Manchester City", "strength": 11}, {"Team": "Manchester United", "strength": 10}, {"Team": "Newcastle", "strength": 7}, {"Team": "Nottingham Forest", "strength": 4}, {"Team": "Southampton", "strength": 4}, {"Team": "Tottenham Hotspur", "strength": 10}, {"Team": "West Ham", "strength": 6}, {"Team": "Wolves", "strength": 5}]
    assert is_bottom("Tottenham Hotspur", stats) == True
    assert is_bottom("West Ham", stats) == True
    assert is_bottom("Wolves", stats) == True
    assert is_bottom("Southampton", stats) == False
    assert is_bottom("Bournemouth", stats) == False
