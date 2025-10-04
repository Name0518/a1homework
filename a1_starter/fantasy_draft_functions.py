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


def get_price(player: str) -> int:
    """Returns the price of player if player is non empty;
      Otherwise return 0.

    >>> get_price('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    5
    >>> get_price('RGI_PF_G20_A67_DC43_H8-_Pr20')
    20
    >>> get_price('')
    0

    """
    if player == '':
        return 0
    return int(player[-2:].strip("-"))


def can_select(player: str, forwards_drafted: int, defence_drafted: int, goalies_drafted: int) -> bool:
    """Return True if player can be selected without 
    exceeding the maximum amount of forwards_drafted,
    defence_drafted, and goalies_drafted, 
    or if the player is an empty string; 
    otherwise return False.

    >>> can_select('MGO_PD_G0-_A14_DC43_H70_Pr5-', 2, 1, 1)
    True
    >>> can_select('NSH_PF_G7-_A14_DC20_H73_Pr10', 3, 2, 1)
    False
    >>> can_select('', 3, 2, 1)
    True

    """
    if player == '':
        return True
    if get_position(player) == FORWARD and forwards_drafted < FORWARDS_NEEDED:
        return True
    if get_position(player) == DEFENCEMEN and defence_drafted < DEFENCEMEN_NEEDED:
        return True
    if get_position(player) == GOALIE and goalies_drafted < GOALIES_NEEDED:
        return True
    return False


def can_afford(budget: int, player: str) -> bool:
    """Return True if the player can be afforded with the current budget;
    otherwise return False.

    >>> can_afford(20, 'MGO_PD_G0-_A14_DC43_H70_Pr5-')
    True
    >>> can_afford(4, 'NSH_PF_G7-_A14_DC20_H73_Pr10')
    False

    """
    return (budget - get_price(player)) >= 0


def update_budget(budget: int, player: str) -> int:
    """Return the budget after drafting a player.

    >>> update_budget(50,"CLA_PG_GAA2.23_SV0.910_Pr20")
    30
    >>> update_budget(70,"GMC_PG_GAA2.57_SV0.902_Pr15")
    55
    >>> update_budget(10,"RRO_PF_G35_A35_DC43_H39_Pr25")
    -15

    """
    return budget - get_price(player)


def add_to_team(player: str, all_players: str) -> str:
    """Return the string of all_players after adding a new player to the team.

    >>> add_to_team('MGO_PD_G0-_A14_DC43_H70_Pr5-', 'DOL_NCA_')
    'DOL_NCA_MGO_'
    >>> add_to_team('CLA_PG_GAA2.23_SV0.910_Pr20', 'DOL_NCA_MGO_')
    'DOL_NCA_MGO_CLA_'
    >>> add_to_team('','DOL_NCA_MGO_')
    'DOL_NCA_MGO_'

    """
    return all_players + player[:4]


def remove_player(players: str, index: int) -> str:
    """Return the string of players after removing the 3-letter player ID 
    that ends at the given index if the index corresponds to a '_' separator.
    If the index is not at the seperator '-' or is invalid,
    return the original unaltered team string.

    >>> remove_player('DOL_NCA_MGO_AHS_', 7)
    'DOL_MGO_AHS_'
    >>> remove_player('DOL_NCA_MGO_AHS_', 2)
    'DOL_NCA_MGO_AHS_'
    >>> remove_player('DOL_NCA_MGO_AHS_', 20)
    'DOL_NCA_MGO_AHS_'

    """
    if 0 <= index <= len(players) and players[index] == "_":
        return players.replace(players[index - 4:index], '')
    return players


def compute_dc_points(player: str) -> int:
    """Return defensive contribution (DC) points of 
    the player in player string if player is non-empty and a skater;
    otherwise return 0.

    >>> compute_dc_points('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    8
    >>> compute_dc_points('AMP_PF_G10_A10_DC51_H30_Pr10')
    5
    >>> compute_dc_points('CLA_PG_GAA2.23_SV0.910_Pr20')
    0
    >>> compute_dc_points('')
    0

    """
    if get_position(player) == DEFENCEMEN:
        return int(player[17:19].strip("-")) // D_DCS_PER_POINT
    if get_position(player) == FORWARD:
        return int(player[17:19].strip("-")) // F_DCS_PER_POINT
    return 0


def compute_goal_points(player: str) -> int:
    """Return goal points of the player in player string 
    if player is non-empty and a skater;
    otherwise return 0.

    >>> compute_goal_points('NCA_PD_G4-_A9-_DC50_H66_Pr10')
    16
    >>> compute_goal_points('AMP_PF_G10_A10_DC51_H30_Pr10')
    40
    >>> compute_goal_points('CLA_PG_GAA2.23_SV0.910_Pr20')
    0
    >>> compute_goal_points('')
    0

    """
    if get_position(player) == DEFENCEMEN or get_position(player) == FORWARD:
        return int(player[8:10].strip("-")) * POINTS_PER_GOAL
    return 0


def compute_assist_points(player: str) -> int:
    """Return assist points of the player in player string 
    if player is non-empty and a skater;
    otherwise return 0.

    >>> compute_assist_points('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    28
    >>> compute_assist_points('CLA_PG_GAA2.23_SV0.910_Pr20')
    0
    >>> compute_assist_points('AMP_PF_G10_A10_DC51_H30_Pr10')
    20
    >>> compute_assist_points('')
    0

    """
    if get_position(player) == DEFENCEMEN or get_position(player) == FORWARD:
        return int(player[12:14].strip("-")) * POINTS_PER_ASSIST
    return 0


def compute_hit_points(player: str) -> float:
    """Return hit points of the player in player string 
    if player is non-empty and a skater;
    otherwise return 0.

    >>> compute_hit_points('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    17.5
    >>> compute_hit_points('CLA_PG_GAA2.23_SV0.910_Pr20')
    0
    >>> compute_hit_points('AMP_PF_G10_A10_DC51_H30_Pr10')
    7.5
    >>> compute_hit_points('')
    0

    """
    if get_position(player) == DEFENCEMEN or get_position(player) == FORWARD:
        return int(player[21:23].strip("-")) * POINTS_PER_HIT
    return 0


def compute_fantasy_score(player: str) -> float:
    """Return the fantasy score of the player in player string 
    if player is non-empty;
    otherwise return 0.

    >>> compute_fantasy_score('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    53.5
    >>> compute_fantasy_score('CLA_PG_GAA2.23_SV0.910_Pr20')
    68.7
    >>> compute_fantasy_score('AMP_PF_G10_A10_DC51_H30_Pr10')
    72.5
    >>> compute_fantasy_score('')
    0

    """
    if get_position(player) != GOALIE:
        return compute_goal_points(player) + compute_assist_points(player) + compute_hit_points(player) + compute_dc_points(player)
    if get_position(player) == GOALIE:
        sv = float(player[17:22])
        gaa = float(player[10:14])
        return SV_VALUE * sv - GAA_VALUE * gaa
    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
