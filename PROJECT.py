import random
from time import sleep

player_wins = 0
computer_wins = 0

deck = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
round = 1
print('Добро пожаловать в игру "Blackjack"\n')

while True:
    print(f'Сейчас {round}-й раунд')
    print(f'Счет: Вы - ({player_wins}:{computer_wins}) - Компьютер')

    # Инициализация нового раунда
    player_cards = []
    player_sum = 0

    computer_cards = []
    computer_sum = 0

    cards = [(mast, numb) for mast in range(4) for numb in ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
    random.shuffle(cards)

    # Раздача карт
    player_cards.append(cards.pop())
    player_cards.append(cards.pop())
    for mast, numb in player_cards:
        if numb == 'A':
            if player_sum + 11 > 21:
                player_sum += 1
            else:
                player_sum += 11
        else:
            player_sum += deck[numb]

    computer_cards.append(cards.pop())
    computer_cards.append(cards.pop())
    for mast, numb in computer_cards:
        if numb == 'A':
            if computer_sum + 11 > 21:
                computer_sum += 1
            else:
                computer_sum += 11
        else:
            computer_sum += deck[numb]

    # ход человекав
    while True:
        print('Ваши карты: ', end='')
        for mast, numb in player_cards:
            print(numb, ['clubs', 'hearts', 'spades', 'diamonds'][mast], end='; ')

        print(f'\nСумма ваших очков: {player_sum}')

        if player_sum > 21:
            sleep(1)
            break

        command = input('Hit or Stand? (h/s) > ')
        if command.lower() == 's':
            break
        elif command.lower() == 'h':
            card = cards.pop()
            numb = card[1]
            player_cards.append(card)

            if numb == 'A':
                if player_sum + 11 > 21:
                    player_sum += 1
                else:
                    player_sum += 11
            else:
                player_sum += deck[numb]
        print()

    # ход компьютера
    while True:
        if computer_sum + 5 <= 21:
            card = cards.pop()
            numb = card[1]
            computer_cards.append(card)

            if numb == 'A':
                if computer_sum + 11 > 21:
                    computer_sum += 1
                else:
                    computer_sum += 11
            else:
                computer_sum += deck[numb]
        else:
            break

    print('\nКарты компьютера: ', end='')
    for mast, numb in computer_cards:
        print(numb, ['clubs', 'hearts', 'spades', 'diamonds'][mast], end='; ')

    print(f'\nСумма очков компьютера: {computer_sum}')

    if (player_sum == computer_sum) or (computer_sum > 21 and player_sum > 21):
        print('\nНичья!\n')
        sleep(2)
        round += 1
    elif player_sum > 21 or (player_sum < computer_sum and computer_sum < 22):
        print('\nПобедил компьютер!\n')
        sleep(2)
        computer_wins += 1
        round += 1
    else:
        print('\nВы победили!\n')
        sleep(2)
        player_wins += 1
        round += 1

    y = input("Хотите сыграть еще раз? Y/N ")
    if y.upper() == 'Y':
        continue
    else:
        break
