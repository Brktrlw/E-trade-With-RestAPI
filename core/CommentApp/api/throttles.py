

from rest_framework.throttling import AnonRateThrottle

class CommentThrottle(AnonRateThrottle):
    scope = "commentThrottle"

