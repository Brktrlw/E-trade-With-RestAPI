

from rest_framework.throttling import UserRateThrottle

class CommentThrottle(UserRateThrottle):
    scope = "commentThrottle"

