# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

STEP = 50
COMMISSION_PERCENT = 1.5
COMMISSION_MIN = 30
COMMISSION_MAX = 600
REWARD_PERCENT = 3
WEALTH_SUM = 5_000_000
TAX_ON_WEALTH = 10
work_flag = True
operation_count = 0
logs = []
account = 0


def deposit(amount: int) -> str:
    global operation_count, account, logs
    if amount % 50 == 0:
        if amount >= WEALTH_SUM:
            amount -= amount * TAX_ON_WEALTH / 100
        operation_count += 1
        if operation_count % 3 == 0:
            amount += amount * REWARD_PERCENT / 100
        account += amount
        logs.append(amount)
        result = f'Пополнение успешно.\nБаланс на счете: {account}.'
    else:
        result = 'Сумма пополнения должна быть кратна 50.'
    return result


def withdraw(amount: int) -> str:
    global operation_count, account
    if amount % 50 == 0 and amount <= account:
        if WEALTH_SUM <= amount <= (account - (amount + amount * TAX_ON_WEALTH / 100)):
            account -= amount * TAX_ON_WEALTH / 100
        elif WEALTH_SUM <= amount:
            return 'Средств на счете недостаточно.'

        tax = amount * COMMISSION_PERCENT / 100
        if tax < COMMISSION_MIN:
            tax = COMMISSION_MIN
        elif tax > COMMISSION_MAX:
            tax = COMMISSION_MAX

        if account - amount - tax >= 0:
            account = account - amount - tax
            logs.append(-amount)
            operation_count += 1
            if operation_count % 3 == 0:
                account += amount * REWARD_PERCENT / 100
            result = f'Снятие успешно.\nБаланс на счете: {account}.'
        else:
            result = 'Средств на счете недостаточно.'
    elif amount % 50 != 0:
        result = 'Сумма снятия должна быть кратна 50.'
    else:
        result = 'Средств на счете недостаточно.'
    return result


def quit_() -> str:
    global work_flag
    work_flag = False
    return f'Баланс на счете: {account}.\nРабота завершена.'


while work_flag:
    k = input('Выберите операцию:\n1. Внести\n2. Снять\n3. Вывести историю\n4. Выйти\n')
    match k:
        case '1':
            income = int(input('Введите сумму кратную 50: '))
            print(deposit(income))
        case '2':
            outlay = int(input('Введите сумму кратную 50: '))
            print(withdraw(outlay))
        case '3':
            for m in logs:
                print(m)
        case '4':
            print(quit_())
