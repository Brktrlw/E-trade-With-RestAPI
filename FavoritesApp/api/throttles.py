from rest_framework.throttling import UserRateThrottle


class FavoriteThrottle(UserRateThrottle):
    scope = "favoriteThrottle"

