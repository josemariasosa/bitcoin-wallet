#!/usr/bin/env python
# coding=utf-8

# Account Manager | Bitcoin Wallet
# ------------------------------------------------------------------------------
# josemariasosa 🧡

import os
import random

from utils.coinkite.rolls_fun import generate_mnemonic_from_string


DEFAULT_TOTAL_DICE_ROLLS = int(os.environ['DEFAULT_TOTAL_DICE_ROLLS'])
DEFAULT_USER_PARAMS = {
    'name': 'jomsosa',
    'testnet': True
}

def generate_initial_entropy():
    r = ''
    for roll in range(DEFAULT_TOTAL_DICE_ROLLS):
        r += str(random.randint(1, 6))
    return r


def create_account(user_params=DEFAULT_USER_PARAMS, key='new'):
    if key  == 'new':
        r = generate_initial_entropy()
        mnemonic = generate_mnemonic_from_string(r)

    print(mnemonic)
    print('jose')
