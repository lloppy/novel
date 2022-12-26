transform offsetLeftPos:
    xpos -0.5

transform offsetRightPos:
    xpos 1.5


define OffsetLeftToLeftSide = MoveTransition(
    delay = 0.6,
    enter=offsetLeftPos,
    leave=offsetLeftPos,
    old=False,
    layers=['master'],
    time_warp=ease,
    enter_time_warp=None,
    leave_time_warp=None
)

define OffsetRightToCenterSide = MoveTransition(
    delay = 1.2,
    enter=offsetRightPos,
    leave=offsetRightPos,
    old=False,
    layers=['master'],
    time_warp=ease,
    enter_time_warp=None,
    leave_time_warp=None
)

define OffsetLeftToCenterSide = MoveTransition(
    delay = 1.2,
    enter=offsetLeftPos,
    leave=offsetLeftPos,
    old=False,
    layers=['master'],
    time_warp=ease,
    enter_time_warp=None,
    leave_time_warp=None
)

define OffsetRightToRightSide = MoveTransition(
    delay = 0.6,
    enter = offsetRightPos,
    leave=offsetRightPos,
    old=False,
    layers=['master'],
    time_warp=ease,
    enter_time_warp=None,
    leave_time_warp=None
)