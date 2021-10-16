def count_distance(steps):
    distance = 1000
    result = distance - steps
    if steps < distance:
        print("Вам осталось пройти", result)
    elif steps == distance:
        print("Вы прошли дистнцию")
    else:
        print("Вы прошли", distance, "и сделали", abs(result), "лишних шагов")

count_distance(1001)