from rest_framework.throttling import UserRateThrottle

class CustomUserThrottle(UserRateThrottle):
    rate = '10/minute'  # 10 requests per minute for regular users

class CustomAdminThrottle(UserRateThrottle):
    rate = '30/minute'  # 30 requests per minute for admins
