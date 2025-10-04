"""A simple checker for functions in fantasy_draft_functions.py."""

from typing import Any, Dict
import unittest
import checker_generic
import fantasy_draft_functions as df

FILENAME = "fantasy_draft_functions.py"
PYTA_CONFIG = "a1_pyta.txt"
TARGET_LEN = 79
SEP = "="

CONSTANTS = {
    "POINTS_PER_GOAL": 4,
    "POINTS_PER_ASSIST": 2,
    "POINTS_PER_HIT": 0.25,
    "F_DCS_PER_POINT": 10,
    "D_DCS_PER_POINT": 5,
    "FORWARDS_NEEDED": 3,
    "DEFENCEMEN_NEEDED": 2,
    "GOALIES_NEEDED": 1,
    "BUDGET": 100,
    "PLAYERS_TO_SELECT": 6,
    "FORWARD": "F",
    "DEFENCEMEN": "D",
    "GOALIE": "G",
    "GAA_VALUE": 10,
    "SV_VALUE": 100,
}


class CheckTest(unittest.TestCase):
    """Sanity checker for assignment functions."""

    def test_is_player_available(self) -> None:
        """Function winning."""

        self._check(df.is_player_available, ["MGO", "DOL_NCA_MGO_AHS_"], bool)

    def test_get_player_id(self) -> None:
        """Function get_player_id."""

        self._check(df.get_player_id, ["MGO_PD_G0-_A14_DC43_H70_Pr5-"], str)

    def test_get_position(self) -> None:
        """Function get_position."""

        self._check(df.get_position, ["MGO_PD_G0-_A14_DC43_H70_Pr5-"], str)

    def test_get_price(self) -> None:
        """Function get_price."""

        self._check(df.get_price, ["MGO_PD_G0-_A14_DC43_H70_Pr5-"], int)

    def test_can_afford(self) -> None:
        """Function can_afford."""

        self._check(df.can_afford, [100, "MGO_PD_G0-_A14_DC43_H70_Pr5-"], bool)

    def test_update_budget(self) -> None:
        """Function update_budget."""

        self._check(df.update_budget, [
                    100, "MGO_PD_G0-_A14_DC43_H70_Pr5-"], int)

    def test_can_select(self) -> None:
        """Function can_select."""

        self._check(df.can_select, [
                    "MGO_PD_G0-_A14_DC43_H70_Pr5-", 3, 1, 1], bool)

    def test_add_to_team(self) -> None:
        """Function add_to_team."""

        self._check(df.add_to_team, ["MGO_PD_G0-_A14_DC43_H70_Pr5-", ""], str)

    def test_remove_player(self) -> None:
        """Function remove_player."""

        self._check(df.remove_player, ["DOL_NCA_MGO_AHS_", 3], str)

    def test_compute_dc_points(self) -> None:
        """Function compute_dc_points."""

        self._check(df.compute_dc_points, [
                    "MGO_PD_G0-_A14_DC43_H70_Pr5-"], int)

    def test_compute_goal_points(self) -> None:
        """Function compute_goal_points."""

        self._check(df.compute_goal_points, [
                    "MGO_PD_G0-_A14_DC43_H70_Pr5-"], int)

    def test_compute_assist_points(self) -> None:
        """Function compute_assist_points."""

        self._check(df.compute_assist_points, [
                    "MGO_PD_G0-_A14_DC43_H70_Pr5-"], int)

    def test_compute_hit_points(self) -> None:
        """Function compute_hit_points."""

        self._check(df.compute_hit_points, [
                    "MGO_PD_G0-_A14_DC43_H70_Pr5-"], float)

    def test_compute_fantasy_score(self) -> None:
        """Function compute_fantasy_score."""

        self._check(
            df.compute_fantasy_score, ["MGO_PD_G0-_A14_DC43_H70_Pr5-"], float
        )

    def test_check_constants(self) -> None:
        """Values of constants."""

        print("\nChecking that constants refer to their original values")
        self._check_constants(CONSTANTS, df)
        print("  check complete")

    def _check(self, func: callable, args: list, ret_type: type) -> None:
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.

        """

        print("\nChecking {}...".format(func.__name__))
        result = checker_generic.check(func, args, ret_type)
        self.assertTrue(result[0], result[1])
        print("  check complete")

    def _check_constants(self, name2value: Dict[str, object], mod: Any) -> None:
        """Check that, for each (name, value) pair in name2value, the value of
        a variable named name in module mod is value.
        """

        for name, expected in name2value.items():
            actual = getattr(mod, name)
            msg = "The value of constant {} should be {} but is {}.".format(
                name, expected, actual
            )
            self.assertEqual(expected, actual, msg)


print("".center(TARGET_LEN, SEP))
print(" Start: checking coding style ".center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
print(" End checking coding style ".center(TARGET_LEN, SEP))

print(" Start: checking type contracts ".center(TARGET_LEN, SEP))
unittest.main(exit=False)
print(" End checking type contracts ".center(TARGET_LEN, SEP))

print("\nScroll up to see ALL RESULTS:")
print("  - checking coding style")
print("  - checking type contract\n")
