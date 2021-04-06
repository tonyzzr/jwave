import unittest
from jwave import signal_processing
from jwave.utils import assert_pytree_isclose
from jax import numpy as jnp
import jax

ABS_PRECISION = 1e-6
RELATIVE_PRECISION = 1e-3


def test_tone_burst():
    reference = jnp.array(
        [
            0,
            0.0116106812198371,
            0.0281315266413015,
            0.0380505006822615,
            0.0224804807780111,
            -0.0327089065284956,
            -0.117203793311269,
            -0.183440596806675,
            -0.160280510250017,
            -7.95169209971387e-17,
            0.264257886527873,
            0.498643240901267,
            0.525270959485276,
            0.241687945273733,
            -0.27386832131183,
            -0.76426473639934,
            -0.931588219014693,
            -0.633921715227677,
            -4.89858719658941e-16,
            0.633921715227676,
            0.931588219014693,
            0.76426473639934,
            0.273868321311831,
            -0.241687945273732,
            -0.525270959485276,
            -0.498643240901267,
            -0.264257886527873,
            -2.38550762991416e-16,
            0.160280510250017,
            0.183440596806675,
            0.117203793311269,
            0.0327089065284956,
            -0.022480480778011,
            -0.0380505006822614,
            -0.0281315266413015,
            -0.0116106812198371,
            0,
        ]
    )
    signal = signal_processing.tone_burst(9, 1, 4)
    assert_pytree_isclose(signal, reference)


if __name__ == "__main__":
    test_tone_burst()
