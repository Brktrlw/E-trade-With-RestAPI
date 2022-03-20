from rest_framework.throttling import UserRateThrottle


class SellerThrottle(UserRateThrottle):
    scope = "sellerThrottle"