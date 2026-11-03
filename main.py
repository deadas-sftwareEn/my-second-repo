from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy = Character("Goblin", 20, 3)
    enemy_2nd = Character("Skeleton Knight", 25, 4)

    print(hero)
    print(enemy)
    print(enemy_2nd)
    print()

    while hero.is_alive() and enemy.is_alive() or enemy_2nd.is_alive():
        if enemy.is_alive():
            hero.attack(enemy)
        if enemy_2nd.is_alive():
            hero.attack(enemy_2nd)

        if enemy.is_alive():
            enemy.attack(hero)
        if enemy_2nd.is_alive():
            enemy_2nd.attack(hero)
        print(hero)
        print(enemy)
        print(enemy_2nd)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"Enemies win!")

if __name__ == "__main__":
    main()
