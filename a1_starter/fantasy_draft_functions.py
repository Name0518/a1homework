"""CSCA08: Fall 2025 -- Assignment 1: Ice Hockey Fantasy Draft

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020-2025 Mario Badr, Jennifer Campbell, Tom Fairgrieve,
Diane Horton, Michael Liut, Jacqueline Smith, and Anya Tafliovich.

"""

from constants import (
    POINTS_PER_GOAL,
    POINTS_PER_ASSIST,
    POINTS_PER_HIT,
    F_DCS_PER_POINT,
    D_DCS_PER_POINT,
    FORWARDS_NEEDED,
    DEFENCEMEN_NEEDED,
    GOALIES_NEEDED,
    BUDGET,
    PLAYERS_TO_SELECT,
    FORWARD,
    DEFENCEMEN,
    GOALIE,
    SV_VALUE,
    GAA_VALUE,
)


# provided
def get_player_id(player: str) -> str:
    """Return the id of player if the string is non-empty;
    otherwise return the empty string.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string

    >>> get_player_id('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    'MGO'
    >>> get_player_id('NSH_PF_G7-_A14_DC20_H73_Pr10')
    'NSH'
    >>> get_player_id('')
    ''

    """

    return player[:3]


# provided as example of calling another function as helper
def is_player_available(player: str, players_available: str) -> bool:
    """Return True if and only if the id of player is in players_available.

    Precondition: player is the string of player stats
                  as seen in players.txt or the empty string,
                  players_available is the string of player ids
                  that are currently available for selection seperated
                  by _.

    >>> is_player_available('MGO_PD_G0-_A14_DC43_H70_Pr5-', 'DOL_NCA_MGO_AHS_')
    True
    >>> is_player_available('GGG_PD_G0-_A14_DC43_H70_Pr5-', 'DOL_NCA_MGO_AHS_')
    False
    >>> is_player_available('', 'DOL_NCA_MGO_AHS_')
    False

    """

    if len(player) == 0:
        return False
    return get_player_id(player) in players_available


# provided
def get_position(player: str) -> str:
    """Return the position of player if player is non-empty;
    otherwise return the empty string.

    Precondition: player is the string of player stats
    as seen in players.txt or the empty string

    >>> get_position('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    'D'
    >>> get_position('NSH_PF_G7-_A14_DC20_H73_Pr10')
    'F'
    >>> get_position('CLA_PG_GAA2.23_SV0.910_Pr20')
    'G'
    >>> get_position('')
    ''

    """

    if len(player) == 0:
        return ""
    return player[5]

def get_price(player:str) -> int:
    if player == "":
        return 0
    if player[-1] == '-':
        return int(player[-2])
    else:
        return int(player[-2:])

def can_select(player: str, forwards_drafted: int, defence_drafted: int, goalies_drafted: int) -> bool:
    """Return True if and only if the player can be selected based on
    the position and how many players of that position have already been drafted.
    >>> can_select('MGO_PD_G0-_A14_DC43_H70_Pr5-', 2, 2, 1)
    True
    >>> can_select('NSH_PF_G7-_A14_DC20_H73_Pr10', 3, 2, 1)
    False
    """
    if player == "":
        return True
    if get_position(player) == FORWARD and forwards_drafted < FORWARDS_NEEDED:
        return True
    elif get_position(player) == DEFENCEMEN and defence_drafted < DEFENCEMEN_NEEDED:
        return True
    elif get_position(player) == GOALIE and goalies_drafted < GOALIES_NEEDED:
        return True
    return False


def can_afford(budget: int, player: str) -> bool:
    """Return True if and only if the player can be afforded based on the budget.
    >>> can_afford(20, 'MGO_PD_G0-_A14_DC43_H70_Pr5-')
    True
    >>> can_afford(4, 'NSH_PF_G7-_A14_DC20_H73_Pr10')
    False"""
    return (budget - get_price(player)) >= 0


def update_budget(budget: int, player: str) -> int:
    """Return the budget after the purchase of a player.
    >>> update_budget(50,"CLA_PG_GAA2.23_SV0.910_Pr20")
    30
    >>> update_budget(70,"GMC_PG_GAA2.57_SV0.902_Pr15")
    45
    """
    return budget - get_price(player)


def add_to_team(player: str, all_players: str) -> str:
    return all_players + player[:4]


def remove_player(player: str, index: int) -> str:
    if index >= 0 and player[index] == "_":
        return player.replace(player[index-3:index], '')
    else:
        return player


def compute_dc_points(player: str) -> int:
    if get_position(player) == DEFENCEMEN:
        return int(player[17:19].strip("-")) // D_DCS_PER_POINT
    elif get_position(player) == FORWARD:
        return int(player[17:19].strip("-")) // F_DCS_PER_POINT
    else:
        return 0


def compute_goal_points(player: str) -> int:
    if get_position(player) == DEFENCEMEN or get_position(player) == FORWARD:
        return int(player[8:9].strip("-")) * POINTS_PER_GOAL
    else:
        return 0


def compute_assist_points(player: str) -> int:
    if get_position(player) == DEFENCEMEN or get_position(player) == FORWARD:
        return int(player[12:14].strip("-")) * POINTS_PER_ASSIST
    else:
        return 0


def compute_hit_points(player: str) -> int:
    if get_position(player) == DEFENCEMEN or get_position(player) == FORWARD:
        return int(player[21:23].strip("-")) * POINTS_PER_HIT
    else:
        return 0


def compute_goalie_points(player: str) -> int:
    if get_position(player) == GOALIE:
        sv = float(player[17:22])
        gaa = float(player[10:14])
        return int(sv * SV_VALUE - gaa * GAA_VALUE)
    else:
        return 0

def compute_fantasy_score(player:str) -> float:
    if get_position(player) != GOALIE:
        return compute_goal_points(player) + compute_assist_points(player) + compute_hit_points(player) + compute_dc_points(player)
    elif get_position(player) == GOALIE:
        sv = float(player[17:22])
        gaa = float(player[10:14])
        return SV_VALUE * sv - GAA_VALUE * gaa
    else:
        return 0

if __name__ == "__main__":
    import doctest

    doctest.testmod()
