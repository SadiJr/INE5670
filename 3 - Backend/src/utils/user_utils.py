#!/usr/bin/env python

import re


def validate_cpf(cpf: str) -> bool:
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True


def validate_email(email: str) -> bool:
    return re.search(r'^[\w]+@[\w]+\.[\w]{2,4}', email) is not None


def validate_phone(phone: str) -> bool:
    return re.search(r'(^[0-9]{2})?(\s|-)?(9?[0-9]{4})-?([0-9]{4}\$)', phone) is None