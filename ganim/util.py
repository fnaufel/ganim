"""
Utilities module for ganim.

"""

import numpy as np


def is_in_segment_box(point, seg):

    x, y = point

    xa, xb = seg.xa, seg.xb
    if xa > xb:
        xa, xb = xb, xa

    ya, yb = seg.ya, seg.yb
    if ya > yb:
        ya, yb = yb, ya

    return (
        xa <= x <= xb
        and
        ya <= y <= yb
    )


def segment_intersection(seg1, seg2, prolong=False):

    coeffs_1 = [
        seg1.yb - seg1.ya,
        -(seg1.xb - seg1.xa)
    ]

    indep_1 = -(
            (seg1.yb - seg1.ya) * seg1.xa
            - (seg1.xb - seg1.xa) * seg1.ya
    )

    coeffs_2 = [
        seg2.yb - seg2.ya,
        -(seg2.xb - seg2.xa)
    ]

    indep_2 = -(
            (seg2.yb - seg2.ya) * seg2.xa
            - (seg2.xb - seg2.xa) * seg2.ya
    )

    a = np.array([coeffs_1, coeffs_2])
    b = np.array([indep_1, indep_2])

    try:
        intersection = np.linalg.solve(a, b)
    except np.linalg.LinAlgError:
        return None

    x, y = intersection

    if prolong:
        return x, y

    if (
            is_in_segment_box(intersection, seg1)
            and
            is_in_segment_box(intersection, seg2)
    ):
        return x, y
    else:
        return None
