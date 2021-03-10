def level_is_even(level):
  return level % 2 == 0

def value_coup(atk,defe,level,bonus):
  real_bonus = bonus if level_is_even(level) else 0
  return (atk + defe)/2 + real_bonus

def main(bonus, array_gabriel, array_duarte):
 
  value_gabriel = value_coup(*array_gabriel,bonus)

  value_duarte = value_coup(*array_duarte,bonus)

  if value_gabriel > value_duarte :
    return "Gabriel"
  elif value_gabriel < value_duarte:
    return "Duarte"
  return "Empate"

#Sami - Ingrid - Juan - Elen - Tiago - Lara